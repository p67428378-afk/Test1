
import React from 'react';
import CancellationForm from './components/CancellationForm';

function App() {
  return (
    <div className='min-h-screen bg-gray-100 flex items-center justify-center'>
      <div className='max-w-md w-full p-6 bg-white rounded-lg shadow-md'>
        <h1 className='text-2xl font-bold text-center text-gray-800 mb-4'>
          Scheduled Transfer Cancellation
        </h1>
        <CancellationForm />
      </div>
    </div>
  );
}

export default App;
