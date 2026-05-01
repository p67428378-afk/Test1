import React from 'react';

const Sidebar = () => {
  return (
    <aside className='fixed left-0 top-0 h-full flex flex-col bg-slate-50 dark:bg-slate-900 h-screen w-64 border-r-0 z-50'>
      <div className='p-8'>
        <span className='font-manrope font-extrabold text-blue-900 dark:text-white tracking-tighter text-2xl'>Editorial Assurance</span>
        <p className='font-manrope text-base tracking-tight text-slate-400 mt-1'>Premium Calculator</p>
      </div>
      <nav className='flex-1 px-4 space-y-2 mt-8'>
        <a className='flex items-center gap-3 px-4 py-3 duration-200 ease-in-out hover:bg-blue-50 dark:hover:bg-blue-900/30 text-blue-900 dark:text-white font-bold border-r-4 border-blue-900 dark:border-blue-400' href='#'>
          <span className='material-symbols-outlined' data-icon='calculate'>calculate</span>
          <span className='font-manrope text-base tracking-tight'>Calculators</span>
        </a>
        <a className='flex items-center gap-3 px-4 py-3 duration-200 ease-in-out hover:bg-blue-50 dark:hover:bg-blue-900/30 text-slate-500 dark:text-slate-400 font-medium' href='#'>
          <span className='material-symbols-outlined' data-icon='dashboard'>dashboard</span>
          <span className='font-manrope text-base tracking-tight'>Dashboard</span>
        </a>
        <a className='flex items-center gap-3 px-4 py-3 duration-200 ease-in-out hover:bg-blue-50 dark:hover:bg-blue-900/30 text-slate-500 dark:text-slate-400 font-medium' href='#'>
          <span className='material-symbols-outlined' data-icon='verified_user'>verified_user</span>
          <span className='font-manrope text-base tracking-tight'>Policies</span>
        </a>
        <a className='flex items-center gap-3 px-4 py-3 duration-200 ease-in-out hover:bg-blue-50 dark:hover:bg-blue-900/30 text-slate-500 dark:text-slate-400 font-medium' href='#'>
          <span className='material-symbols-outlined' data-icon='assignment_late'>assignment_late</span>
          <span className='font-manrope text-base tracking-tight'>Claims</span>
        </a>
        <a className='flex items-center gap-3 px-4 py-3 duration-200 ease-in-out hover:bg-blue-50 dark:hover:bg-blue-900/30 text-slate-500 dark:text-slate-400 font-medium' href='#'>
          <span className='material-symbols-outlined' data-icon='support_agent'>support_agent</span>
          <span className='font-manrope text-base tracking-tight'>Support</span>
        </a>
      </nav>
      <div className='p-8 border-t border-slate-100 dark:border-slate-800'>
        <div className='flex items-center gap-3'>
          <img className='w-10 h-10 rounded-full object-cover' alt='Professional insurance agent in a sharp navy suit looking confident in a modern office setting' src='https://lh3.googleusercontent.com/aida-public/AB6AXuAI1xmMtLlwAz9vnwQzy6oyM1jfjL80dN1ws1rhwRBKy-Ix0eHQPiTci2zbqZkcY2MvZjYCkqCV8EV6j8jLW1eRjbuzF8WHaEBqET7mhYhShhaQJHUXMIs8SfO5YjDljfuCJORqQtb_9uP35TQfz-NYtnyfOs6V0OYiTZGpupCSqIe-1phCFIY00A-ASKaSy_rqw_p9q61Oqppahrci34xX5A8HK_HftO2om3fv8C3unwarvUR-u-cbwdX1lp_qIJt0RumYWZi-XoI'/>
          <div>
            <p className='text-sm font-bold text-blue-900 dark:text-white'>Alex Sterling</p>
            <p className='text-xs text-slate-500'>Premium Partner</p>
          </div>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;
