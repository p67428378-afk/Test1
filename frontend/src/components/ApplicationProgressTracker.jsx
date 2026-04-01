import React from 'react';

function ApplicationProgressTracker() {
  return (
    <section className='bg-surface-container-low rounded-2xl p-8 relative overflow-hidden group'>
      <div className='relative z-10 flex flex-col md:flex-row justify-between gap-8'>
        <div className='space-y-4 max-w-md'>
          <div className='inline-flex items-center gap-2 px-3 py-1 bg-primary/5 text-primary rounded-full text-xs font-bold font-label tracking-wider uppercase'>
            Active Application
          </div>
          <h3 className='text-2xl font-bold font-headline text-on-surface'>Step 2 of 4: Financial Info</h3>
          <p className='text-on-surface-variant leading-relaxed'>Your application for the Vault Infinite card is in progress. Complete your income verification to move to step 3.</p>
          <div className='flex gap-4 pt-2'>
            <button className='bg-primary text-on-primary px-6 py-3 rounded-md font-bold text-sm shadow-lg hover:shadow-primary/20 transition-all active:scale-95'>Resume Application</button>
          </div>
        </div>
        <div className='flex-1 max-w-sm flex flex-col justify-center space-y-6'>
          <div className='flex justify-between text-xs font-bold font-label text-on-surface-variant uppercase tracking-widest'>
            <span>Progress</span>
            <span>45%</span>
          </div>
          <div className='flex gap-2 h-3'>
            <div className='flex-1 bg-primary rounded-full'></div>
            <div className='flex-1 bg-primary/30 rounded-full relative overflow-hidden'>
              <div className='absolute inset-0 bg-primary/60 w-1/2'></div>
            </div>
            <div className='flex-1 bg-surface-container-high rounded-full'></div>
            <div className='flex-1 bg-surface-container-high rounded-full'></div>
          </div>
          <div className='flex justify-between items-center bg-surface-container-lowest p-4 rounded-xl'>
            <div className='flex items-center gap-3'>
              <span className='material-symbols-outlined text-primary-container'>description</span>
              <span className='text-sm font-semibold'>Income_Verify_2024.pdf</span>
            </div>
            <span className='material-symbols-outlined text-green-600'>check_circle</span>
          </div>
        </div>
      </div>
      <div className='absolute -right-20 -top-20 w-80 h-80 bg-primary-container/5 rounded-full blur-3xl'></div>
    </section>
  );
}

export default ApplicationProgressTracker;
