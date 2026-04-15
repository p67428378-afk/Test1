import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [premium, setPremium] = useState(null);
  const [formData, setFormData] = useState({
    ncb_level: '0_years',
    vehicle_make: 'Mercedes-Benz',
    vehicle_model: 'S-Class',
    vehicle_year: 2024,
    vehicle_type: 'sedan',
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleCalculate = async () => {
    try {
      const response = await axios.post('/api/v1/premium-calculator', formData);
      setPremium(response.data.calculated_premium);
    } catch (error) {
      console.error('Error calculating premium:', error);
    }
  };

  return (
    <div className='bg-surface font-body text-on-surface min-h-screen pb-32'>
      <header className='bg-[#f9f9ff]/70 backdrop-blur-md text-[#00488d] font-["Manrope"] font-bold text-lg tracking-tight docked full-width top-0 sticky z-50 flex justify-between items-center px-6 py-4 w-full'>
        <div className='flex items-center gap-4'>
          <span className='material-symbols-outlined text-[#00488d]'>menu</span>
          <span className='text-xl font-black text-[#00488d]'>The Sovereign Architect</span>
        </div>
        <div className='w-8 h-8 rounded-full bg-surface-container-high flex items-center justify-center overflow-hidden border border-outline-variant/15'>
          <img
            alt='User Profile'
            src='https://lh3.googleusercontent.com/aida-public/AB6AXuD1lrBz5IDazGTTKvV30LbtdJkONDd6Csp4riwbGcN9YxLXAVSqhvta8MXsw4e2Xwonmkxo3ksFl6sz52GTjDC_-utUqboWP1pXZ8ClAvgGAPWjXH4OSKFgXRTnE3ogJK49Rj5lg_ZKfJp6NwdDYxQdD5ewQwROR4zmqrdsixxgJklVXnsuOWLeDE71Yu59GLpbGfGm_irM43DX5VAKcyq4-yx7Ne3y840_wphqGReEvkxavNP2swG_mSvihliB6TYjkXsfMwrfy8A'
          />
        </div>
      </header>
      <main className='px-6 pt-8 max-w-lg mx-auto'>
        <section className='mb-10'>
          <div className='w-12 h-1 bg-primary-container mb-6'></div>
          <h1 className='font-headline font-extrabold text-4xl text-primary leading-tight tracking-tighter mb-4'>
            Premium
            <br />
            Precision
          </h1>
          <p className='text-on-surface-variant font-medium max-w-[80%]'>
            Calculate your vehicle's protection architecture with institutional-grade accuracy.
          </p>
        </section>
        <div className='w-full h-1 bg-surface-container-high rounded-full mb-10 overflow-hidden'>
          <div className='w-1/3 h-full bg-primary-container'></div>
        </div>
        <div className='space-y-8'>
          <div className='bg-surface-container-lowest p-6 rounded-xl border border-outline-variant/15 editorial-shadow'>
            <div className='space-y-6'>
              <div>
                <label className='block font-label text-[11px] font-bold uppercase tracking-widest text-on-surface-variant mb-2'>
                  Vehicle Make
                </label>
                <select
                  name='vehicle_make'
                  value={formData.vehicle_make}
                  onChange={handleInputChange}
                  className='w-full bg-surface-container-high border-none rounded-lg p-4 font-body text-on-surface focus:ring-2 focus:ring-surface-tint focus:bg-surface-container-lowest transition-all appearance-none'
                >
                  <option>Select Manufacturer</option>
                  <option>Mercedes-Benz</option>
                  <option>BMW</option>
                  <option>Audi</option>
                  <option>Porsche</option>
                </select>
              </div>
              <div>
                <label className='block font-label text-[11px] font-bold uppercase tracking-widest text-on-surface-variant mb-2'>
                  Model Designation
                </label>
                <input
                  name='vehicle_model'
                  value={formData.vehicle_model}
                  onChange={handleInputChange}
                  className='w-full bg-surface-container-high border-none rounded-lg p-4 font-body text-on-surface focus:ring-2 focus:ring-surface-tint focus:bg-surface-container-lowest transition-all'
                  placeholder='e.g. S-Class'
                  type='text'
                />
              </div>
              <div className='grid grid-cols-2 gap-4'>
                <div>
                  <label className='block font-label text-[11px] font-bold uppercase tracking-widest text-on-surface-variant mb-2'>
                    Year
                  </label>
                  <input
                    name='vehicle_year'
                    value={formData.vehicle_year}
                    onChange={handleInputChange}
                    className='w-full bg-surface-container-high border-none rounded-lg p-4 font-body text-on-surface focus:ring-2 focus:ring-surface-tint focus:bg-surface-container-lowest transition-all'
                    placeholder='2024'
                    type='number'
                  />
                </div>
                <div>
                  <label className='block font-label text-[11px] font-bold uppercase tracking-widest text-on-surface-variant mb-2'>
                    Usage
                  </label>
                  <select
                    name='vehicle_type'
                    value={formData.vehicle_type}
                    onChange={handleInputChange}
                    className='w-full bg-surface-container-high border-none rounded-lg p-4 font-body text-on-surface focus:ring-2 focus:ring-surface-tint focus:bg-surface-container-lowest transition-all appearance-none'
                  >
                    <option value='sedan'>Executive</option>
                    <option value='suv'>Personal</option>
                    <option value='hatchback'>Leisure</option>
                  </select>
                </div>
              </div>
            </div>
          </div>
          <div className='flex flex-wrap gap-2'>
            <span className='bg-secondary-container text-on-secondary-container px-3 py-1.5 rounded-full text-[11px] font-bold uppercase tracking-wider flex items-center gap-1.5'>
              <span className='material-symbols-outlined text-[14px]'>verified</span> Safe Driver Discount
            </span>
            <span className='bg-secondary-container text-on-secondary-container px-3 py-1.5 rounded-full text-[11px] font-bold uppercase tracking-wider flex items-center gap-1.5'>
              <span className='material-symbols-outlined text-[14px]'>electric_car</span> EV Incentive
            </span>
          </div>
          <button
            onClick={handleCalculate}
            className='w-full bg-tertiary hover:opacity-90 text-white font-headline font-bold py-5 rounded-xl transition-all active:scale-[0.98] flex items-center justify-center gap-3 shadow-lg shadow-tertiary/20'
          >
            <span className='material-symbols-outlined'>calculate</span>
            Calculate Premium
          </button>
        </div>
        {premium !== null && (
          <section className='mt-16 mb-12'>
            <div className='bg-surface-container-low p-8 rounded-2xl relative overflow-hidden'>
              <div className='absolute top-0 right-0 p-4 opacity-5'>
                <span className='material-symbols-outlined text-[120px]'>shield</span>
              </div>
              <div className='relative z-10'>
                <h3 className='font-label text-[11px] font-bold uppercase tracking-[0.2em] text-primary mb-6'>
                  Estimated Annual Investment
                </h3>
                <div className='flex items-baseline gap-2 mb-2'>
                  <span className='font-headline font-extrabold text-5xl text-on-surface tracking-tighter'>
                    ${premium.toFixed(2)}
                  </span>
                </div>
                <p className='text-sm font-medium text-on-surface-variant/80 mb-8 max-w-[200px]'>
                  Structured coverage based on current market valuations and risk assessment.
                </p>
                <div className='grid grid-cols-1 gap-3'>
                  <div className='bg-surface-container-lowest p-4 rounded-lg flex justify-between items-center border border-outline-variant/10'>
                    <span className='text-xs font-bold uppercase tracking-wider text-on-surface-variant'>
                      Monthly Plan
                    </span>
                    <span className='font-headline font-bold text-primary'>${(premium / 12).toFixed(2)}</span>
                  </div>
                  <div className='bg-surface-container-lowest p-4 rounded-lg flex justify-between items-center border border-outline-variant/10'>
                    <span className='text-xs font-bold uppercase tracking-wider text-on-surface-variant'>
                      Liability Limit
                    </span>
                    <span className='font-headline font-bold text-primary'>$1M</span>
                  </div>
                </div>
              </div>
            </div>
          </section>
        )}
      </main>
      <nav className='fixed bottom-0 left-0 w-full z-50 flex justify-around items-center pt-2 pb-6 px-4 bg-white border-t border-[#c2c6d4]/15 shadow-[0_-4px_32px_rgba(25,28,33,0.06)]'>
        <div className='flex flex-col items-center justify-center bg-[#d6e3ff] text-[#00488d] rounded-2xl px-5 py-1.5 transition-all duration-150 active:scale-95'>
          <span className='material-symbols-outlined'>calculate</span>
          <span className='font-["Inter"] text-[11px] font-semibold uppercase tracking-wider'>Calculate</span>
        </div>
        <div className='flex flex-col items-center justify-center text-[#424752] px-5 py-1.5 hover:text-[#005fb8] transition-all'>
          <span className='material-symbols-outlined'>verified_user</span>
          <span className='font-["Inter"] text-[11px] font-semibold uppercase tracking-wider'>Policies</span>
        </div>
        <div className='flex flex-col items-center justify-center text-[#424752] px-5 py-1.5 hover:text-[#005fb8] transition-all'>
          <span className='material-symbols-outlined'>assignment_late</span>
          <span className='font-["Inter"] text-[11px] font-semibold uppercase tracking-wider'>Claims</span>
        </div>
        <div className='flex flex-col items-center justify-center text-[#424752] px-5 py-1.5 hover:text-[#005fb8] transition-all'>
          <span className='material-symbols-outlined'>person</span>
          <span className='font-["Inter"] text-[11px] font-semibold uppercase tracking-wider'>Account</span>
        </div>
      </nav>
    </div>
  );
};

export default App;
