import React from 'react';

const Deposit = () => {
  return (
    <div className='bg-primary text-white rounded-xl p-8 shadow-xl relative overflow-hidden'>
      <div className='relative z-10'>
        <h3 className='text-xs font-bold text-blue-300 uppercase tracking-[0.2em] mb-6'>Secure Deposit</h3>
        <div className='grid grid-cols-2 gap-4'>
          <button className='bg-white/10 hover:bg-white/20 transition-colors p-6 rounded-lg flex flex-col items-center gap-4 text-center group'>
            <span className='material-symbols-outlined text-4xl group-hover:scale-110 transition-transform'>photo_camera</span>
            <span className='text-xs font-bold uppercase tracking-widest leading-tight'>Mobile Check<br/>Deposit</span>
          </button>
          <button className='bg-white/10 hover:bg-white/20 transition-colors p-6 rounded-lg flex flex-col items-center gap-4 text-center group'>
            <span className='material-symbols-outlined text-4xl group-hover:scale-110 transition-transform'>swap_horiz</span>
            <span className='text-xs font-bold uppercase tracking-widest leading-tight'>Electronic<br/>Transfer</span>
          </button>
        </div>
      </div>
      <div className='absolute -bottom-10 -right-10 opacity-10'>
        <span className='material-symbols-outlined text-[200px]'>qr_code_2</span>
      </div>
    </div>
  );
};

export default Deposit;
