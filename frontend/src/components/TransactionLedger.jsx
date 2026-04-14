import React from 'react';

const TransactionLedger = () => {
  return (
    <div className='bg-surface-container-lowest rounded-xl p-8 flex-1 shadow-[0_32px_32px_-4px_rgba(0,29,68,0.06)]'>
      <div className='flex justify-between items-center mb-8'>
        <h3 className='text-sm font-bold text-on-surface-variant uppercase tracking-[0.2em]'>Transaction Ledger</h3>
        <a className='text-xs font-bold text-primary hover:underline' href='#'>View All</a>
      </div>
      <div className='space-y-4'>
        {/* Transaction 1 */}
        <div className='flex items-center justify-between p-3 rounded-lg hover:bg-surface-container-low transition-all cursor-pointer'>
          <div className='flex items-center gap-4'>
            <div className='w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center'>
              <span className='material-symbols-outlined text-on-surface-variant'>shopping_bag</span>
            </div>
            <div>
              <p className='text-sm font-bold'>Harrods London</p>
              <p className='text-[10px] text-on-surface-variant uppercase font-medium'>Dec 18 • Luxury Retail</p>
            </div>
          </div>
          <p className='text-sm font-extrabold tabular-nums'>-$1,420.00</p>
        </div>
        {/* Transaction 2 */}
        <div className='flex items-center justify-between p-3 rounded-lg hover:bg-surface-container-low transition-all cursor-pointer'>
          <div className='flex items-center gap-4'>
            <div className='w-10 h-10 rounded-full bg-tertiary/10 flex items-center justify-center text-tertiary'>
              <span className='material-symbols-outlined'>account_balance</span>
            </div>
            <div>
              <p className='text-sm font-bold'>Dividends Credited</p>
              <p className='text-[10px] text-on-surface-variant uppercase font-medium'>Dec 17 • Investment</p>
            </div>
          </div>
          <p className='text-sm font-extrabold text-tertiary tabular-nums'>+$4,200.50</p>
        </div>
        {/* Transaction 3 */}
        <div className='flex items-center justify-between p-3 rounded-lg hover:bg-surface-container-low transition-all cursor-pointer'>
          <div className='flex items-center gap-4'>
            <div className='w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center'>
              <span className='material-symbols-outlined text-on-surface-variant'>restaurant</span>
            </div>
            <div>
              <p className='text-sm font-bold'>The Wolseley</p>
              <p className='text-[10px] text-on-surface-variant uppercase font-medium'>Dec 16 • Dining</p>
            </div>
          </div>
          <p className='text-sm font-extrabold tabular-nums'>-$284.10</p>
        </div>
        {/* Transaction 4 */}
        <div className='flex items-center justify-between p-3 rounded-lg hover:bg-surface-container-low transition-all cursor-pointer'>
          <div className='flex items-center gap-4'>
            <div className='w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center'>
              <span className='material-symbols-outlined text-on-surface-variant'>flight</span>
            </div>
            <div>
              <p className='text-sm font-bold'>British Airways</p>
              <p className='text-[10px] text-on-surface-variant uppercase font-medium'>Dec 15 • Travel</p>
            </div>
          </div>
          <p className='text-sm font-extrabold tabular-nums'>-$8,402.00</p>
        </div>
        {/* Transaction 5 */}
        <div className='flex items-center justify-between p-3 rounded-lg hover:bg-surface-container-low transition-all cursor-pointer'>
          <div className='flex items-center gap-4'>
            <div className='w-10 h-10 rounded-full bg-slate-100 flex items-center justify-center text-primary'>
              <span className='material-symbols-outlined'>bolt</span>
            </div>
            <div>
              <p className='text-sm font-bold'>EDF Energy</p>
              <p className='text-[10px] text-on-surface-variant uppercase font-medium'>Dec 15 • Utilities</p>
            </div>
          </div>
          <p className='text-sm font-extrabold tabular-nums'>-$450.00</p>
        </div>
      </div>
      <div className='mt-12 p-4 rounded-lg bg-surface-container-low flex items-center gap-4'>
        <img alt='Relationship Manager' className='w-10 h-10 rounded-full object-cover grayscale' src='https://lh3.googleusercontent.com/aida-public/AB6AXuB9x6suxMLDOZf5semNuz-Ae5TEu0xHDjEueF9Pzh2NjuI-gnA0Hfu581j3T6BlRx4oNYTQEVD094Vy5R0yWnvvMadkHOA7eZqj5R4ES4Adr4O2qGBXWgDco-uPIrO6sl10DLNcsLT0nMZGUJ75ti8xO1pw3lFNquINfCgjQkHngfGzvXv4q_Qq9uIEqPH1eylnN9HoeknAfS2AMEo9y-pd59Iler6Sg-KfcHanzJqfhpQvJC4CRmkAQTmLq_8trurGN4yhd0HOQjY'/>
        <div>
          <p className='text-[10px] font-bold text-on-surface-variant uppercase tracking-widest'>Personal Advisor</p>
          <p className='text-xs font-semibold'>Sarah Jenkins is available</p>
        </div>
        <button className='ml-auto material-symbols-outlined text-primary'>chat</button>
      </div>
    </div>
  );
};

export default TransactionLedger;
