import React from 'react';

const HomePage: React.FC = () => {
  return (
    <div className="container mx-auto px-4 py-8">
      <header className="text-center mb-8">
        <h1 className="text-4xl font-bold text-primary-600 mb-2">
          FoodieClone
        </h1>
        <p className="text-gray-600">
          Discover great food & restaurants near you
        </p>
      </header>
      
      <div className="max-w-md mx-auto">
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h2 className="text-xl font-semibold mb-4">Search Restaurants</h2>
          <input
            type="text"
            placeholder="Enter your location"
            className="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500"
          />
          <button className="btn-primary w-full mt-4">
            Find Restaurants
          </button>
        </div>
      </div>
    </div>
  );
}

export default HomePage;