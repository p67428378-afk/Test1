import React, { useState, useEffect } from 'react';

function LoanOfficerDashboard() {
  const [applications, setApplications] = useState([]);
  const [selectedApplication, setSelectedApplication] = useState(null);
  const [officerId, setOfficerId] = useState(null); // Placeholder for logged-in officer ID
  const [loginForm, setLoginForm] = useState({
    email: '',
    password: '',
  });
  const [registerForm, setRegisterForm] = useState({
    full_name: '',
    email: '',
    password: '',
  });
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

  useEffect(() => {
    if (officerId) {
      fetchApplications();
    }
  }, [officerId]);

  const fetchApplications = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/applications`);
      if (response.ok) {
        const data = await response.json();
        setApplications(data);
      } else {
        setError('Failed to fetch applications.');
      }
    } catch (err) {
      setError('Network error while fetching applications.');
      console.error('Fetch applications error:', err);
    }
  };

  const handleLoginChange = (e) => {
    const { name, value } = e.target;
    setLoginForm({ ...loginForm, [name]: value });
  };

  const handleRegisterChange = (e) => {
    const { name, value } = e.target;
    setRegisterForm({ ...registerForm, [name]: value });
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    setMessage('');
    setError('');
    try {
      const response = await fetch(`${API_BASE_URL}/loan_officers/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(loginForm),
      });
      const data = await response.json();
      if (response.ok) {
        setMessage(data.message);
        setOfficerId(data.loan_officer_id);
      } else {
        setError(data.message || 'Login failed.');
      }
    } catch (err) {
      setError('Network error during login.');
    }
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    setMessage('');
    setError('');
    try {
      const response = await fetch(`${API_BASE_URL}/loan_officers/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(registerForm),
      });
      const data = await response.json();
      if (response.ok) {
        setMessage(data.message + '. Please log in.');
        setRegisterForm({ full_name: '', email: '', password: '' });
      } else {
        setError(data.error || 'Registration failed.');
      }
    } catch (err) {
      setError('Network error during registration.');
    }
  };

  const handleStatusUpdate = async (applicationId, newStatus, comments) => {
    if (!officerId) {
      setError('Please log in as a loan officer to update status.');
      return;
    }
    try {
      const response = await fetch(`${API_BASE_URL}/applications/${applicationId}/status`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ status: newStatus, loan_officer_id: officerId, comments }),
      });
      const data = await response.json();
      if (response.ok) {
        setMessage(data.message);
        fetchApplications(); // Refresh the list
        setSelectedApplication(null); // Close details view
      } else {
        setError(data.error || 'Failed to update status.');
      }
    } catch (err) {
      setError('Network error during status update.');
    }
  };

  if (!officerId) {
    return (
      <div style={{ maxWidth: '400px', margin: 'auto', padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
        <h2>Loan Officer Login</h2>
        <form onSubmit={handleLogin}>
          <label>
            Email:
            <input type="email" name="email" value={loginForm.email} onChange={handleLoginChange} required />
          </label>
          <label>
            Password:
            <input type="password" name="password" value={loginForm.password} onChange={handleLoginChange} required />
          </label>
          <button type="submit">Login</button>
        </form>
        {message && <p style={{ color: 'green' }}>{message}</p>}
        {error && <p style={{ color: 'red' }}>{error}</p>}

        <h3 style={{ marginTop: '30px' }}>Register New Loan Officer</h3>
        <form onSubmit={handleRegister}>
          <label>
            Full Name:
            <input type="text" name="full_name" value={registerForm.full_name} onChange={handleRegisterChange} required />
          </label>
          <label>
            Email:
            <input type="email" name="email" value={registerForm.email} onChange={handleRegisterChange} required />
          </label>
          <label>
            Password:
            <input type="password" name="password" value={registerForm.password} onChange={handleRegisterChange} required />
          </label>
          <button type="submit">Register</button>
        </form>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: '900px', margin: 'auto', padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h2>Loan Officer Dashboard (ID: {officerId})</h2>
      <button onClick={() => setOfficerId(null)} style={{ marginBottom: '20px' }}>Logout</button>
      {message && <p style={{ color: 'green' }}>{message}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      <h3>All Applications</h3>
      {applications.length === 0 ? (
        <p>No applications found.</p>
      ) : (
        <ul>
          {applications.map((app) => (
            <li key={app.id} style={{ border: '1px solid #eee', padding: '10px', margin: '5px 0', cursor: 'pointer' }} onClick={() => setSelectedApplication(app)}>
              Application ID: {app.id} - Applicant: {app.applicant.full_name} - Status: {app.status}
            </li>
          ))}
        </ul>
      )}

      {selectedApplication && (
        <div style={{ marginTop: '30px', border: '1px solid #007bff', padding: '20px', borderRadius: '8px' }}>
          <h3>Application Details (ID: {selectedApplication.id})</h3>
          <p><strong>Status:</strong> {selectedApplication.status}</p>
          <p><strong>Submission Date:</strong> {new Date(selectedApplication.submission_date).toLocaleString()}</p>
          <p><strong>Loan Amount:</strong> ${selectedApplication.loan_amount}</p>
          <p><strong>Tenure:</strong> {selectedApplication.tenure_months} months</p>

          <h4>Applicant Information</h4>
          <p>Name: {selectedApplication.applicant.full_name}</p>
          <p>Contact: {selectedApplication.applicant.contact_info}</p>
          <p>DOB: {selectedApplication.applicant.date_of_birth}</p>
          <p>Address: {selectedApplication.applicant.address}</p>

          <h4>Financial Details</h4>
          <p>Income: ${selectedApplication.financial_details.income}</p>
          <p>Employment: {selectedApplication.financial_details.employment_status}</p>
          <p>Liabilities: ${selectedApplication.financial_details.existing_liabilities || '0'}</p>

          <h4>Bank Details</h4>
          <p>Bank Name: {selectedApplication.bank_details.bank_name}</p>
          <p>Account No: {selectedApplication.bank_details.account_number}</p>
          <p>IFSC/SWIFT: {selectedApplication.bank_details.ifsc_swift_code}</p>

          <h4>Legal Agreements</h4>
          <p>Terms Agreed: {selectedApplication.legal_agreements.terms_agreed ? 'Yes' : 'No'}</p>
          <p>Credit Check Consent: {selectedApplication.legal_agreements.credit_check_consent ? 'Yes' : 'No'}</p>

          <h4>Update Status</h4>
          <select onChange={(e) => handleStatusUpdate(selectedApplication.id, e.target.value, prompt("Add comments for this status update:"))} value={selectedApplication.status}>
            <option value="Pending Review">Pending Review</option>
            <option value="Approved">Approved</option>
            <option value="Rejected">Rejected</option>
          </select>
          <button onClick={() => setSelectedApplication(null)} style={{ marginLeft: '10px' }}>Close Details</button>
        </div>
      )}
    </div>
  );
}

export default LoanOfficerDashboard;
