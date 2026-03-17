import React, { useState } from 'react';
import './LoanApplicationForm.css'; // Import the CSS file

const LoanApplicationForm = () => {
    const [formData, setFormData] = useState({
        applicant: {
            first_name: '',
            last_name: '',
            date_of_birth: '',
            ssn: '',
            email: '',
            phone_number: '',
            address: '',
        },
        employment: {
            company_name: '',
            company_address: '',
            job_title: '',
            income: '',
        },
        bank_account: {
            account_number: '',
            aba_routing_number: '',
        },
        loan_details: {
            loan_purpose: '',
            loan_amount: '',
            loan_period_months: '',
        },
        legal_declaration: {
            citizenship_status: '',
            has_pending_cases: false,
        },
    });

    const [errors, setErrors] = useState({});
    const [submissionStatus, setSubmissionStatus] = useState(null);

    const validate = () => {
        let newErrors = {};
        // Basic validation examples - expand as needed
        if (!formData.applicant.first_name) newErrors.first_name = 'First Name is required';
        if (!formData.applicant.last_name) newErrors.last_name = 'Last Name is required';
        if (!formData.applicant.date_of_birth) newErrors.date_of_birth = 'Date of Birth is required';
        if (!formData.applicant.ssn) newErrors.ssn = 'SSN is required';
        if (!/^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/.test(formData.applicant.email)) newErrors.email = 'Valid Email is required';
        if (!formData.applicant.phone_number) newErrors.phone_number = 'Phone Number is required';
        if (!formData.applicant.address) newErrors.address = 'Address is required';

        if (!formData.employment.company_name) newErrors.company_name = 'Company Name is required';
        if (!formData.employment.income || isNaN(formData.employment.income) || parseFloat(formData.employment.income) <= 0) newErrors.income = 'Valid Income is required';

        if (!formData.bank_account.account_number) newErrors.account_number = 'Account Number is required';
        if (!/^[0-9]{9}$/.test(formData.bank_account.aba_routing_number)) newErrors.aba_routing_number = 'Valid ABA Routing Number (9 digits) is required';

        if (!formData.loan_details.loan_purpose) newErrors.loan_purpose = 'Loan Purpose is required';
        if (!formData.loan_details.loan_amount || isNaN(formData.loan_details.loan_amount) || parseFloat(formData.loan_details.loan_amount) <= 0) newErrors.loan_amount = 'Valid Loan Amount is required';
        if (!formData.loan_details.loan_period_months || isNaN(formData.loan_details.loan_period_months) || parseInt(formData.loan_details.loan_period_months) <= 0) newErrors.loan_period_months = 'Valid Loan Period is required';

        if (!formData.legal_declaration.citizenship_status) newErrors.citizenship_status = 'Citizenship Status is required';

        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleChange = (e, section, field) => {
        const value = e.target.type === 'checkbox' ? e.target.checked : e.target.value;
        setFormData(prevData => ({
            ...prevData,
            [section]: {
                ...prevData[section],
                [field]: value,
            },
        }));
        // Clear error for the field as user types
        if (errors[field]) {
            setErrors(prevErrors => {
                const newErrors = { ...prevErrors };
                delete newErrors[field];
                return newErrors;
            });
        }
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setSubmissionStatus(null);

        if (!validate()) {
            setSubmissionStatus('error');
            return;
        }

        try {
            const apiUrl = process.env.REACT_APP_API_URL || 'http://localhost:8000';
            const response = await fetch(`${apiUrl}/applications/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    applicant: {
                        ...formData.applicant,
                        date_of_birth: formData.applicant.date_of_birth, // Ensure date is in YYYY-MM-DD
                    },
                    employment: {
                        ...formData.employment,
                        income: parseFloat(formData.employment.income),
                    },
                    bank_account: formData.bank_account,
                    loan_details: {
                        ...formData.loan_details,
                        loan_amount: parseFloat(formData.loan_details.loan_amount),
                        loan_period_months: parseInt(formData.loan_details.loan_period_months),
                    },
                    legal_declaration: formData.legal_declaration,
                }),
            });

            if (response.ok) {
                const result = await response.json();
                console.log('Application submitted successfully:', result);
                setSubmissionStatus('success');
                // Optionally reset form
                setFormData({
                    applicant: {
                        first_name: '',
                        last_name: '',
                        date_of_birth: '',
                        ssn: '',
                        email: '',
                        phone_number: '',
                        address: '',
                    },
                    employment: {
                        company_name: '',
                        company_address: '',
                        job_title: '',
                        income: '',
                    },
                    bank_account: {
                        account_number: '',
                        aba_routing_number: '',
                    },
                    loan_details: {
                        loan_purpose: '',
                        loan_amount: '',
                        loan_period_months: '',
                    },
                    legal_declaration: {
                        citizenship_status: '',
                        has_pending_cases: false,
                    },
                });
                setErrors({});
            } else {
                const errorData = await response.json();
                console.error('Error submitting application:', errorData);
                setSubmissionStatus('error');
                // Attempt to map backend errors to form fields if possible
                if (errorData.detail && Array.isArray(errorData.detail)) {
                    const backendErrors = {};
                    errorData.detail.forEach(err => {
                        if (err.loc && err.loc.length > 1) {
                            backendErrors[err.loc[err.loc.length - 1]] = err.msg;
                        }
                    });
                    setErrors(prevErrors => ({ ...prevErrors, ...backendErrors }));
                }
            }
        } catch (error) {
            console.error('Network or unexpected error:', error);
            setSubmissionStatus('error');
        }
    };

    return (
        <div className="loan-application-container">
            <h2>Personal Loan Application</h2>
            <form onSubmit={handleSubmit} className="loan-application-form">
                {/* Personal Information */}
                <fieldset>
                    <legend>Personal Information</legend>
                    <div className="form-group">
                        <label htmlFor="first_name">First Name:</label>
                        <input type="text" id="first_name" value={formData.applicant.first_name} onChange={(e) => handleChange(e, 'applicant', 'first_name')} className={errors.first_name ? 'input-error' : ''} />
                        {errors.first_name && <span className="error-message">{errors.first_name}</span>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="last_name">Last Name:</label>
                        <input type="text" id="last_name" value={formData.applicant.last_name} onChange={(e) => handleChange(e, 'applicant', 'last_name')} className={errors.last_name ? 'input-error' : ''} />
                        {errors.last_name && <span className="error-message">{errors.last_name}</span>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="date_of_birth">Date of Birth:</label>
                        <input type="date" id="date_of_birth" value={formData.applicant.date_of_birth} onChange={(e) => handleChange(e, 'applicant', 'date_of_birth')} className={errors.date_of_birth ? 'input-error' : ''} />
                        {errors.date_of_birth && <span className="error-message">{errors.date_of_birth}</span>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="ssn">SSN (XXX-XX-XXXX):</label>
                        <input type="text" id="ssn" value={formData.applicant.ssn} onChange={(e) => handleChange(e, 'applicant', 'ssn')} placeholder="XXX-XX-XXXX" className={errors.ssn ? 'input-error' : ''} />
                        {errors.ssn && <span className="error-message">{errors.ssn}</span>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="email">Email:</label>
                        <input type="email" id="email" value={formData.applicant.email} onChange={(e) => handleChange(e, 'applicant', 'email')} className={errors.email ? 'input-error' : ''} />
                        {errors.email && <span className="error-message">{errors.email}</span>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="phone_number">Phone Number:</label>
                        <input type="tel" id="phone_number" value={formData.applicant.phone_number} onChange={(e) => handleChange(e, 'applicant', 'phone_number')} className={errors.phone_number ? 'input-error' : ''} />
                        {errors.phone_number && <span className="error-message">{errors.phone_number}</span>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="address">Address:</label>
                        <input type="text" id="address" value={formData.applicant.address} onChange={(e) => handleChange(e, 'applicant', 'address')} className={errors.address ? 'input-error' : ''} />
                        {errors.address && <span className="error-message">{errors.address}</span>}
                    </div>
                </fieldset>

                {/* Employment Information */}
                <fieldset>
                    <legend>Employment Information</legend>
                    <div className="form-group">
                        <label htmlFor="company_name">Company Name:</label>
                        <input type="text" id="company_name" value={formData.employment.company_name} onChange={(e) => handleChange(e, 'employment', 'company_name')} className={errors.company_name ? 'input-error' : ''} />
                        {errors.company_name && <span className="error-message">{errors.company_name}</span>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="company_address">Company Address:</label>
                        <input type="text" id="company_address" value={formData.employment.company_address} onChange={(e) => handleChange(e, 'employment', 'company_address')} className={errors.company_address ? 'input-error' : ''} />
                        {errors.company_address && <span className="error-message">{errors.company_address}</span>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="job_title">Job Title:</label>
                        <input type="text" id="job_title" value={formData.employment.job_title} onChange={(e) => handleChange(e, 'employment', 'job_title')} className={errors.job_title ? 'input-error' : ''} />
                        {errors.job_title && <span className="error-message">{errors.job_title}</span>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="income">Annual Income:</label>
                        <input type="number" id="income" value={formData.employment.income} onChange={(e) => handleChange(e, 'employment', 'income')} className={errors.income ? 'input-error' : ''} />
                        {errors.income && <span className="error-message">{errors.income}</span>}
                    </div>
                </fieldset>

                {/* Bank Information */}
                <fieldset>
                    <legend>Bank Information</legend>
                    <div className="form-group">
                        <label htmlFor="account_number">Bank Account Number:</label>
                        <input type="text" id="account_number" value={formData.bank_account.account_number} onChange={(e) => handleChange(e, 'bank_account', 'account_number')} className={errors.account_number ? 'input-error' : ''} />
                        {errors.account_number && <span className="error-message">{errors.account_number}</span>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="aba_routing_number">ABA Routing Number:</label>
                        <input type="text" id="aba_routing_number" value={formData.bank_account.aba_routing_number} onChange={(e) => handleChange(e, 'bank_account', 'aba_routing_number')} placeholder="9 digits" className={errors.aba_routing_number ? 'input-error' : ''} />
                        {errors.aba_routing_number && <span className="error-message">{errors.aba_routing_number}</span>}
                    </div>
                </fieldset>

                {/* Loan Details */}
                <fieldset>
                    <legend>Loan Details</legend>
                    <div className="form-group">
                        <label htmlFor="loan_purpose">Loan Purpose:</label>
                        <input type="text" id="loan_purpose" value={formData.loan_details.loan_purpose} onChange={(e) => handleChange(e, 'loan_details', 'loan_purpose')} className={errors.loan_purpose ? 'input-error' : ''} />
                        {errors.loan_purpose && <span className="error-message">{errors.loan_purpose}</span>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="loan_amount">Loan Amount:</label>
                        <input type="number" id="loan_amount" value={formData.loan_details.loan_amount} onChange={(e) => handleChange(e, 'loan_details', 'loan_amount')} className={errors.loan_amount ? 'input-error' : ''} />
                        {errors.loan_amount && <span className="error-message">{errors.loan_amount}</span>}
                    </div>
                    <div className="form-group">
                        <label htmlFor="loan_period_months">Loan Period (Months):</label>
                        <input type="number" id="loan_period_months" value={formData.loan_details.loan_period_months} onChange={(e) => handleChange(e, 'loan_details', 'loan_period_months')} className={errors.loan_period_months ? 'input-error' : ''} />
                        {errors.loan_period_months && <span className="error-message">{errors.loan_period_months}</span>}
                    </div>
                </fieldset>

                {/* Legal Information */}
                <fieldset>
                    <legend>Legal Information</legend>
                    <div className="form-group">
                        <label htmlFor="citizenship_status">Citizenship Status:</label>
                        <input type="text" id="citizenship_status" value={formData.legal_declaration.citizenship_status} onChange={(e) => handleChange(e, 'legal_declaration', 'citizenship_status')} className={errors.citizenship_status ? 'input-error' : ''} />
                        {errors.citizenship_status && <span className="error-message">{errors.citizenship_status}</span>}
                    </div>
                    <div className="form-group checkbox-group">
                        <input type="checkbox" id="has_pending_cases" checked={formData.legal_declaration.has_pending_cases} onChange={(e) => handleChange(e, 'legal_declaration', 'has_pending_cases')} />
                        <label htmlFor="has_pending_cases">Do you have any pending legal cases?</label>
                    </div>
                </fieldset>

                <button type="submit" className="submit-button">Submit Application</button>

                {submissionStatus === 'success' && (
                    <p className="success-message">Loan application submitted successfully!</p>
                )}
                {submissionStatus === 'error' && (
                    <p className="error-message">Error submitting application. Please check your inputs.</p>
                )}
            </form>
        </div>
    );
};

export default LoanApplicationForm;
