import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/home/HomePage.tsx';
import './App.css';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/restaurant/:id" element={<div>Restaurant Page</div>} />
          <Route path="/login" element={<div>Login Page</div>} />
          <Route path="/cart" element={<div>Cart Page</div>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;