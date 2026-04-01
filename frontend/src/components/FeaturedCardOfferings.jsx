import React from 'react';

function FeaturedCardOfferings() {
  return (
    <section className='space-y-6'>
      <div className='flex justify-between items-end'>
        <div className='space-y-1'>
          <h3 className='text-2xl font-bold font-headline text-on-surface'>Precision Tiers</h3>
          <p className='text-on-surface-variant text-sm'>Select the instrument that matches your lifestyle.</p>
        </div>
        <button className='text-primary font-bold text-sm flex items-center gap-1 hover:gap-2 transition-all'>View All Offers <span className='material-symbols-outlined text-sm'>arrow_forward</span></button>
      </div>
      <div className='flex gap-6 overflow-x-auto no-scrollbar pb-4 snap-x'>
        {/* Vault Infinite */}
        <div className='min-w-[320px] md:min-w-[380px] snap-center bg-gradient-to-br from-primary to-primary-container p-8 rounded-3xl text-on-primary flex flex-col justify-between h-56 shadow-2xl shadow-primary/20 relative overflow-hidden'>
          <div className='relative z-10'>
            <h4 className='text-xl font-bold font-headline tracking-tight'>Vault Infinite</h4>
            <p className='text-on-primary-container text-xs font-bold font-label uppercase tracking-widest mt-1'>Elite Collection</p>
          </div>
          <div className='relative z-10 flex justify-between items-end'>
            <div className='space-y-1'>
              <p className='text-2xl font-bold'>4.25%</p>
              <p className='text-[10px] text-on-primary-container font-bold uppercase tracking-tighter'>Unlimited Cashback</p>
            </div>
            <span className='material-symbols-outlined text-4xl opacity-50'>contactless</span>
          </div>
          <div className='absolute right-[-10%] bottom-[-10%] w-32 h-32 bg-white/10 rounded-full blur-2xl'></div>
        </div>
        {/* Obsidian Credit */}
        <div className='min-w-[320px] md:min-w-[380px] snap-center bg-surface-container-lowest p-8 rounded-3xl border border-outline-variant/20 flex flex-col justify-between h-56 shadow-sm relative overflow-hidden group'>
          <div className='relative z-10'>
            <h4 className='text-xl font-bold font-headline tracking-tight text-primary'>Obsidian Credit</h4>
            <p className='text-on-surface-variant text-xs font-bold font-label uppercase tracking-widest mt-1'>Modern Everyday</p>
          </div>
          <div className='relative z-10 flex justify-between items-end'>
            <div className='space-y-1'>
              <p className='text-2xl font-bold text-primary'>0%</p>
              <p className='text-[10px] text-on-surface-variant font-bold uppercase tracking-tighter'>Intro APR for 18 mo.</p>
            </div>
            <span className='material-symbols-outlined text-4xl text-primary/20 group-hover:text-primary/40 transition-colors'>diamond</span>
          </div>
          <div className='absolute inset-0 bg-gradient-to-br from-transparent to-surface-container-low opacity-50'></div>
        </div>
        {/* Commercial Prime */}
        <div className='min-w-[320px] md:min-w-[380px] snap-center bg-surface-container-lowest p-8 rounded-3xl border border-outline-variant/20 flex flex-col justify-between h-56 shadow-sm relative overflow-hidden'>
          <div className='relative z-10'>
            <h4 className='text-xl font-bold font-headline tracking-tight text-primary'>Commercial Prime</h4>
            <p className='text-on-surface-variant text-xs font-bold font-label uppercase tracking-widest mt-1'>Corporate Engine</p>
          </div>
          <div className='relative z-10 flex justify-between items-end'>
            <div className='space-y-1'>
              <p className='text-2xl font-bold text-primary'>$0</p>
              <p className='text-[10px] text-on-surface-variant font-bold uppercase tracking-tighter'>Annual Fee for Business</p>
            </div>
            <span className='material-symbols-outlined text-4xl text-primary/20'>business_center</span>
          </div>
        </div>
      </div>
    </section>
  );
}

export default FeaturedCardOfferings;
