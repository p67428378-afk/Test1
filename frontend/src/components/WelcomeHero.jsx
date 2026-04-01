import React from 'react';

function WelcomeHero() {
  return (
    <section className='grid grid-cols-1 md:grid-cols-12 gap-8 items-end'>
      <div className='md:col-span-8 space-y-2'>
        <p className='text-on-surface-variant font-medium tracking-wide font-label uppercase text-sm'>Welcome Back</p>
        <h2 className='text-4xl md:text-5xl font-extrabold font-headline text-primary tracking-tight leading-tight'>
          Your financial future, <br/><span className='text-on-primary-container'>precisely engineered.</span>
        </h2>
      </div>
      <div className='md:col-span-4 flex justify-end'>
        <div className='bg-surface-container-low p-4 rounded-xl flex items-center gap-3 border border-outline-variant/10'>
          <div className='w-2 h-2 rounded-full bg-green-500 animate-pulse'></div>
          <span className='text-sm font-semibold text-on-surface'>Systems Operational</span>
        </div>
      </div>
    </section>
  );
}

export default WelcomeHero;
