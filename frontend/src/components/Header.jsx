import React from 'react';

const Header = () => {
  return (
    <nav className='fixed top-0 w-full z-50 bg-slate-50/70 dark:bg-slate-900/70 backdrop-blur-xl shadow-[0_32px_32px_-4px_rgba(0,29,68,0.06)]'>
      <div className='flex justify-between items-center px-16 py-4 w-full max-w-[1920px] mx-auto'>
        <div className='flex items-center gap-12'>
          <span className='text-xl font-bold tracking-tight text-blue-900 dark:text-blue-100'>The Architectural Ledger</span>
          <div className='hidden md:flex gap-8'>
            <a className='text-blue-900 dark:text-blue-100 font-bold border-b-2 border-blue-900 dark:border-blue-100 pb-1' href='#'>Accounts</a>
            <a className='text-slate-500 dark:text-slate-400 font-medium hover:text-blue-800 dark:hover:text-blue-200 transition-colors duration-200' href='#'>Loans</a>
            <a className='text-slate-500 dark:text-slate-400 font-medium hover:text-blue-800 dark:hover:text-blue-200 transition-colors duration-200' href='#'>Deposits</a>
            <a className='text-slate-500 dark:text-slate-400 font-medium hover:text-blue-800 dark:hover:text-blue-200 transition-colors duration-200' href='#'>Transfers</a>
          </div>
        </div>
        <div className='flex items-center gap-6'>
          <div className='relative group'>
            <span className='material-symbols-outlined text-on-surface-variant cursor-pointer p-2 rounded-full hover:bg-slate-200/50 transition-colors'>notifications</span>
            <span className='absolute top-2 right-2 w-2 h-2 bg-error rounded-full'></span>
          </div>
          <span className='material-symbols-outlined text-on-surface-variant cursor-pointer p-2 rounded-full hover:bg-slate-200/50 transition-colors'>lock</span>
          <div className='flex items-center gap-3 pl-4 border-l border-outline-variant/30'>
            <div className='text-right'>
              <p className='text-xs font-semibold text-on-surface'>Alexander Sterling</p>
              <p className='text-[10px] text-on-surface-variant uppercase tracking-widest'>Private Client</p>
            </div>
            <img alt='User profile' className='w-10 h-10 rounded-lg object-cover' src='https://lh3.googleusercontent.com/aida-public/AB6AXuBTSVpTWXz6yrn86BqJf7_hgG5FF1hxA-QBxOXY_igZ_DO4m1m2C_f_p2MUx5DqnL66yJpI-3XpPKQpBKnlXPlUMyOMfecffWvzRcmo6oE2_Z6Zb92VvBnnOcBVL3dwRwInV_FUuhDaFLElKYIn-UpHxRH1KrNTcSpvpeMtSIAqnIy6KNfMwGpIsajlzTaTjBk1vt8FbQ-BhaJCDinhhxCNaQGZvaHwyaqzdiO80hQUSRcELlYHIY6STav23ZZQxXFVjDMDISGrwHM'/>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Header;
