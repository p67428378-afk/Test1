import React, { useState } from 'react';

const ApplicantForm = () => {
  const [formData, setFormData] = useState({
    full_name: '',
    email: '',
    phone_number: '',
    date_of_birth: '',
    address: '',
    income: '',
    employment_status: '',
    existing_liabilities: '',
    bank_name: '',
    account_number: '',
    ifsc_swift_code: '',
    loan_amount: '',
    tenure_months: '',
    agreed_terms: false,
    credit_check_consent: false,
  });
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage('');
    setError('');

    try {
      const response = await fetch(`${process.env.REACT_APP_API_BASE_URL}/api/apply`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        setMessage(data.message);
        setFormData({
          full_name: '',
          email: '',
          phone_number: '',
          date_of_birth: '',
          address: '',
          income: '',
          employment_status: '',
          existing_liabilities: '',
          bank_name: '',
          account_number: '',
          ifsc_swift_code: '',
          loan_amount: '',
          tenure_months: '',
          agreed_terms: false,
          credit_check_consent: false,
        });
      } else {
        setError(data.error || 'An error occurred during submission.');
      }
    } catch (err) {
      setError('Network error or server is unreachable.');
      console.error('Submission error:', err);
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', maxWidth: '500px', margin: 'auto', gap: '10px' }}>
      <h3>Personal Information</h3>
      <input type="text" name="full_name" value={formData.full_name} onChange={handleChange} placeholder="Full Name" required />
      <input type="email" name="email" value={formData.email} onChange={handleChange} placeholder="Email" required />
      <input type="text" name="phone_number" value={formData.phone_number} onChange={handleChange} placeholder="Phone Number" required />
      <input type="date" name="date_of_birth" value={formData.date_of_birth} onChange={handleChange} placeholder="Date of Birth" required />
      <input type="text" name="address" value={formData.address} onChange={handleChange} placeholder="Address" required />

      <h3>Financial Information</h3>
      <input type="number" name="income" value={formData.income} onChange={handleChange} placeholder="Annual Income" required />
      <input type="text" name="employment_status" value={formData.employment_status} onChange={handleChange} placeholder="Employment Status" required />
      <input type="number" name="existing_liabilities" value={formData.existing_liabilities} onChange={handleChange} placeholder="Existing Liabilities" required />

      <h3>Bank Details</h3>
      <input type="text" name="bank_name" value={formData.bank_name} onChange={handleChange} placeholder="Bank Name" required />
      <input type="text" name="account_number" value={formData.account_number} onChange={handleChange} placeholder="Account Number" required />
      <input type="text" name="ifsc_swift_code" value={formData.ifsc_swift_code} onChange={handleChange} placeholder="IFSC/SWIFT Code" required />

      <h3>Loan Information</h3>
      <input type="number" name="loan_amount" value={formData.loan_amount} onChange={handleChange} placeholder="Loan Amount" required />
      <input type="number" name="tenure_months" value={formData.tenure_months} onChange={handleChange} placeholder="Tenure (Months)" required />

      <h3>Legal Agreements</h3>
      <label>
        <input type="checkbox" name="agreed_terms" checked={formData.agreed_terms} onChange={handleChange} required />
        I agree to the terms and conditions.
      </label>
      <label>
        <input type="checkbox" name="credit_check_consent" checked={formData.credit_check_consent} onChange={handleChange} required />
        I consent to a credit check.
      </label>

      <button type="submit" style={{ padding: '10px', marginTop: '20px' }}>Submit Application</button>

      {message && <p style={{ color: 'green' }}>{message}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </form>
  );
};

export default ApplicantForm;
