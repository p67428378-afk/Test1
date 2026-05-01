import React from 'react';

const Footer = () => {
  return (
    <footer className='bg-gray-100 p-4 mt-8'>
      <div className='container mx-auto text-center text-gray-600 text-sm'>
        <p>&copy; 2024 Vehicle Insurance Premium Calculator. All Rights Reserved.</p>
        <p className='mt-2'>
          Disclaimer: All calculations are editorial estimates. Please consult with an agent for exact figures.
        </p>
      </div>
    </footer>
  );
};

export default Footer;
