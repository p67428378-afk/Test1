import React from 'react';
import Header from './components/Header';
import Balance from './components/Balance';
import AccountSummary from './components/AccountSummary';
import LoanCenter from './components/LoanCenter';
import Deposit from './components/Deposit';
import TransactionLedger from './components/TransactionLedger';

function App() {
  return (
    <div className='bg-surface text-on-surface min-h-screen'>
      <Header />
      <main className='pt-24 px-16 pb-16 max-w-[1920px] mx-auto'>
        <Balance />
        <div className='grid grid-cols-12 gap-8'>
          <div className='col-span-8 flex flex-col gap-8'>
            <AccountSummary />
            <LoanCenter />
          </div>
          <div className='col-span-4 flex flex-col gap-8'>
            <Deposit />
            <TransactionLedger />
          </div>
        </div>
      </main>
      <div className='fixed bottom-0 left-0 w-full h-1 bg-gradient-to-r from-primary via-primary-container to-primary opacity-20'></div>
    </div>
  );
}

export default App;
