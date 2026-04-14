import React from 'react';

const LoanCenter = () => {
  return (
    <div className='grid grid-cols-2 gap-8'>
      <div className='bg-surface-container-low rounded-xl p-8 flex flex-col justify-between'>
        <div>
          <h3 className='text-sm font-bold text-on-surface-variant uppercase tracking-[0.2em] mb-6'>Loan Center</h3>
          <p className='text-on-surface-variant mb-6 text-sm'>Expand your horizons with our institutional-grade lending solutions.</p>
          <div className='flex flex-col gap-3'>
            <label className='flex items-center gap-4 p-3 rounded-lg border border-outline-variant/20 bg-surface-container-lowest cursor-pointer hover:border-primary/40 transition-colors'>
              <span className='material-symbols-outlined text-primary'>directions_car</span>
              <span className='text-sm font-semibold'>Auto Loan</span>
              <span className='ml-auto text-xs font-bold text-tertiary'>From 3.2%</span>
            </label>
            <label className='flex items-center gap-4 p-3 rounded-lg border border-outline-variant/20 bg-surface-container-lowest cursor-pointer hover:border-primary/40 transition-colors'>
              <span className='material-symbols-outlined text-primary'>home</span>
              <span className='text-sm font-semibold'>Home Mortgage</span>
              <span className='ml-auto text-xs font-bold text-tertiary'>From 5.8%</span>
            </label>
          </div>
        </div>
        <button className='mt-8 vault-gradient text-white py-4 rounded-lg font-bold hover:shadow-lg transition-all uppercase tracking-widest text-xs'>Apply for a Loan</button>
      </div>
      <div className='bg-surface-container-lowest rounded-xl p-8 border border-outline-variant/10'>
        <h3 className='text-sm font-bold text-on-surface-variant uppercase tracking-[0.2em] mb-6'>Application Status</h3>
        <div className='space-y-6'>
          <div className='relative pl-8 pb-8 border-l-2 border-primary/20'>
            <div className='absolute -left-[9px] top-0 w-4 h-4 rounded-full bg-primary border-4 border-surface-container-lowest'></div>
            <p className='text-xs font-bold text-primary uppercase tracking-tighter mb-1'>Mortgage Refinance</p>
            <p className='text-sm font-semibold'>Underwriting Review</p>
            <p className='text-[10px] text-on-surface-variant mt-2'>Submitted Dec 14 • ID: #LN-9921</p>
          </div>
          <div className='relative pl-8'>
            <div className='absolute -left-[9px] top-0 w-4 h-4 rounded-full bg-slate-300 border-4 border-surface-container-lowest'></div>
            <p className='text-xs font-bold text-slate-400 uppercase tracking-tighter mb-1'>Personal Line of Credit</p>
            <p className='text-sm font-semibold text-slate-400'>Final Verification</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoanCenter;
