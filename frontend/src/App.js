import React from 'react';
import './App.css'; // Assuming you might add some global CSS later
import ApplicantForm from './components/ApplicantForm';
import LoanOfficerDashboard from './components/LoanOfficerDashboard';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Online Loan Application Platform</h1>
      </header>
      <main>
        <section>
          <h2>Apply for a Loan</h2>
          <ApplicantForm />
        </section>
        <section>
          <h2>Loan Officer Dashboard</h2>
          <LoanOfficerDashboard />
        </section>
      </main>
    </div>
  );
}

export default App;
