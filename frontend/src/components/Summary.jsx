import React from 'react';

const Summary = ({ calculatedPremium, baseRate, ncbYears, vehicleMultiplier }) => {
  const ncbDiscount = () => {
    if (ncbYears >= 4) return baseRate * 0.5;
    if (ncbYears === 3) return baseRate * 0.4;
    if (ncbYears === 2) return baseRate * 0.3;
    if (ncbYears === 1) return baseRate * 0.2;
    return 0;
  };

  const vehicleLoading = () => {
    const premiumAfterNcb = baseRate - ncbDiscount();
    return (premiumAfterNcb * vehicleMultiplier) - premiumAfterNcb;
  };

  return (
    <div className='lg:w-[450px]'>
      <div className='glass-panel sticky top-32 rounded-3xl p-10 border border-white/20 shadow-[0_40px_80px_rgba(25,28,30,0.06)] overflow-hidden'>
        <div className='absolute -top-24 -right-24 w-64 h-64 bg-primary-fixed/30 blur-[80px] rounded-full pointer-events-none'></div>
        <div className='relative z-10'>
          <div className='flex items-center gap-2 mb-10'>
            <div className='w-2 h-2 rounded-full bg-primary animate-pulse'></div>
            <span className='font-label text-[10px] uppercase tracking-[0.2em] text-on-surface-variant font-bold'>Estimated Annual Premium</span>
          </div>
          <div className='mb-12'>
            <div className='font-headline text-7xl font-extrabold text-primary tracking-tight mb-2'>
              ${calculatedPremium ? calculatedPremium.toFixed(2) : '0.00'}
            </div>
            <div className='text-on-surface-variant text-sm font-medium'>Billed annually or ${calculatedPremium ? (calculatedPremium / 12).toFixed(2) : '0.00'}/month</div>
          </div>
          <div className='space-y-6 mb-12'>
            <div className='flex justify-between items-center'>
              <span className='text-on-surface-variant text-sm'>Base Rate</span>
              <span className='font-headline text-on-surface font-semibold'>${baseRate.toFixed(2)}</span>
            </div>
            <div className='flex justify-between items-center'>
              <span className='text-on-surface-variant text-sm'>NCB Discount ({ncbYears} Years)</span>
              <span className='font-headline text-tertiary font-semibold'>-${ncbDiscount().toFixed(2)}</span>
            </div>
            <div className='flex justify-between items-center'>
              <span className='text-on-surface-variant text-sm'>Vehicle Loading ({vehicleMultiplier}x)</span>
              <span className='font-headline text-on-surface font-semibold'>+${vehicleLoading().toFixed(2)}</span>
            </div>
            <div className='pt-6 border-t border-outline-variant/20'>
              <div className='flex justify-between items-center font-bold'>
                <span className='text-on-surface text-base'>Subtotal</span>
                <span className='font-headline text-primary text-xl'>${calculatedPremium ? calculatedPremium.toFixed(2) : '0.00'}</span>
              </div>
            </div>
          </div>
          <div className='space-y-4'>
            <div className='flex items-center gap-3 p-4 bg-primary-fixed/20 rounded-xl'>
              <span className='material-symbols-outlined text-primary'>verified_user</span>
              <div>
                <div className='text-sm font-bold text-on-primary-fixed'>Guaranteed Quote</div>
                <div className='text-xs text-on-primary-fixed-variant'>Valid for 30 days based on data provided</div>
              </div>
            </div>
            <button className='w-full py-4 px-6 bg-gradient-to-br from-primary to-primary-container text-on-primary font-bold rounded-xl shadow-lg hover:shadow-primary/20 transition-all active:scale-[0.98]'>
              Proceed to Payment
            </button>
            <button className='w-full py-3 px-6 text-primary font-semibold text-sm hover:underline'>
              Download Quote PDF
            </button>
          </div>
        </div>
        <div className='mt-10 rounded-2xl overflow-hidden h-32 relative group'>
          <img alt='Premium Vehicle' className='w-full h-full object-cover transition-transform duration-700 group-hover:scale-110' src='https://lh3.googleusercontent.com/aida-public/AB6AXuA0C-txSr4xk0ER0ivuuw3upTWuEiR1OIqHDAnwqMaTgyO-eylW1n54eWEgKWKSby5V6q3-h1PlI8tp5ZRUGpvc0K-TRul4Ym36K-jY8g28mEO1eY_gYxl517CLgsIc-Q-y3mf80s3Yg_ni8ZCqcpuld0eylpvFH6QaC2R4T9oDuRfwku1WM1PWezOSn24BsbK7h7_JGHfCCfIdLaE1a3XD1udO1V-iMWmXrG7tayJWRjnbjvZAsCdR8A65Tx8K9GPazOmGTvUbOdU' />
          <div className='absolute inset-0 bg-gradient-to-t from-primary/60 to-transparent'></div>
          <div className='absolute bottom-3 left-4 text-white text-[10px] font-bold uppercase tracking-wider'>Premium Selection</div>
        </div>
      </div>
    </div>
  );
};

export default Summary;
