import React, { useState } from 'react';
import axios from 'axios';

const LoanApplicationForm = () => {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    phone_number: '',
    date_of_birth: '',
    address: '',
    loan_amount: '',
    loan_tenure: '',
    financial_details: '',
    bank_details: '',
    legal_consent: false,
  });
  const [message, setMessage] = useState({ type: '', text: '' });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage({ type: '', text: '' });

    try {
      const api_url = process.env.REACT_APP_API_URL || 'http://localhost:5000';
      const response = await axios.post(`${api_url}/applications`, formData);
      setMessage({ type: 'success', text: response.data.message });
      setFormData({
        first_name: '',
        last_name: '',
        email: '',
        phone_number: '',
        date_of_birth: '',
        address: '',
        loan_amount: '',
        loan_tenure: '',
        financial_details: '',
        bank_details: '',
        legal_consent: false,
      });
    } catch (error) {
      console.error('Error submitting application:', error);
      setMessage({ type: 'error', text: error.response?.data?.error || 'Failed to submit application.' });
    }
  };

  return (
    <main>
      <h2>Apply for a Personal Loan</h2>
      <form onSubmit={handleSubmit}>
        <h3>Personal Information</h3>
        <div>
          <label htmlFor="first_name">First Name:</label>
          <input type="text" id="first_name" name="first_name" value={formData.first_name} onChange={handleChange} required />
        </div>
        <div>
          <label htmlFor="last_name">Last Name:</label>
          <input type="text" id="last_name" name="last_name" value={formData.last_name} onChange={handleChange} required />
        </div>
        <div>
          <label htmlFor="email">Email:</label>
          <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} required />
        </div>
        <div>
          <label htmlFor="phone_number">Phone Number:</label>
          <input type="text" id="phone_number" name="phone_number" value={formData.phone_number} onChange={handleChange} />
        </div>
        <div>
          <label htmlFor="date_of_birth">Date of Birth:</label>
          <input type="date" id="date_of_birth" name="date_of_birth" value={formData.date_of_birth} onChange={handleChange} />
        </div>
        <div>
          <label htmlFor="address">Address:</label>
          <textarea id="address" name="address" value={formData.address} onChange={handleChange}></textarea>
        </div>

        <h3>Loan Details</h3>
        <div>
          <label htmlFor="loan_amount">Loan Amount ($):</label>
          <input type="number" id="loan_amount" name="loan_amount" value={formData.loan_amount} onChange={handleChange} required min="1" />
        </div>
        <div>
          <label htmlFor="loan_tenure">Loan Tenure (months):</label>
          <input type="number" id="loan_tenure" name="loan_tenure" value={formData.loan_tenure} onChange={handleChange} required min="6" max="120" />
        </div>

        <h3>Financial Information</h3>
        <div>
          <label htmlFor="financial_details">Income, Employment Status, Existing Liabilities:</label>
          <textarea id="financial_details" name="financial_details" value={formData.financial_details} onChange={handleChange} placeholder="e.g., Annual Income: $60,000, Employment: Full-time, Existing Loan: $10,000"></textarea>
        </div>

        <h3>Bank Details</h3>
        <div>
          <label htmlFor="bank_details">Bank Name, Account Number, IFSC/SWIFT:</label>
          <textarea id="bank_details" name="bank_details" value={formData.bank_details} onChange={handleChange} placeholder="e.g., Bank of America, 1234567890, BOFAUS3N"></textarea>
        </div>

        <h3>Legal Information</h3>
        <div>
          <input type="checkbox" id="legal_consent" name="legal_consent" checked={formData.legal_consent} onChange={handleChange} required />
          <label htmlFor="legal_consent">I agree to the Terms and Conditions and provide consent for a credit check.</label>
        </div>

        <button type="submit">Submit Application</button>
      </form>

      {message.text && (
        <div className={`message ${message.type}`}>
          {message.text}
        </div>
      )}
    </main>
  );
};

export default LoanApplicationForm;
