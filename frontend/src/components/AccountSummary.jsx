import React from 'react';

const AccountSummary = () => {
  return (
    <div className='bg-surface-container-lowest rounded-xl p-8 shadow-[0_32px_32px_-4px_rgba(0,29,68,0.06)] relative overflow-hidden'>
      <div className='absolute top-0 right-0 p-8 opacity-5'>
        <span className='material-symbols-outlined text-9xl'>account_balance_wallet</span>
      </div>
      <h3 className='text-sm font-bold text-on-surface-variant uppercase tracking-[0.2em] mb-8'>Asset Allocation</h3>
      <div className='space-y-6'>
        <div className='flex items-center justify-between p-4 rounded-lg bg-surface-container-low hover:bg-surface-container-high transition-colors group'>
          <div className='flex items-center gap-6'>
            <div className='w-12 h-12 rounded-lg bg-primary/5 flex items-center justify-center text-primary'>
              <span className='material-symbols-outlined'>shield</span>
            </div>
            <div>
              <p className='font-bold text-lg'>Elite Checking</p>
              <p className='text-xs text-on-surface-variant tabular-nums'>Account •••• 8829</p>
            </div>
          </div>
          <div className='text-right'>
            <p className='text-xl font-extrabold tabular-nums'>$142,500.00</p>
            <p className='text-xs text-on-surface-variant'>Available: $141,920.00</p>
          </div>
        </div>
        <div className='flex items-center justify-between p-4 rounded-lg bg-surface-container-low hover:bg-surface-container-high transition-colors group'>
          <div className='flex items-center gap-6'>
            <div className='w-12 h-12 rounded-lg bg-tertiary/5 flex items-center justify-center text-tertiary'>
              <span className='material-symbols-outlined'>savings</span>
            </div>
            <div>
              <p className='font-bold text-lg'>High-Yield Savings</p>
              <p className='text-xs text-on-surface-variant tabular-nums'>Account •••• 4401</p>
            </div>
          </div>
          <div className='text-right'>
            <p className='text-xl font-extrabold tabular-nums'>$2,340,401.42</p>
            <p className='text-xs text-on-surface-variant'>APY: 4.85%</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default AccountSummary;
