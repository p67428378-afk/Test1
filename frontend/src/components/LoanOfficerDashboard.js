import React, { useEffect, useState } from 'react';

const LoanOfficerDashboard = () => {
  const [applications, setApplications] = useState([]);
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const fetchApplications = async () => {
    try {
      const response = await fetch(`${process.env.REACT_APP_API_BASE_URL}/api/applications`);
      const data = await response.json();
      if (response.ok) {
        setApplications(data);
      } else {
        setError(data.error || 'Failed to fetch applications');
      }
    } catch (err) {
      setError('Network error or server is unreachable.');
      console.error('Fetch applications error:', err);
    }
  };

  useEffect(() => {
    fetchApplications();
  }, []);

  const handleStatusUpdate = async (appId, status) => {
    setMessage('');
    setError('');
    // In a real application, officer_id would come from authenticated user context
    const officerId = 1; // Placeholder for now

    try {
      const response = await fetch(`${process.env.REACT_APP_API_BASE_URL}/api/applications/${appId}/status`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ status, officer_id: officerId, comments: `Application ${status} by officer ${officerId}` }),
      });

      const data = await response.json();

      if (response.ok) {
        setMessage(data.message);
        fetchApplications(); // Refresh the list
      } else {
        setError(data.error || 'Failed to update status.');
      }
    } catch (err) {
      setError('Network error or server is unreachable.');
      console.error('Status update error:', err);
    }
  };

  return (
    <div style={{ margin: '20px', textAlign: 'left' }}>
      {message && <p style={{ color: 'green' }}>{message}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {applications.length === 0 ? (
        <p>No loan applications to review.</p>
      ) : (
        <ul style={{ listStyleType: 'none', padding: 0 }}>
          {applications.map((app) => (
            <li key={app.id} style={{ border: '1px solid #ccc', margin: '10px 0', padding: '10px' }}>
              <p><strong>Application ID:</strong> {app.id}</p>
              <p><strong>Applicant:</strong> {app.applicant_name}</p>
              <p><strong>Loan Amount:</strong> ${app.loan_amount}</p>
              <p><strong>Tenure:</strong> {app.tenure_months} months</p>
              <p><strong>Status:</strong> {app.status}</p>
              <p><strong>Submitted:</strong> {new Date(app.submission_date).toLocaleString()}</p>
              <div>
                <button onClick={() => handleStatusUpdate(app.id, 'Approved')} disabled={app.status !== 'Pending Review'}>Approve</button>
                <button onClick={() => handleStatusUpdate(app.id, 'Rejected')} disabled={app.status !== 'Pending Review'} style={{ marginLeft: '10px' }}>Reject</button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default LoanOfficerDashboard;
