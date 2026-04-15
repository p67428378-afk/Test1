import React, { useState } from 'react';
import { calculatePremium } from '../services/api';
import Summary from './Summary';

const Calculator = () => {
  const [baseRate, setBaseRate] = useState(500);
  const [ncbYears, setNcbYears] = useState(5);
  const [vehicleMultiplier, setVehicleMultiplier] = useState(1.2);
  const [calculatedPremium, setCalculatedPremium] = useState(480);

  const handleCalculatePremium = async () => {
    try {
      const response = await calculatePremium({
        base_rate: baseRate,
        ncb_years: ncbYears,
        vehicle_multiplier: vehicleMultiplier,
      });
      setCalculatedPremium(response.data.calculated_premium);
    } catch (error) {
      console.error('Error calculating premium:', error);
    }
  };

  return (
    <div className='flex flex-col lg:flex-row gap-12'>
      <div className='flex-1 space-y-16'>
        <section>
          <h2 className='font-headline text-2xl text-on-surface-variant font-bold mb-8'>Policy Holder & Vehicle</h2>
          <div className='bg-surface-container rounded-xl p-8 space-y-8'>
            <div className='grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-8'>
              <div className='flex flex-col gap-2'>
                <label className='font-label text-xs uppercase tracking-wider text-on-surface-variant font-semibold'>Policyholder Name</label>
                <input className='bg-surface-container-lowest border-none rounded-lg h-12 px-4 focus:ring-2 focus:ring-primary-fixed transition-all text-on-surface' placeholder='Johnathan Doe' type='text' />
              </div>
              <div className='flex flex-col gap-2'>
                <label className='font-label text-xs uppercase tracking-wider text-on-surface-variant font-semibold'>Policy Start Date</label>
                <input className='bg-surface-container-lowest border-none rounded-lg h-12 px-4 focus:ring-2 focus:ring-primary-fixed transition-all text-on-surface' type='date' />
              </div>
              <div className='flex flex-col gap-2'>
                <label className='font-label text-xs uppercase tracking-wider text-on-surface-variant font-semibold'>Vehicle Make</label>
                <input className='bg-surface-container-lowest border-none rounded-lg h-12 px-4 focus:ring-2 focus:ring-primary-fixed transition-all text-on-surface' placeholder='Porsche' type='text' />
              </div>
              <div className='flex flex-col gap-2'>
                <label className='font-label text-xs uppercase tracking-wider text-on-surface-variant font-semibold'>Vehicle Model</label>
                <input className='bg-surface-container-lowest border-none rounded-lg h-12 px-4 focus:ring-2 focus:ring-primary-fixed transition-all text-on-surface' placeholder='Taycan 4S' type='text' />
              </div>
              <div className='flex flex-col gap-2'>
                <label className='font-label text-xs uppercase tracking-wider text-on-surface-variant font-semibold'>Vehicle Year</label>
                <input className='bg-surface-container-lowest border-none rounded-lg h-12 px-4 focus:ring-2 focus:ring-primary-fixed transition-all text-on-surface' placeholder='2024' type='number' />
              </div>
              <div className='flex items-end'>
                <button className='w-full h-12 bg-secondary-container text-on-secondary-container rounded-lg font-semibold hover:bg-secondary-fixed transition-all active:scale-95'>Save Policy</button>
              </div>
            </div>
          </div>
        </section>
        <section>
          <h2 className='font-headline text-2xl text-on-surface-variant font-bold mb-8'>Premium Configuration</h2>
          <div className='bg-surface-container rounded-xl p-8 space-y-10'>
            <div className='grid grid-cols-1 md:grid-cols-2 gap-12'>
              <div className='flex flex-col gap-2'>
                <label className='font-label text-xs uppercase tracking-wider text-on-surface-variant font-semibold'>Base Rate (USD)</label>
                <div className='relative'>
                  <span className='absolute left-4 top-1/2 -translate-y-1/2 text-on-surface-variant'>$</span>
                  <input className='w-full bg-surface-container-lowest border-none rounded-lg h-12 pl-8 pr-4 focus:ring-2 focus:ring-primary-fixed transition-all text-on-surface font-semibold' type='number' value={baseRate} onChange={(e) => setBaseRate(parseFloat(e.target.value))} />
                </div>
              </div>
              <div className='flex flex-col gap-2'>
                <label className='font-label text-xs uppercase tracking-wider text-on-surface-variant font-semibold'>NCB Years (No Claims Bonus)</label>
                <div className='relative'>
                  <select className='w-full bg-surface-container-lowest border-none rounded-lg h-12 px-4 focus:ring-2 focus:ring-primary-fixed transition-all appearance-none text-on-surface' value={ncbYears} onChange={(e) => setNcbYears(parseInt(e.target.value))}>
                    <option>0</option>
                    <option>1</option>
                    <option>2</option>
                    <option>3</option>
                    <option>4</option>
                    <option>5</option>
                  </select>
                  <span className='material-symbols-outlined absolute right-4 top-1/2 -translate-y-1/2 pointer-events-none text-outline'>expand_more</span>
                </div>
              </div>
            </div>
            <div className='flex flex-col gap-6'>
              <div className='flex justify-between items-center'>
                <label className='font-label text-xs uppercase tracking-wider text-on-surface-variant font-semibold'>Vehicle Multiplier</label>
                <span className='text-primary font-bold font-headline'>{vehicleMultiplier}x</span>
              </div>
              <div className='relative py-2'>
                <div className='absolute w-full h-2 bg-secondary-container rounded-full top-1/2 -translate-y-1/2'></div>
                <div className='absolute w-[50%] h-2 bg-gradient-to-r from-primary to-primary-container rounded-full top-1/2 -translate-y-1/2'></div>
                <input className='relative w-full h-2 bg-transparent appearance-none cursor-pointer z-10' max='1.6' min='0.8' step='0.1' type='range' value={vehicleMultiplier} onChange={(e) => setVehicleMultiplier(parseFloat(e.target.value))} />
                <div className='flex justify-between mt-4 text-[10px] text-on-surface-variant font-medium uppercase'>
                  <span>0.8x Economy</span>
                  <span>1.2x Standard</span>
                  <span>1.6x Performance</span>
                </div>
              </div>
            </div>
            <button className='w-full h-14 bg-primary text-on-primary rounded-xl font-bold text-lg hover:bg-primary-container transition-all active:scale-[0.98] shadow-sm' onClick={handleCalculatePremium}>
              Calculate Premium
            </button>
          </div>
        </section>
      </div>
      <Summary calculatedPremium={calculatedPremium} baseRate={baseRate} ncbYears={ncbYears} vehicleMultiplier={vehicleMultiplier} />
    </div>
  );
};

export default Calculator;
