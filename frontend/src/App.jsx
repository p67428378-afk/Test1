import React from 'react';
import Sidebar from './components/Sidebar';
import Header from './components/Header';
import Calculator from './components/Calculator';

function App() {
  return (
    <div className='bg-surface font-body text-on-surface antialiased'>
      <Sidebar />
      <main className='ml-64 min-h-screen'>
        <Header />
        <div className='p-12 space-y-12 max-w-[1600px] mx-auto'>
          <Calculator />
        </div>
      </main>
    </div>
  );
}

export default App;
