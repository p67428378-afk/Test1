import React from 'react';

const MetricCard = ({ title, value, unit, icon }) => {
  return (
    <div className='col-span-12 md:col-span-4 bg-surface-container-lowest p-8 rounded-xl relative overflow-hidden group'>
      <div className='relative z-10'>
        <p className='text-on-surface-variant text-xs font-bold uppercase tracking-widest mb-4'>{title}</p>
        <div className='flex items-baseline gap-2'>
          <span className='text-4xl font-black font-headline text-on-surface'>{value}</span>
          {unit && <span className='text-sm font-medium text-on-surface-variant'>{unit}</span>}
        </div>
      </div>
      <span className='material-symbols-outlined absolute -bottom-4 -right-4 text-9xl text-slate-50 opacity-10 group-hover:scale-110 transition-transform duration-500'>{icon}</span>
    </div>
  );
};

export default MetricCard;
