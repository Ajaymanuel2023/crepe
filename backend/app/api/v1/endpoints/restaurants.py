from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.models.restaurant import Restaurant
from app.schemas.restaurant import RestaurantResponse

router = APIRouter()

@router.get("/", response_model=List[RestaurantResponse])
def get_restaurants(
    skip: int = 0,
    limit: int = 20,
    cuisine: str = None,
    db: Session = Depends(get_db)
):
    """Get list of restaurants with optional filters"""
    query = db.query(Restaurant).filter(Restaurant.is_active == True)
    
    if cuisine:
        query = query.filter(Restaurant.cuisine_type.ilike(f"%{cuisine}%"))
    
    restaurants = query.offset(skip).limit(limit).all()
    return restaurants

@router.get("/{restaurant_id}", response_model=RestaurantResponse)
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    """Get specific restaurant by ID"""
    restaurant = db.query(Restaurant).filter(
        Restaurant.id == restaurant_id,
        Restaurant.is_active == True
    ).first()
    
    if not restaurant:
        raise HTTPException(status_code=404, detail="Restaurant not found")
    
    return restaurant

@router.get("/search/{query}")
def search_restaurants(
    query: str,
    db: Session = Depends(get_db)
):
    """Search restaurants by name or cuisine"""
    restaurants = db.query(Restaurant).filter(
        Restaurant.is_active == True,
        (Restaurant.name.ilike(f"%{query}%") | 
         Restaurant.cuisine_type.ilike(f"%{query}%"))
    ).all()
    
    return restaurants
