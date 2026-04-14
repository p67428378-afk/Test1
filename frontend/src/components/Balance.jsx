import React from 'react';

const Balance = () => {
  return (
    <section className='mb-12 flex justify-between items-end'>
      <div>
        <h1 className='text-on-surface-variant font-headline text-lg font-medium mb-1 uppercase tracking-widest'>Institutional Portfolio</h1>
        <div className='flex items-baseline gap-4'>
          <span className='text-6xl font-headline font-extrabold tracking-tight tabular-nums'>$2,482,901.42</span>
          <span className='text-tertiary font-bold flex items-center gap-1'>
            <span className='material-symbols-outlined text-sm'>trending_up</span>
            2.4%
          </span>
        </div>
        <div className='mt-4 flex items-center gap-3 text-on-surface-variant'>
          <span className='material-symbols-outlined text-sm'>sync</span>
          <span className='text-xs font-medium uppercase tracking-wider'>Last updated: 1 minute ago</span>
        </div>
      </div>
      <div className='flex gap-4'>
        <button className='vault-gradient text-white px-8 py-3 rounded-lg font-bold shadow-lg hover:brightness-110 transition-all flex items-center gap-2'>
          <span className='material-symbols-outlined'>payments</span>
          Quick Transfer
        </button>
      </div>
    </section>
  );
};

export default Balance;
