'''import React, { useState } from 'react';
import axios from 'axios';

const Calculator = () => {
  const [formData, setFormData] = useState({
    vehicle_make: 'Mercedes-Benz',
    vehicle_model: 'EQS Sedan',
    vehicle_year: 2024,
    vin: '',
    engine_size_cc: 2996,
    ncb_years: 5,
  });

  const [premium, setPremium] = useState(1248.50);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleNcbChange = (e) => {
    const { value } = e.target;
    const ncbYears = parseInt(value.split(' ')[0]);
    setFormData({ ...formData, ncb_years: ncbYears });
  };

  const calculatePremium = async () => {
    try {
      const response = await axios.post('/api/v1/insurance/premium', {
        ncb_years: formData.ncb_years,
        vehicle_make: formData.vehicle_make,
        vehicle_model: formData.vehicle_model,
        vehicle_year: formData.vehicle_year,
        engine_size_cc: formData.engine_size_cc,
      });
      setPremium(response.data.premium);
    } catch (error) {
      console.error('Error calculating premium:', error);
    }
  };

  return (
    <section className='grid grid-cols-12 gap-8'>
      <div className='col-span-8 bg-surface-container-lowest p-10 rounded-xl shadow-[12px_24px_48px_rgba(13,28,46,0.04)]'>
        <h3 className='font-manrope font-bold text-xl mb-8 flex items-center gap-2'>
          <span className='material-symbols-outlined text-primary' data-icon='directions_car'>directions_car</span>
          Vehicle Specifications
        </h3>
        <div className='grid grid-cols-3 gap-x-12 gap-y-10'>
          <div className='relative'>
            <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-2'>Vehicle Make</label>
            <input className='w-full bg-transparent border-0 border-b-2 border-outline-variant/20 focus:border-primary focus:ring-0 px-0 py-2 text-lg font-medium transition-colors' type='text' name='vehicle_make' value={formData.vehicle_make} onChange={handleInputChange} />
          </div>
          <div className='relative'>
            <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-2'>Model</label>
            <input className='w-full bg-transparent border-0 border-b-2 border-outline-variant/20 focus:border-primary focus:ring-0 px-0 py-2 text-lg font-medium transition-colors' type='text' name='vehicle_model' value={formData.vehicle_model} onChange={handleInputChange} />
          </div>
          <div className='relative'>
            <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-2'>Year</label>
            <input className='w-full bg-transparent border-0 border-b-2 border-outline-variant/20 focus:border-primary focus:ring-0 px-0 py-2 text-lg font-medium transition-colors' type='number' name='vehicle_year' value={formData.vehicle_year} onChange={handleInputChange} />
          </div>
          <div className='relative'>
            <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-2'>VIN</label>
            <input className='w-full bg-transparent border-0 border-b-2 border-outline-variant/20 focus:border-primary focus:ring-0 px-0 py-2 text-lg font-medium transition-colors' placeholder='W1KZF8EB...' type='text' name='vin' value={formData.vin} onChange={handleInputChange} />
          </div>
          <div className='relative'>
            <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-2'>Engine Size (cc)</label>
            <input className='w-full bg-transparent border-0 border-b-2 border-outline-variant/20 focus:border-primary focus:ring-0 px-0 py-2 text-lg font-medium transition-colors' type='number' name='engine_size_cc' value={formData.engine_size_cc} onChange={handleInputChange} />
          </div>
          <div className='relative'>
            <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-2'>NCB Years</label>
            <select className='w-full bg-transparent border-0 border-b-2 border-outline-variant/20 focus:border-primary focus:ring-0 px-0 py-2 text-lg font-medium transition-colors appearance-none' onChange={handleNcbChange}>
              <option>0 Years</option>
              <option>1 Year (20%)</option>
              <option>2 Years (30%)</option>
              <option>3 Years (40%)</option>
              <option selected=''>5+ Years (50%)</option>
            </select>
          </div>
        </div>
        <div className='mt-12'>
          <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-4'>Safety & Assistance Features</label>
          <div className='flex flex-wrap gap-3'>
            <button className='px-5 py-2 bg-primary text-on-primary rounded-full text-sm font-medium'>Autonomous Braking</button>
            <button className='px-5 py-2 bg-primary text-on-primary rounded-full text-sm font-medium'>Lane Keep Assist</button>
            <button className='px-5 py-2 bg-surface-container-high text-on-surface-variant rounded-full text-sm font-medium hover:bg-primary-fixed-dim transition-colors'>Adaptive Cruise</button>
            <button className='px-5 py-2 bg-surface-container-high text-on-surface-variant rounded-full text-sm font-medium hover:bg-primary-fixed-dim transition-colors'>360° Cameras</button>
            <button className='px-5 py-2 bg-surface-container-high text-on-surface-variant rounded-full text-sm font-medium hover:bg-primary-fixed-dim transition-colors'>Night Vision</button>
          </div>
        </div>
      </div>
      <div className='col-span-4 flex flex-col gap-8'>
        <div className='flex-1 bg-surface-container-low p-10 rounded-xl flex flex-col justify-center items-center text-center'>
          <div className='w-20 h-20 bg-primary-fixed rounded-full flex items-center justify-center mb-6'>
            <span className='material-symbols-outlined text-primary text-4xl' data-icon='analytics'>analytics</span>
          </div>
          <h3 className='font-manrope font-bold text-2xl text-primary mb-3'>Refine Valuation</h3>
          <p className='text-secondary mb-8 px-4'>Our algorithm calculates real-time risk parity based on 48 unique vehicle vectors.</p>
          <button className='w-full py-5 premium-gradient text-tertiary-fixed font-semibold text-lg rounded-md shadow-xl hover:scale-[1.02] transition-transform flex items-center justify-center gap-3' onClick={calculatePremium}>
            <span className='material-symbols-outlined' data-icon='calculate'>calculate</span>
            Calculate Premium
          </button>
        </div>
      </div>
      <div className='col-span-7 premium-gradient rounded-xl p-12 text-white flex flex-col justify-between shadow-2xl relative'>
        <div className='relative z-10'>
          <span className='text-primary-fixed uppercase tracking-widest text-xs font-bold opacity-80'>Estimated Annual Premium</span>
          <div className='mt-4 flex items-baseline gap-2'>
            <span className='font-manrope font-semibold text-3xl text-primary-fixed-dim'>$</span>
            <span className='font-manrope font-extrabold text-8xl tracking-tight leading-none'>{premium.toFixed(2)}</span>
          </div>
        </div>
        <div className='mt-16 flex justify-between items-center relative z-10'>
          <div className='flex items-center gap-6'>
            <div className='flex flex-col'>
              <span className='text-xs text-primary-fixed-dim uppercase font-bold tracking-wider'>Valid Until</span>
              <span className='font-medium text-lg'>Oct 31, 2024</span>
            </div>
            <div className='w-px h-10 bg-primary-fixed/20'></div>
            <div className='flex flex-col'>
              <span className='text-xs text-primary-fixed-dim uppercase font-bold tracking-wider'>Risk Profile</span>
              <span className='font-medium text-lg text-tertiary-fixed'>Ultra Low</span>
            </div>
          </div>
          <div className='flex gap-3'>
            <button className='p-3 rounded-lg border border-primary-fixed/30 hover:bg-white/10 transition-colors'>
              <span className='material-symbols-outlined' data-icon='share'>share</span>
            </button>
            <button className='p-3 rounded-lg border border-primary-fixed/30 hover:bg-white/10 transition-colors'>
              <span className='material-symbols-outlined' data-icon='download'>download</span>
            </button>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Calculator;
''