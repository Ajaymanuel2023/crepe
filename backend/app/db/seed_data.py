from sqlalchemy.orm import Session
from app.models.restaurant import Restaurant
from app.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_seed_data(db: Session):
    """Create initial seed data for development"""
    
    # Check if data already exists
    if db.query(Restaurant).first():
        print("Seed data already exists, skipping...")
        return
    
    # Create sample restaurants
    restaurants = [
        Restaurant(
            name="Pizza Palace",
            description="Authentic Italian pizzas with fresh ingredients",
            cuisine_type="Italian",
            address="123 Main St, Downtown",
            phone="+1-555-0101",
            price_range="$",
            delivery_time=30,
            delivery_fee=2.99,
            rating=4.5,
            image_url="https://images.unsplash.com/photo-1513104890138-7c749659a591?w=400"
        ),
        Restaurant(
            name="Burger Barn",
            description="Juicy burgers and crispy fries",
            cuisine_type="American",
            address="456 Oak Ave, Midtown",
            phone="+1-555-0102",
            price_range="$",
            delivery_time=25,
            delivery_fee=1.99,
            rating=4.2,
            image_url="https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400"
        ),
        Restaurant(
            name="Sushi Zen",
            description="Fresh sushi and Japanese cuisine",
            cuisine_type="Japanese",
            address="789 Pine St, Uptown",
            phone="+1-555-0103",
            price_range="$$",
            delivery_time=45,
            delivery_fee=3.99,
            rating=4.8,
            image_url="https://images.unsplash.com/photo-1579584425555-c3ce17fd4351?w=400"
        ),
        Restaurant(
            name="Taco Fiesta",
            description="Authentic Mexican tacos and burritos",
            cuisine_type="Mexican",
            address="321 Elm St, South Side",
            phone="+1-555-0104",
            price_range="$",
            delivery_time=20,
            delivery_fee=1.49,
            rating=4.3,
            image_url="https://images.unsplash.com/photo-1565299624946-b28f40a0ca4b?w=400"
        ),
        Restaurant(
            name="Curry House",
            description="Spicy Indian curries and naan bread",
            cuisine_type="Indian",
            address="654 Maple Dr, East End",
            phone="+1-555-0105",
            price_range="$",
            delivery_time=35,
            delivery_fee=2.49,
            rating=4.6,
            image_url="https://images.unsplash.com/photo-1585937421612-70a008356fbe?w=400"
        )
    ]
    
    # Add restaurants to database
    for restaurant in restaurants:
        db.add(restaurant)
    
    # Create a test user
    test_user = User(
        email="test@example.com",
        full_name="Test User",
        phone="+1-555-9999",
        hashed_password=pwd_context.hash("testpassword123")
    )
    db.add(test_user)
    
    # Commit all changes
    db.commit()
    print("✅ Seed data created successfully!")
    print("🍕 Created 5 sample restaurants")
    print("👤 Created test user: test@example.com (password: testpassword123)")