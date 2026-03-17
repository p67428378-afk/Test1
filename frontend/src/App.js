import React, { useState } from 'react';
import ApplicantForm from './components/ApplicantForm';
import LoanOfficerDashboard from './components/LoanOfficerDashboard';

function App() {
  const [view, setView] = useState('applicant'); // 'applicant' or 'officer'

  return (
    <div className="App">
      <nav style={{ marginBottom: '20px' }}>
        <button onClick={() => setView('applicant')} style={{ marginRight: '10px' }}>Applicant View</button>
        <button onClick={() => setView('officer')}>Loan Officer View</button>
      </nav>
      <header className="App-header">
        <h1>Online Loan Application Platform</h1>
      </header>
      {
        view === 'applicant' ? <ApplicantForm /> : <LoanOfficerDashboard />
      }
    </div>
  );
}

export default App;
