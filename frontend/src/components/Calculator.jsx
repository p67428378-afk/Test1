import React, { useState } from 'react';
import axios from 'axios';

const Calculator = () => {
  const [vehicleMake, setVehicleMake] = useState('Mercedes-Benz');
  const [vehicleModel, setVehicleModel] = useState('EQS Sedan');
  const [vehicleYear, setVehicleYear] = useState(2024);
  const [vin, setVin] = useState('');
  const [engineSize, setEngineSize] = useState(2996);
  const [ncbYears, setNcbYears] = useState('5+ Years (50%)');
  const [premium, setPremium] = useState(1248.50);

  const handleCalculatePremium = async () => {
    const ncbMap = {
      '0 Years': 0,
      '1 Year (20%)': 1,
      '2 Years (30%)': 2,
      '3 Years (40%)': 3,
      '5+ Years (50%)': 5,
    };

    try {
      const response = await axios.post('/api/v1/insurance/premium', {
        vehicle_make: vehicleMake,
        vehicle_model: vehicleModel,
        vehicle_year: parseInt(vehicleYear, 10),
        engine_size_cc: parseInt(engineSize, 10),
        ncb_years: ncbMap[ncbYears],
      });
      setPremium(response.data.premium);
    } catch (error) {
      console.error('Error calculating premium:', error);
      // You might want to show an error message to the user
    }
  };

  return (
    <div className='p-12 space-y-12 max-w-[1600px] mx-auto'>
      <section className='flex justify-between items-end'>
        <div>
          <h2 className='font-manrope font-extrabold text-4xl tracking-tight text-primary'>Premium Calculator</h2>
          <p className='text-secondary mt-2 text-lg'>Detailed valuation for commercial and private vehicle assets.</p>
        </div>
        <div className='flex gap-4'>
          <div className='flex items-center gap-2 px-4 py-2 bg-surface-container-high rounded-full text-on-surface-variant text-sm font-medium'>
            <span className='w-2 h-2 rounded-full bg-on-tertiary-container'></span>
            Live Market Rates
          </div>
        </div>
      </section>

      <section className='grid grid-cols-12 gap-8'>
        <div className='col-span-8 bg-surface-container-lowest p-10 rounded-xl shadow-[12px_24px_48px_rgba(13,28,46,0.04)]'>
          <h3 className='font-manrope font-bold text-xl mb-8 flex items-center gap-2'>
            <span className='material-symbols-outlined text-primary' data-icon='directions_car'>directions_car</span>
            Vehicle Specifications
          </h3>
          <div className='grid grid-cols-3 gap-x-12 gap-y-10'>
            <div className='relative'>
              <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-2'>Vehicle Make</label>
              <input className='w-full bg-transparent border-0 border-b-2 border-outline-variant/20 focus:border-primary focus:ring-0 px-0 py-2 text-lg font-medium transition-colors' type='text' value={vehicleMake} onChange={(e) => setVehicleMake(e.target.value)} />
            </div>
            <div className='relative'>
              <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-2'>Model</label>
              <input className='w-full bg-transparent border-0 border-b-2 border-outline-variant/20 focus:border-primary focus:ring-0 px-0 py-2 text-lg font-medium transition-colors' type='text' value={vehicleModel} onChange={(e) => setVehicleModel(e.target.value)} />
            </div>
            <div className='relative'>
              <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-2'>Year</label>
              <input className='w-full bg-transparent border-0 border-b-2 border-outline-variant/20 focus:border-primary focus:ring-0 px-0 py-2 text-lg font-medium transition-colors' type='number' value={vehicleYear} onChange={(e) => setVehicleYear(e.target.value)} />
            </div>
            <div className='relative'>
              <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-2'>VIN</label>
              <input className='w-full bg-transparent border-0 border-b-2 border-outline-variant/20 focus:border-primary focus:ring-0 px-0 py-2 text-lg font-medium transition-colors' placeholder='W1KZF8EB...' type='text' value={vin} onChange={(e) => setVin(e.target.value)} />
            </div>
            <div className='relative'>
              <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-2'>Engine Size (cc)</label>
              <input className='w-full bg-transparent border-0 border-b-2 border-outline-variant/20 focus:border-primary focus:ring-0 px-0 py-2 text-lg font-medium transition-colors' type='number' value={engineSize} onChange={(e) => setEngineSize(e.target.value)} />
            </div>
            <div className='relative'>
              <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-2'>NCB Years</label>
              <select className='w-full bg-transparent border-0 border-b-2 border-outline-variant/20 focus:border-primary focus:ring-0 px-0 py-2 text-lg font-medium transition-colors appearance-none' value={ncbYears} onChange={(e) => setNcbYears(e.target.value)}>
                <option>0 Years</option>
                <option>1 Year (20%)</option>
                <option>2 Years (30%)</option>
                <option>3 Years (40%)</option>
                <option>5+ Years (50%)</option>
              </select>
            </div>
          </div>
          <div className='mt-12'>
            <label className='block text-xs font-semibold text-primary uppercase tracking-widest mb-4'>Safety &amp; Assistance Features</label>
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
            <button onClick={handleCalculatePremium} className='w-full py-5 premium-gradient text-tertiary-fixed font-semibold text-lg rounded-md shadow-xl hover:scale-[1.02] transition-transform flex items-center justify-center gap-3'>
              <span className='material-symbols-outlined' data-icon='calculate'>calculate</span>
              Calculate Premium
            </button>
          </div>
        </div>
      </section>

      <section className='grid grid-cols-12 gap-12 pt-8'>
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

        <div className='col-span-5 space-y-8'>
          <h4 className='font-manrope font-bold text-xl text-primary'>Premium Breakdown</h4>
          <div className='space-y-6'>
            <div className='flex justify-between items-end group'>
              <div>
                <p className='text-sm font-semibold text-primary uppercase tracking-widest'>Base Underwriting Rate</p>
                <p className='text-xs text-secondary mt-1'>Standard market entry for vehicle class</p>
              </div>
              <p className='font-manrope font-bold text-xl'>$500.00</p>
            </div>
            <div className='h-px bg-surface-container'></div>
            <div className='flex justify-between items-end group'>
              <div>
                <p className='text-sm font-semibold text-on-tertiary-container uppercase tracking-widest'>NCB Discount Applied</p>
                <p className='text-xs text-secondary mt-1'>5+ Years Claim Free History</p>
              </div>
              <p className='font-manrope font-bold text-xl text-on-tertiary-container'>- 50%</p>
            </div>
            <div className='h-px bg-surface-container'></div>
            <div className='flex justify-between items-end group'>
              <div>
                <p className='text-sm font-semibold text-primary uppercase tracking-widest'>Vehicle Asset Multiplier</p>
                <p className='text-xs text-secondary mt-1'>Luxury Electric Performance Adjustment</p>
              </div>
              <p className='font-manrope font-bold text-xl'>x 1.45</p>
            </div>
            <div className='h-px bg-surface-container'></div>
            <div className='flex justify-between items-end group'>
              <div>
                <p className='text-sm font-semibold text-on-tertiary-container uppercase tracking-widest'>Safety Feature Credit</p>
                <p className='text-xs text-secondary mt-1'>ADAS Level 3 Implementation</p>
              </div>
              <p className='font-manrope font-bold text-xl text-on-tertiary-container'>- $125.00</p>
            </div>
          </div>
          <div className='p-6 bg-surface-container-high rounded-lg mt-4 flex items-center gap-4'>
            <span className='material-symbols-outlined text-primary' data-icon='info'>info</span>
            <p className='text-sm text-on-surface-variant italic'>Final calculation incorporates local state taxes and regional luxury surcharges where applicable.</p>
          </div>
        </div>
      </section>

      <section className='relative h-64 rounded-xl overflow-hidden shadow-lg group'>
        <div className='absolute inset-0 bg-black/40 z-10 group-hover:bg-black/20 transition-colors duration-500'></div>
        <img className='w-full h-full object-cover group-hover:scale-105 transition-transform duration-700' alt='Modern electric vehicle interior with focus on digital dashboard and premium leather finishes, morning sunlight' src='https://lh3.googleusercontent.com/aida-public/AB6AXuAaMldeXiIuybegiFq8FJom7zkoaoBl6Q9eLvIUk9tSxgSKvSciUxpZnoccfojzlCdZCyzf-CPNnta8BT9KrLPl_9W9NsIOQO4nhphf5FofvZpVC1XNUiJyO5yVTjS40YccijHhZQDZZ_xj_q53x0EVXDquaRqNH5ekBDg3J3c9h0FlgwWuxTIXV5-Kn5WO2ZcY939Shwr25zee3I-RS2--AoeD2K-LZShzpGNt-TXzZMsLGV6Ws723gr9QYsPApvE8jGhuDT2qYls'/>
        <div className='absolute bottom-8 left-8 z-20'>
          <h4 className='text-white font-manrope font-bold text-2xl'>Insuring the Future of Mobility</h4>
          <p className='text-white/80 mt-1'>Learn more about our dedicated EV and Autonomous coverage plans.</p>
        </div>
      </section>
    </div>
  );
};

export default Calculator;
