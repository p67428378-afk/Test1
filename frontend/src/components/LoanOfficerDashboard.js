import React, { useState, useEffect } from 'react';
import axios from 'axios';

const LoanOfficerDashboard = () => {
  const [applications, setApplications] = useState([]);
  const [message, setMessage] = useState({ type: '', text: '' });
  const [officerId, setOfficerId] = useState(1); // Hardcoded for demonstration
  const [reviewComments, setReviewComments] = useState({});

  const api_url = process.env.REACT_APP_API_URL || 'http://localhost:5000';

  useEffect(() => {
    fetchApplications();
  }, []);

  const fetchApplications = async () => {
    try {
      const response = await axios.get(`${api_url}/applications`);
      setApplications(response.data);
    } catch (error) {
      console.error('Error fetching applications:', error);
      setMessage({ type: 'error', text: 'Failed to fetch applications.' });
    }
  };

  const handleStatusUpdate = async (applicationId, decision) => {
    try {
      const response = await axios.put(`${api_url}/applications/${applicationId}/status`, {
        officer_id: officerId,
        decision: decision,
        comments: reviewComments[applicationId] || '',
      });
      setMessage({ type: 'success', text: response.data.message });
      fetchApplications(); // Refresh the list
      setReviewComments(prev => ({ ...prev, [applicationId]: '' })); // Clear comments
    } catch (error) {
      console.error(`Error updating application ${applicationId} status:`, error);
      setMessage({ type: 'error', text: error.response?.data?.error || 'Failed to update application status.' });
    }
  };

  const handleCommentChange = (applicationId, comment) => {
    setReviewComments(prev => ({ ...prev, [applicationId]: comment }));
  };

  return (
    <main>
      <h2>Loan Officer Dashboard</h2>
      {message.text && (
        <div className={`message ${message.type}`}>
          {message.text}
        </div>
      )}
      <div className="dashboard-container">
        {applications.length === 0 ? (
          <p>No loan applications to review.</p>
        ) : (
          applications.map((app) => (
            <div key={app.id} className="application-card">
              <h3>Application #{app.id} - Status: <span className={`status-${app.status.toLowerCase()}`}>{app.status}</span></h3>
              <p><strong>Applicant:</strong> {app.applicant?.first_name} {app.applicant?.last_name} ({app.applicant?.email})</p>
              <p><strong>Loan Amount:</strong> ${app.loan_amount}</p>
              <p><strong>Loan Tenure:</strong> {app.loan_tenure} months</p>
              <p><strong>Application Date:</strong> {new Date(app.application_date).toLocaleDateString()}</p>
              <p><strong>Financial Details:</strong> {app.financial_details}</p>
              <p><strong>Bank Details:</strong> {app.bank_details}</p>
              <p><strong>Legal Consent:</strong> {app.legal_consent ? 'Yes' : 'No'}</p>
              {app.status === 'Pending' && (
                <div className="application-actions">
                  <textarea
                    placeholder="Add review comments..."
                    value={reviewComments[app.id] || ''}
                    onChange={(e) => handleCommentChange(app.id, e.target.value)}
                  ></textarea>
                  <button className="approve-btn" onClick={() => handleStatusUpdate(app.id, 'Approved')}>Approve</button>
                  <button className="reject-btn" onClick={() => handleStatusUpdate(app.id, 'Rejected')}>Reject</button>
                </div>
              )}
            </div>
          ))
        )}
      </div>
    </main>
  );
};

export default LoanOfficerDashboard;
