
import React, { useState } from 'react';
import api from '../services/api';

const CancellationForm = () => {
  const [transferReferenceId, setTransferReferenceId] = useState('');
  const [accountNumber, setAccountNumber] = useState('');
  const [message, setMessage] = useState('');
  const [isError, setIsError] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage('');
    setIsError(false);

    try {
      const response = await api.post('/transfers/cancel', {
        transferReferenceId,
        accountNumber,
      });
      setMessage(`Status: ${response.data.status}, Reason: ${response.data.reason}`);
    } catch (error) {
      setIsError(true);
      if (error.response) {
        setMessage(`Error: ${error.response.data.detail}`);
      } else {
        setMessage('An unexpected error occurred.');
      }
    }
  };

  return (
    <form onSubmit={handleSubmit} className='space-y-4'>
      <div>
        <label htmlFor='transferReferenceId' className='block text-sm font-medium text-gray-700'>
          Transfer Reference ID
        </label>
        <input
          type='text'
          id='transferReferenceId'
          value={transferReferenceId}
          onChange={(e) => setTransferReferenceId(e.target.value)}
          className='mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
          required
        />
      </div>
      <div>
        <label htmlFor='accountNumber' className='block text-sm font-medium text-gray-700'>
          Account Number
        </label>
        <input
          type='text'
          id='accountNumber'
          value={accountNumber}
          onChange={(e) => setAccountNumber(e.target.value)}
          className='mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm'
          required
        />
      </div>
      <button
        type='submit'
        className='w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500'
      >
        Cancel Transfer
      </button>
      {message && (
        <div className={`mt-4 text-center p-2 rounded-md ${isError ? 'bg-red-100 text-red-700' : 'bg-green-100 text-green-700'}`}>
          {message}
        </div>
      )}
    </form>
  );
};

export default CancellationForm;
