import React from 'react';
import PremiumCalculator from './components/PremiumCalculator';

function App() {
  return (
    <div className='bg-surface text-on-surface h-screen overflow-hidden flex'>
      <aside className='flex flex-col p-6 space-y-8 bg-slate-50 dark:bg-slate-900 h-screen w-64 fixed left-0 top-0 z-50 font-manrope tracking-tight shadow-none border-r border-slate-100/10'>
        <div className='flex items-center space-x-3 px-2'>
          <div className='w-8 h-8 rounded bg-primary flex items-center justify-center'>
            <span className='material-symbols-outlined text-white text-sm' data-icon='shield'>shield</span>
          </div>
          <div>
            <h1 className='text-xl font-bold text-slate-950 dark:text-white leading-tight'>Sovereign Ledger</h1>
            <p className='text-[10px] uppercase tracking-[0.2em] text-on-surface-variant font-semibold'>Premium Shield</p>
          </div>
        </div>
        <nav className='flex-1 space-y-1'>
          <a className='flex items-center px-4 py-3 text-slate-950 dark:text-white font-bold bg-white dark:bg-slate-800 rounded-lg shadow-sm transition-all scale-95 active:scale-90 duration-200' href='#'>
            <span className='material-symbols-outlined mr-3' data-icon='calculate'>calculate</span>
            <span>Calculator</span>
          </a>
          <a className='flex items-center px-4 py-3 text-slate-500 dark:text-slate-400 font-medium hover:bg-slate-200/50 dark:hover:bg-slate-800/50 transition-all' href='#'>
            <span className='material-symbols-outlined mr-3' data-icon='request_quote'>request_quote</span>
            <span>Quotes</span>
          </a>
          <a className='flex items-center px-4 py-3 text-slate-500 dark:text-slate-400 font-medium hover:bg-slate-200/50 dark:hover:bg-slate-800/50 transition-all' href='#'>
            <span className='material-symbols-outlined mr-3' data-icon='verified_user'>verified_user</span>
            <span>Policies</span>
          </a>
          <a className='flex items-center px-4 py-3 text-slate-500 dark:text-slate-400 font-medium hover:bg-slate-200/50 dark:hover:bg-slate-800/50 transition-all' href='#'>
            <span className='material-symbols-outlined mr-3' data-icon='folder_open'>folder_open</span>
            <span>Documents</span>
          </a>
        </nav>
        <button className='w-full py-3 px-4 bg-primary text-on-primary rounded-full font-bold text-sm flex items-center justify-center space-x-2 transition-transform active:scale-95'>
          <span className='material-symbols-outlined text-sm' data-icon='add'>add</span>
          <span>New Application</span>
        </button>
        <div className='pt-6 border-t border-slate-200/50'>
          <a className='flex items-center px-4 py-2 text-slate-500 dark:text-slate-400 font-medium text-sm hover:bg-slate-200/50 transition-all' href='#'>
            <span className='material-symbols-outlined mr-3' data-icon='contact_support'>contact_support</span>
            <span>Support</span>
          </a>
          <a className='flex items-center px-4 py-2 text-slate-500 dark:text-slate-400 font-medium text-sm hover:bg-slate-200/50 transition-all' href='#'>
            <span className='material-symbols-outlined mr-3' data-icon='settings'>settings</span>
            <span>Settings</span>
          </a>
        </div>
      </aside>
      <div className='flex-1 ml-64 flex flex-col h-screen'>
        <header className='flex justify-between items-center px-8 py-4 sticky top-0 w-full z-40 bg-white/80 dark:bg-slate-950/80 backdrop-blur-xl border-b border-slate-100 dark:border-slate-800/50 shadow-sm font-manrope text-sm font-semibold'>
          <div className='flex items-center space-x-8'>
            <span className='text-lg font-black tracking-tighter text-slate-900 dark:text-white'>Premium Ledger</span>
            <nav className='hidden md:flex space-x-6'>
              <a className='text-slate-400 dark:text-slate-500 hover:text-slate-900 dark:hover:text-slate-100 transition-colors' href='#'>Dashboard</a>
              <a className='text-slate-400 dark:text-slate-500 hover:text-slate-900 dark:hover:text-slate-100 transition-colors' href='#'>Analytics</a>
              <a className='text-slate-400 dark:text-slate-500 hover:text-slate-900 dark:hover:text-slate-100 transition-colors' href='#'>Reports</a>
            </nav>
          </div>
          <div className='flex items-center space-x-6'>
            <div className='relative'>
              <span className='material-symbols-outlined text-on-surface-variant cursor-pointer opacity-80 hover:opacity-100 duration-300' data-icon='search'>search</span>
            </div>
            <div className='flex items-center space-x-4'>
              <span className='material-symbols-outlined text-on-surface-variant cursor-pointer opacity-80 hover:opacity-100 duration-300' data-icon='notifications'>notifications</span>
              <div className='w-8 h-8 rounded-full bg-surface-container-high overflow-hidden border border-outline-variant/20'>
                <img alt='User Profile' className='w-full h-full object-cover' src='https://lh3.googleusercontent.com/aida-public/AB6AXuBIZTElN9u472NGlJv-WxAdCyDnjnemo_Wpp24NOdtingIkG-ujAWJCnVrxCoYu_iZYRgZ8B98xU7HNcWxjenSqSkKC5Zxy8LANWT8GBp9hTRhP345gLWNomS2qzrxiS_vk0UM7-eFa9KJl3jMGdpb4pnlR6AW0ZMfw7guITEVTkzt0aRiz94pYAFNrGb4rLgUXY16k73IORBzm_Pv48wLKqI3SM7v3XWN1LIRc270OMPs-NrCdMn8N97OzM4SlVa8y0RebX8Vv2mA' />
              </div>
            </div>
          </div>
        </header>
        <main className='p-10 flex-1 overflow-y-auto max-w-[1440px] mx-auto w-full'>
          <PremiumCalculator />
        </main>
      </div>
    </div>
  );
}

export default App;
