import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import LoanApplicationForm from './components/LoanApplicationForm';
import LoanOfficerDashboard from './components/LoanOfficerDashboard';
import './App.css'; // Assuming you'll create this for basic styling

function App() {
  return (
    <Router>
      <div className="App">
        <nav>
          <ul>
            <li>
              <Link to="/">Apply for Loan</Link>
            </li>
            <li>
              <Link to="/officer-dashboard">Officer Dashboard</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/" element={<LoanApplicationForm />} />
          <Route path="/officer-dashboard" element={<LoanOfficerDashboard />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
