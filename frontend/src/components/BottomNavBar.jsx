import React from 'react';

function BottomNavBar() {
  return (
    <nav className='fixed bottom-0 left-0 w-full z-50 flex justify-around items-center px-4 pb-6 pt-3 bg-white/90 dark:bg-slate-950/90 backdrop-blur-2xl shadow-[0_-4px_20px_rgba(0,0,0,0.05)] rounded-t-3xl border-t border-slate-200/20'>
      <a className='flex flex-col items-center justify-center text-slate-400 dark:text-slate-500 px-5 py-2 hover:text-blue-600 active:scale-90 transition-all duration-150' href='#'>
        <span className='material-symbols-outlined'>credit_card</span>
        <span className='font-inter text-[11px] font-semibold uppercase tracking-wider mt-1'>Cards</span>
      </a>
      <a className='flex flex-col items-center justify-center text-slate-400 dark:text-slate-500 px-5 py-2 hover:text-blue-600 active:scale-90 transition-all duration-150' href='#'>
        <span className='material-symbols-outlined'>add_circle</span>
        <span className='font-inter text-[11px] font-semibold uppercase tracking-wider mt-1'>Apply</span>
      </a>
      <a className='flex flex-col items-center justify-center bg-blue-50 dark:bg-blue-900/30 text-blue-700 dark:text-blue-300 rounded-2xl px-5 py-2 active:scale-90 transition-all duration-150' href='#'>
        <span className='material-symbols-outlined' style={{fill: 1}}>history</span>
        <span className='font-inter text-[11px] font-semibold uppercase tracking-wider mt-1'>Activity</span>
      </a>
      <a className='flex flex-col items-center justify-center text-slate-400 dark:text-slate-500 px-5 py-2 hover:text-blue-600 active:scale-90 transition-all duration-150' href='#'>
        <span className='material-symbols-outlined'>help_outline</span>
        <span className='font-inter text-[11px] font-semibold uppercase tracking-wider mt-1'>Support</span>
      </a>
    </nav>
  );
}

export default BottomNavBar;
