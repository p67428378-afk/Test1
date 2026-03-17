import React, { useState } from 'react';

function ApplicantForm() {
  const [formData, setFormData] = useState({
    full_name: '',
    contact_info: '',
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
    terms_agreed: false,
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
      const response = await fetch(`${process.env.REACT_APP_API_BASE_URL}/applications`, {
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
          contact_info: '',
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
          terms_agreed: false,
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
    <div style={{ maxWidth: '600px', margin: 'auto', padding: '20px', border: '1px solid #ccc', borderRadius: '8px' }}>
      <h2>Loan Application Form</h2>
      <form onSubmit={handleSubmit}>
        <h3>Personal Information</h3>
        <label>
          Full Name:
          <input type="text" name="full_name" value={formData.full_name} onChange={handleChange} required />
        </label>
        <label>
          Contact Info:
          <input type="text" name="contact_info" value={formData.contact_info} onChange={handleChange} required />
        </label>
        <label>
          Date of Birth:
          <input type="date" name="date_of_birth" value={formData.date_of_birth} onChange={handleChange} required />
        </label>
        <label>
          Address:
          <input type="text" name="address" value={formData.address} onChange={handleChange} required />
        </label>

        <h3>Financial Information</h3>
        <label>
          Income:
          <input type="number" name="income" value={formData.income} onChange={handleChange} required />
        </label>
        <label>
          Employment Status:
          <input type="text" name="employment_status" value={formData.employment_status} onChange={handleChange} required />
        </label>
        <label>
          Existing Liabilities:
          <input type="number" name="existing_liabilities" value={formData.existing_liabilities} onChange={handleChange} />
        </label>

        <h3>Bank Details</h3>
        <label>
          Bank Name:
          <input type="text" name="bank_name" value={formData.bank_name} onChange={handleChange} required />
        </label>
        <label>
          Account Number:
          <input type="text" name="account_number" value={formData.account_number} onChange={handleChange} required />
        </label>
        <label>
          IFSC/SWIFT Code:
          <input type="text" name="ifsc_swift_code" value={formData.ifsc_swift_code} onChange={handleChange} required />
        </label>

        <h3>Loan Information</h3>
        <label>
          Loan Amount:
          <input type="number" name="loan_amount" value={formData.loan_amount} onChange={handleChange} required />
        </label>
        <label>
          Tenure (Months):
          <input type="number" name="tenure_months" value={formData.tenure_months} onChange={handleChange} required />
        </label>

        <h3>Legal Information</h3>
        <label>
          <input type="checkbox" name="terms_agreed" checked={formData.terms_agreed} onChange={handleChange} required />
          I agree to the Terms and Conditions.
        </label>
        <label>
          <input type="checkbox" name="credit_check_consent" checked={formData.credit_check_consent} onChange={handleChange} required />
          I consent to a credit check.
        </label>

        <button type="submit" style={{ marginTop: '20px', padding: '10px 20px', backgroundColor: '#007bff', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}>
          Submit Application
        </button>
      </form>

      {message && <p style={{ color: 'green' }}>{message}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
}

export default ApplicantForm;
