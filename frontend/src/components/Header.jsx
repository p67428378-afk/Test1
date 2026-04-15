import React from 'react';

const Header = () => {
  return (
    <header className='sticky top-0 z-40 flex items-center justify-between px-8 py-4 bg-white/80 dark:bg-slate-950/80 backdrop-blur-xl shadow-sm dark:shadow-none'>
      <div className='flex items-center gap-4'>
        <h1 className='font-manrope font-bold text-lg text-blue-900 dark:text-blue-100'>Vehicle Premium</h1>
        <div className='h-6 w-px bg-slate-200 mx-2'></div>
        <div className='relative group'>
          <span className='material-symbols-outlined absolute left-3 top-1/2 -translate-y-1/2 text-slate-400' data-icon='search'>search</span>
          <input className='pl-10 pr-4 py-1.5 bg-surface-container-low rounded-lg border-none focus:ring-2 focus:ring-primary-fixed-dim text-sm w-64 transition-all' placeholder='Search vehicle data...' type='text' />
        </div>
      </div>
      <div className='flex items-center gap-6'>
        <span className='material-symbols-outlined cursor-pointer hover:opacity-80 transition-opacity text-blue-900 dark:text-blue-100' data-icon='notifications'>notifications</span>
        <span className='material-symbols-outlined cursor-pointer hover:opacity-80 transition-opacity text-blue-900 dark:text-blue-100' data-icon='settings'>settings</span>
        <img className='w-8 h-8 rounded-full border border-slate-200' alt='Close-up portrait of a corporate professional with a subtle smile, high-end editorial lighting' src='https://lh3.googleusercontent.com/aida-public/AB6AXuAA28SnQVth5t12Tj-j7FxCBzpEzSjJQai6WexZPLz3Yj81Dj2QW6eKG1E6c8gFGv7LD5qPkNsUJBIe2SG_Q1i-ervSJSTxlqLR8fAJgWyjP7PI4x5A09ofBqMzaxjvxxHZvhiXI0S-ApeCvYEBF1GIm5LPfMc0b5mg28ASmzZkVx_4XgVEiKbVEspwcj5y4TkHzeP_VNzQLsdSqn88gbf3a6z8hCRBjDg1qOPItHeZSjxPrGTyiyx-yq18qEkxd6SXAywjg_FN10A' />
      </div>
    </header>
  );
};

export default Header;
