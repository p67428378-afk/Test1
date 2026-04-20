import React from 'react';

const Header = () => {
  return (
    <header className='w-full h-16 sticky top-0 bg-slate-50 dark:bg-slate-900 z-40 flex justify-between items-center px-8'>
      <div className='flex items-center gap-4 bg-slate-100 dark:bg-slate-800 px-4 py-2 rounded-lg w-96'>
        <span className='material-symbols-outlined text-slate-400'>search</span>
        <input className='bg-transparent border-none focus:ring-0 text-sm w-full font-body text-slate-900 dark:text-white' placeholder='Search Ledger...' type='text'/>
      </div>
      <div className='flex items-center gap-6'>
        <button className='relative text-slate-500 hover:text-slate-900 transition-colors'>
          <span className='material-symbols-outlined'>notifications</span>
          <span className='absolute top-0 right-0 block h-2 w-2 rounded-full bg-error ring-2 ring-white'></span>
        </button>
        <button className='text-slate-500 hover:text-slate-900 transition-colors'>
          <span className='material-symbols-outlined'>help_outline</span>
        </button>
        <div className='h-8 w-8 rounded-full overflow-hidden bg-surface-container-high border border-outline-variant/20'>
          <img alt='Society Owner Avatar' className='w-full h-full object-cover' src='https://lh3.googleusercontent.com/aida-public/AB6AXuDcdUUui67nfI3wIJAyZa7Ik-gzBykDw3mxpzGGVkjWqz4m_XkoAf78xnl1EovLQVWv0z9KTDycwbByd5vQez9h8-uwZllZWpf2U5UxBuWalkQXlS_-rNv_s86S1yvXYV0RRlz9kv3RX5b2UH_i-bOGmNlXmg4dOgAbctUXMMU0wL6XGsUk4kzEtBaxu61qgbE8bydiAzEAm3PKzDUUWOLk-yZwSHNnb5LjFX0oxvgOWb2MI92Bax_9KIc6iRMQLnM1_C8KVEY4ZnK_'/>
        </div>
      </div>
    </header>
  );
};

export default Header;
