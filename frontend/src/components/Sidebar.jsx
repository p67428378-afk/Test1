import React from 'react';

const Sidebar = () => {
  return (
    <aside className='h-screen w-72 fixed left-0 top-0 flex flex-col bg-slate-100 dark:bg-slate-950 z-50'>
      <div className='flex flex-col gap-2 pt-8 pb-4 h-full bg-slate-50 dark:bg-slate-900'>
        <div className='px-8 mb-10'>
          <h1 className='font-black text-lg text-slate-900 dark:text-white uppercase tracking-widest font-headline'>THE LEDGER</h1>
          <p className='text-[10px] text-on-surface-variant tracking-[0.2em] font-medium uppercase mt-1'>Society Management</p>
        </div>
        <nav className='flex flex-col flex-1'>
          <a className='flex items-center gap-4 bg-white dark:bg-slate-800 text-slate-900 dark:text-white font-bold px-8 py-4 border-l-4 border-slate-900 dark:border-slate-100 transform translate-x-1 transition-all duration-300' href='#'>
            <span className='material-symbols-outlined'>dashboard</span>
            <span className='text-sm font-headline'>Dashboard</span>
          </a>
          <a className='flex items-center gap-4 text-slate-500 dark:text-slate-400 px-8 py-4 hover:bg-slate-200 dark:hover:bg-slate-800/50 transition-all duration-300' href='#'>
            <span className='material-symbols-outlined'>verified_user</span>
            <span className='text-sm font-headline'>Ownership Verifications</span>
          </a>
          <a className='flex items-center gap-4 text-slate-500 dark:text-slate-400 px-8 py-4 hover:bg-slate-200 dark:hover:bg-slate-800/50 transition-all duration-300' href='#'>
            <span className='material-symbols-outlined'>payments</span>
            <span className='text-sm font-headline'>Member Ledger</span>
          </a>
          <a className='flex items-center gap-4 text-slate-500 dark:text-slate-400 px-8 py-4 hover:bg-slate-200 dark:hover:bg-slate-800/50 transition-all duration-300' href='#'>
            <span className='material-symbols-outlined'>history</span>
            <span className='text-sm font-headline'>Transfer History</span>
          </a>
          <a className='flex items-center gap-4 text-slate-500 dark:text-slate-400 px-8 py-4 hover:bg-slate-200 dark:hover:bg-slate-800/50 transition-all duration-300' href='#'>
            <span className='material-symbols-outlined'>settings</span>
            <span className='text-sm font-headline'>Settings</span>
          </a>
        </nav>
        <div className='px-6 py-8 mt-auto'>
          <button className='w-full primary-gradient text-on-primary py-4 px-4 rounded-lg font-headline font-bold text-sm tracking-tight flex items-center justify-center gap-2 active:scale-95 duration-150'>
            <span className='material-symbols-outlined text-sm'>add</span>
            New Transfer
          </button>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
