import React from 'react';

function RecentActivity() {
  return (
    <div className='lg:col-span-8 space-y-6'>
      <div className='flex justify-between items-center'>
        <h3 className='text-xl font-bold font-headline text-on-surface'>Recent Activity</h3>
        <span className='text-xs font-bold text-on-surface-variant font-label uppercase tracking-widest'>Last 7 Days</span>
      </div>
      <div className='bg-surface-container-lowest rounded-3xl overflow-hidden shadow-sm border border-outline-variant/10'>
        <div className='divide-y divide-outline-variant/10'>
          <div className='p-6 flex items-start justify-between bg-surface-container-low/30'>
            <div className='flex gap-4'>
              <div className='w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center shrink-0'>
                <span className='material-symbols-outlined text-blue-700'>info</span>
              </div>
              <div>
                <p className='font-bold text-sm text-on-surface'>Address Verified</p>
                <p className='text-xs text-on-surface-variant mt-1'>Your residential proof has been accepted by our audit team.</p>
              </div>
            </div>
            <span className='text-[10px] font-bold text-on-surface-variant uppercase tracking-tighter'>2h ago</span>
          </div>
          <div className='p-6 flex items-start justify-between'>
            <div className='flex gap-4'>
              <div className='w-10 h-10 rounded-full bg-green-100 flex items-center justify-center shrink-0'>
                <span className='material-symbols-outlined text-green-700'>security</span>
              </div>
              <div>
                <p className='font-bold text-sm text-on-surface'>Soft Credit Inquiry</p>
                <p className='text-xs text-on-surface-variant mt-1'>Initial eligibility check completed with TransUnion.</p>
              </div>
            </div>
            <span className='text-[10px] font-bold text-on-surface-variant uppercase tracking-tighter'>Yesterday</span>
          </div>
          <div className='p-6 flex items-start justify-between bg-surface-container-low/30'>
            <div className='flex gap-4'>
              <div className='w-10 h-10 rounded-full bg-amber-100 flex items-center justify-center shrink-0'>
                <span className='material-symbols-outlined text-amber-700'>notifications_active</span>
              </div>
              <div>
                <p className='font-bold text-sm text-on-surface'>Application Started</p>
                <p className='text-xs text-on-surface-variant mt-1'>You began your journey with the Vault Infinite Card.</p>
              </div>
            </div>
            <span className='text-[10px] font-bold text-on-surface-variant uppercase tracking-tighter'>Oct 24</span>
          </div>
        </div>
      </div>
    </div>
  );
}

export default RecentActivity;
