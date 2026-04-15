import React from 'react';

const SideNav = () => {
  return (
    <aside className='fixed left-0 top-20 h-[calc(100vh-80px)] w-64 bg-slate-100 dark:bg-slate-800/50 flex flex-col pt-8 font-headline text-sm font-semibold tracking-wide'>
      <div className='px-8 mb-10'>
        <div className='text-lg font-black text-blue-900 dark:text-blue-50'>Quote Builder</div>
        <div className='text-xs text-on-surface-variant/60 font-medium'>ID: #8829-001</div>
      </div>
      <div className='flex flex-col gap-1'>
        <div className='flex items-center gap-3 text-slate-500 dark:text-slate-400 pl-10 py-3 hover:bg-slate-200/50 dark:hover:bg-slate-700/50 transition-all cursor-pointer'>
          <span className='material-symbols-outlined'>dashboard</span>
          <span>Overview</span>
        </div>
        <div className='flex items-center gap-3 bg-white dark:bg-blue-900/30 text-blue-900 dark:text-blue-100 rounded-l-full ml-4 pl-6 py-3 Active: translate-x-1 transition-transform'>
          <span className='material-symbols-outlined' style={{ fontVariationSettings: '\'FILL\' 1' }}>calculate</span>
          <span>Calculator</span>
        </div>
        <div className='flex items-center gap-3 text-slate-500 dark:text-slate-400 pl-10 py-3 hover:bg-slate-200/50 dark:hover:bg-slate-700/50 transition-all cursor-pointer'>
          <span className='material-symbols-outlined'>directions_car</span>
          <span>Vehicle Details</span>
        </div>
        <div className='flex items-center gap-3 text-slate-500 dark:text-slate-400 pl-10 py-3 hover:bg-slate-200/50 dark:hover:bg-slate-700/50 transition-all cursor-pointer'>
          <span className='material-symbols-outlined'>security</span>
          <span>Coverage</span>
        </div>
        <div className='flex items-center gap-3 text-slate-500 dark:text-slate-400 pl-10 py-3 hover:bg-slate-200/50 dark:hover:bg-slate-700/50 transition-all cursor-pointer'>
          <span className='material-symbols-outlined'>verified</span>
          <span>Finalize</span>
        </div>
      </div>
    </aside>
  );
};

export default SideNav;
