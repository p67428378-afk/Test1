import React, { useState } from 'react';
import { calculatePremium } from '../services/api';

const PremiumCalculator = () => {
  const [vehicleType, setVehicleType] = useState('SUV');
  const [ncbPercentage, setNcbPercentage] = useState(0.35);
  const [vehicleMultiplier, setVehicleMultiplier] = useState(1.2);
  const [calculatedPremium, setCalculatedPremium] = useState(750.0);
  const [policyDetails, setPolicyDetails] = useState({
    base_premium: 500.0,
    vehicle_type: 'SUV',
    no_claims_bonus_percentage: 0.35,
    vehicle_multiplier: 1.2,
  });
  const [error, setError] = useState(null);

  const handleCalculatePremium = async () => {
    try {
      const data = {
        vehicle_type: vehicleType,
        no_claims_bonus_percentage: ncbPercentage,
        vehicle_multiplier: vehicleMultiplier,
      };
      const result = await calculatePremium(data);
      setCalculatedPremium(result.calculated_premium);
      setPolicyDetails(result.policy_details);
      setError(null);
    } catch (err) {
      setError(err.detail[0].msg);
    }
  };

  return (
    <div className='grid grid-cols-12 gap-8'>
      <section className='col-span-7 space-y-6'>
        <div className='bg-surface-container-lowest p-8 rounded-xl relative overflow-hidden'>
          <div className='absolute left-0 top-0 bottom-0 w-1 bg-surface-tint'></div>
          <div className='space-y-10'>
            <div>
              <label className='block text-sm font-bold text-on-surface-variant mb-4 flex items-center uppercase tracking-wider'>
                <span className='material-symbols-outlined text-xs mr-2'>directions_car</span>
                Vehicle Classification
              </label>
              <div className='relative'>
                <select
                  value={vehicleType}
                  onChange={(e) => setVehicleType(e.target.value)}
                  className='w-full bg-surface-container-low border-none rounded-lg py-4 px-5 text-on-surface font-medium appearance-none focus:ring-2 focus:ring-primary/10 transition-all'
                >
                  <option>Sedan</option>
                  <option>SUV</option>
                  <option>Truck</option>
                </select>
                <span className='material-symbols-outlined absolute right-4 top-1/2 -translate-y-1/2 pointer-events-none text-on-surface-variant'>expand_more</span>
              </div>
            </div>
            <div>
              <div className='flex justify-between items-center mb-6'>
                <label className='text-sm font-bold text-on-surface-variant uppercase tracking-wider flex items-center'>
                  <span className='material-symbols-outlined text-xs mr-2'>verified</span>
                  No Claims Bonus (NCB)
                </label>
                <span className='text-lg font-black text-primary'>{Math.round(ncbPercentage * 100)}%</span>
              </div>
              <div className='px-2'>
                <input
                  type='range'
                  min='0.2'
                  max='0.5'
                  step='0.01'
                  value={ncbPercentage}
                  onChange={(e) => setNcbPercentage(parseFloat(e.target.value))}
                  className='w-full'
                />
                <div className='flex justify-between mt-3 text-[10px] font-bold text-on-surface-variant/50 uppercase tracking-tighter'>
                  <span>20% (Minimum)</span>
                  <span>50% (Loyalty Cap)</span>
                </div>
              </div>
            </div>
            <div>
              <div className='flex justify-between items-center mb-6'>
                <label className='text-sm font-bold text-on-surface-variant uppercase tracking-wider flex items-center'>
                  <span className='material-symbols-outlined text-xs mr-2'>speed</span>
                  Vehicle Multiplier
                </label>
                <span className='text-lg font-black text-primary'>{vehicleMultiplier}x</span>
              </div>
              <div className='px-2'>
                <input
                  type='range'
                  min='0.8'
                  max='1.6'
                  step='0.1'
                  value={vehicleMultiplier}
                  onChange={(e) => setVehicleMultiplier(parseFloat(e.target.value))}
                  className='w-full'
                />
                <div className='flex justify-between mt-3 text-[10px] font-bold text-on-surface-variant/50 uppercase tracking-tighter'>
                  <span>0.8x (Efficiency)</span>
                  <span>1.6x (Performance)</span>
                </div>
              </div>
            </div>
            <button
              onClick={handleCalculatePremium}
              className='w-full bg-primary text-on-primary py-5 rounded-full font-black text-lg shadow-xl shadow-primary/10 hover:shadow-primary/20 transition-all flex items-center justify-center group'
            >
              <span>Calculate Premium</span>
              <span className='material-symbols-outlined ml-3 group-hover:translate-x-1 transition-transform'>arrow_forward</span>
            </button>
            {error && <p className='text-red-500'>{error}</p>}
          </div>
        </div>
      </section>
      <section className='col-span-5 space-y-6'>
        <div className='bg-surface-container-lowest p-8 rounded-xl shadow-sm relative overflow-hidden'>
          <div className='flex items-start justify-between mb-8'>
            <span className='text-sm font-bold text-on-surface-variant uppercase tracking-widest'>Calculated Premium</span>
            <span className='material-symbols-outlined text-surface-tint'>payments</span>
          </div>
          <div className='mb-2'>
            <span className='text-6xl font-black text-primary font-display tracking-tighter'>${calculatedPremium.toFixed(2)}</span>
            <span className='text-on-surface-variant text-sm font-semibold ml-2'>/ Annual</span>
          </div>
          <div className='h-1 w-24 bg-surface-tint rounded-full mt-6'></div>
          <div className='mt-10 bg-surface-container-low rounded-lg p-4 flex items-center justify-between'>
            <div className='flex items-center'>
              <span className='material-symbols-outlined text-on-primary-container mr-3'>info</span>
              <span className='text-xs font-semibold text-on-surface-variant'>Next adjustment scheduled for Jan 2025</span>
            </div>
            <span className='material-symbols-outlined text-on-surface-variant text-sm cursor-pointer'>close</span>
          </div>
        </div>
        <div className='bg-white p-8 rounded-xl border border-outline-variant/15'>
          <h3 className='text-sm font-bold text-on-surface-variant uppercase tracking-widest mb-6'>Policy Details Summary</h3>
          <div className='space-y-4'>
            <div className='flex justify-between items-center py-2 border-b border-surface-container'>
              <span className='text-on-surface-variant text-sm'>Base Premium</span>
              <span className='font-bold text-on-surface'>${policyDetails.base_premium.toFixed(2)}</span>
            </div>
            <div className='flex justify-between items-center py-2 border-b border-surface-container'>
              <span className='text-on-surface-variant text-sm'>Selected Vehicle Type</span>
              <span className='font-bold text-on-surface'>{policyDetails.vehicle_type}</span>
            </div>
            <div className='flex justify-between items-center py-2 border-b border-surface-container'>
              <span className='text-on-surface-variant text-sm'>NCB Percentage</span>
              <span className='font-bold text-on-surface'>{Math.round(policyDetails.no_claims_bonus_percentage * 100)}%</span>
            </div>
            <div className='flex justify-between items-center py-2'>
              <span className='text-on-surface-variant text-sm'>Vehicle Multiplier</span>
              <span className='font-bold text-on-surface'>{policyDetails.vehicle_multiplier}x</span>
            </div>
          </div>
          <div className='mt-8 pt-6 border-t border-dashed border-outline-variant/30 flex items-center justify-between'>
            <span className='text-xs font-bold text-on-surface-variant uppercase'>Total Liability Shield</span>
            <span className='text-xl font-black text-primary'>$1,250,000</span>
          </div>
        </div>
      </section>
    </div>
  );
};

export default PremiumCalculator;
