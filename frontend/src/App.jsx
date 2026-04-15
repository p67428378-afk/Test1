import React from 'react';
import Header from './components/Header';
import SideNav from './components/SideNav';
import Calculator from './components/Calculator';

function App() {
  return (
    <div className='bg-background text-on-background font-body min-h-screen'>
      <Header />
      <SideNav />
      <main className='ml-64 pt-20 min-h-screen'>
        <div className='w-full h-1 bg-surface-container relative'>
          <div className='absolute left-0 top-0 h-full w-[40%] bg-gradient-to-r from-tertiary to-primary transition-all duration-500'></div>
        </div>
        <div className='px-12 py-12 max-w-[1600px] mx-auto'>
          <Calculator />
        </div>
      </main>
      <div className='fixed -bottom-32 -left-32 w-96 h-96 bg-secondary-fixed/20 blur-[120px] rounded-full -z-10'></div>
      <div className='fixed top-1/2 right-10 w-64 h-64 bg-primary-fixed/10 blur-[100px] rounded-full -z-10'></div>
    </div>
  );
}

export default App;
