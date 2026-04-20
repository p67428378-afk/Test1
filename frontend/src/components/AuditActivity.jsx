import React from 'react';

const AuditActivity = () => {
  const activities = [
    {
      icon: 'upload_file',
      bgColor: 'bg-primary-container',
      title: 'New Document Uploaded',
      description: "Flat 402 submitted 'Sale Deed' draft for review.",
      time: '12 Mins Ago',
    },
    {
      icon: 'check_circle',
      bgColor: 'bg-on-secondary-container',
      title: 'NOC Approved',
      description: 'Secretary cleared No Objection Certificate for Flat 105.',
      time: '2 Hours Ago',
    },
    {
      icon: 'person_add',
      bgColor: 'bg-slate-300',
      title: 'New Member Verification',
      description: 'KYC verification started for potential owner of Flat 312.',
      time: '5 Hours Ago',
    },
    {
      icon: 'priority_high',
      bgColor: 'bg-error-container',
      title: 'Flagged: Dues Owed',
      description: 'Flat 204 transfer halted due to unpaid maintenance dues.',
      time: 'Yesterday',
    },
  ];

  return (
    <div className='bg-surface-container-low p-8 rounded-xl h-full'>
      <div className='flex items-center gap-2 mb-8'>
        <span className='material-symbols-outlined text-primary'>history_edu</span>
        <h3 className='text-lg font-bold font-headline text-on-surface'>Recent Audit Activity</h3>
      </div>
      <div className='space-y-8 relative'>
        <div className='absolute left-[11px] top-2 bottom-2 w-px bg-outline-variant opacity-30'></div>
        {activities.map((activity, index) => (
          <div key={index} className='relative flex gap-4'>
            <div className={`relative z-10 w-6 h-6 rounded-full ${activity.bgColor} flex items-center justify-center`}>
              <span className={`material-symbols-outlined text-[12px] ${activity.bgColor === 'bg-slate-300' ? 'text-slate-700' : 'text-white'}`}>{activity.icon}</span>
            </div>
            <div className='space-y-1'>
              <p className='text-sm font-semibold text-on-surface'>{activity.title}</p>
              <p className='text-xs text-on-surface-variant'>{activity.description}</p>
              <p className='text-[10px] font-bold text-slate-400 uppercase tracking-tighter'>{activity.time}</p>
            </div>
          </div>
        ))}
      </div>
      <button className='w-full mt-10 py-3 rounded-lg border border-outline-variant/30 text-xs font-bold uppercase tracking-widest text-on-surface-variant hover:bg-surface-container-highest transition-colors'>
        Full Activity Log
      </button>
    </div>
  );
};

export default AuditActivity;
