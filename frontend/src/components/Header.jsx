import React from 'react';

function Header() {
  return (
    <header className='fixed top-0 w-full z-50 bg-slate-50/80 dark:bg-slate-900/80 backdrop-blur-xl shadow-sm flex justify-between items-center px-6 h-16 w-full'>
      <div className='flex items-center gap-4'>
        <button className='material-symbols-outlined text-blue-900 dark:text-blue-100 p-2 hover:bg-slate-200/50 transition-colors active:scale-95 duration-200'>menu</button>
        <h1 className='text-xl font-extrabold tracking-tighter text-blue-950 dark:text-white font-headline'>Architect</h1>
      </div>
      <div className='flex items-center gap-4'>
        <div className='w-10 h-10 rounded-full bg-surface-container-high flex items-center justify-center border-2 border-primary/10 overflow-hidden'>
          <img alt='User Avatar' className='w-full h-full object-cover' src='https://lh3.googleusercontent.com/aida-public/AB6AXuABUJBcArfHqrIFjUphaxov4WBV-YnZq_iaU_BQJbQsxzkqjab_bc6otgkdyJ-iyj5WDZMaWphTmLq7KH5apzD0Ci0Ca6L-YQEXIm3BJiZxN1SBZ1LiMAiD8AK1e-JkUrO_t62yy5PVBVWAL_WOVa9D8Qwkyy1yMrVYPhYVyA_o2WumH6PzLjE2guZF_JTRLH9VYT-B_jEwhK4zXOvKDK5GK4qXIbNU57St9mCq6ywz1cafWRNnxAwI2Oa8_UJhIAyIZlYdZ7Ynmqg'/>
        </div>
      </div>
    </header>
  );
}

export default Header;
