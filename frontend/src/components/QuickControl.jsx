import React from 'react';

function QuickControl() {
  return (
    <div className='lg:col-span-4 space-y-6'>
      <h3 className='text-xl font-bold font-headline text-on-surface'>Quick Control</h3>
      <div className='space-y-3'>
        <button className='w-full flex items-center justify-between p-4 bg-surface-container-low hover:bg-surface-container-high rounded-xl transition-colors group'>
          <div className='flex items-center gap-4'>
            <div className='w-10 h-10 bg-primary/5 rounded-lg flex items-center justify-center'>
              <span className='material-symbols-outlined text-primary'>upload_file</span>
            </div>
            <span className='font-bold text-sm text-on-surface'>Upload Documents</span>
          </div>
          <span className='material-symbols-outlined text-on-surface-variant group-hover:translate-x-1 transition-transform'>chevron_right</span>
        </button>
        <button className='w-full flex items-center justify-between p-4 bg-surface-container-low hover:bg-surface-container-high rounded-xl transition-colors group'>
          <div className='flex items-center gap-4'>
            <div className='w-10 h-10 bg-primary/5 rounded-lg flex items-center justify-center'>
              <span className='material-symbols-outlined text-primary'>verified_user</span>
            </div>
            <span className='font-bold text-sm text-on-surface'>Check Eligibility</span>
          </div>
          <span className='material-symbols-outlined text-on-surface-variant group-hover:translate-x-1 transition-transform'>chevron_right</span>
        </button>
        <button className='w-full flex items-center justify-between p-4 bg-surface-container-low hover:bg-surface-container-high rounded-xl transition-colors group'>
          <div className='flex items-center gap-4'>
            <div className='w-10 h-10 bg-primary/5 rounded-lg flex items-center justify-center'>
              <span className='material-symbols-outlined text-primary'>support_agent</span>
            </div>
            <span className='font-bold text-sm text-on-surface'>Talk to Specialist</span>
          </div>
          <span className='material-symbols-outlined text-on-surface-variant group-hover:translate-x-1 transition-transform'>chevron_right</span>
        </button>
      </div>
      <div className='p-6 bg-tertiary-container text-on-tertiary-container rounded-2xl space-y-3'>
        <div className='flex items-center gap-3'>
          <span className='material-symbols-outlined text-on-tertiary-container' style={{fill: 1}}>shield_lock</span>
          <p className='font-bold font-headline text-sm'>Military-Grade Encryption</p>
        </div>
        <p className='text-xs opacity-90 leading-relaxed'>Your financial data is protected by AES-256 standards. Vault Prime never shares your raw data with third parties.</p>
      </div>
    </div>
  );
}

export default QuickControl;
