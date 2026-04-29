
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [ncb, setNcb] = useState(3);
  const [premium, setPremium] = useState(1240.00);

  const handleNcbChange = (e) => {
    setNcb(e.target.value);
  };

  const calculatePremium = async () => {
    try {
      const response = await axios.post('/api/v1/insurance/premium/calculate', {
        vehicle_details: { value: 50000, multiplier: 1.2 },
        ncb_tier: ncb / 10,
      });
      setPremium(response.data.calculated_premium);
    } catch (error) {
      console.error('Error calculating premium:', error);
    }
  };

  return (
    <div className="bg-background font-body-md text-on-surface">
      <header className="bg-white dark:bg-slate-900 text-slate-900 dark:text-slate-50 font-inter antialiased shadow-sm border-b border-slate-200 dark:border-slate-800 flex justify-between items-center h-16 px-6 w-full sticky top-0 z-50">
        <div className="flex items-center gap-8">
          <span className="text-xl font-bold text-slate-900 dark:text-white tracking-tight">InsureCalc Pro</span>
          <nav className="hidden md:flex gap-6 items-center h-full">
            <a className="text-teal-600 dark:text-teal-400 font-semibold border-b-2 border-teal-600 h-full flex items-center px-1">Dashboard</a>
            <a className="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 h-full flex items-center px-1 transition-colors cursor-pointer">Policies</a>
            <a className="text-slate-500 dark:text-slate-400 hover:text-slate-900 dark:hover:text-slate-200 h-full flex items-center px-1 transition-colors cursor-pointer">Claims</a>
          </nav>
        </div>
        <div className="flex items-center gap-4">
          <button className="p-2 hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors rounded-full cursor-pointer">
            <span className="material-symbols-outlined" data-icon="notifications">notifications</span>
          </button>
          <button className="p-2 hover:bg-slate-50 dark:hover:bg-slate-800 transition-colors rounded-full cursor-pointer">
            <span className="material-symbols-outlined" data-icon="help_outline">help_outline</span>
          </button>
          <div className="h-8 w-8 rounded-full overflow-hidden border border-slate-200">
            <img alt="User profile" src="https://lh3.googleusercontent.com/aida-public/AB6AXuDxfvOQaJ3BBx3qXJHD96nwwvz45dtfT4kbJd44Lr52JMOXEuM6F4pRckxT_arNq18TipBXyKTxMeN15XyRasvuRHiGaalz7t0KbUk6phGhPi-ZRpe2Nx7knIkq79o_ho4RBlvlOZIMZplOu5XnYF8SHQbH1rb6HbxMaML56EW8CQOMiDB6Uw6cmrnn5vIsO6hcUYuP6XghozSx0-jw6WOtvTA3Y4WlHSIV97ovV9ElYtqkiRMem0D-JsnwmbHlBSsxWU4a54Mfh3M" />
          </div>
        </div>
      </header>
      <div className="flex min-h-[calc(100vh-64px)]">
        <aside className="bg-slate-50 dark:bg-slate-950 text-slate-900 dark:text-slate-50 font-inter text-sm font-medium h-screen w-64 border-r border-slate-200 dark:border-slate-800 hidden lg:flex flex-col gap-4 p-4 sticky left-0 top-16 no-shadow">
          <div className="mb-6 px-2">
            <h2 className="text-lg font-black text-slate-900 dark:text-white">Premium Suite</h2>
            <p className="text-xs text-slate-500">Enterprise Tier</p>
          </div>
          <nav className="flex flex-col gap-1">
            <a className="flex items-center gap-3 px-3 py-2 bg-slate-200 dark:bg-slate-800 text-teal-600 dark:text-teal-400 rounded-lg active:scale-95 transition-all">
              <span className="material-symbols-outlined" data-icon="dashboard">dashboard</span>
              <span>Dashboard</span>
            </a>
            <a className="flex items-center gap-3 px-3 py-2 text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-900 rounded-lg hover:translate-x-1 transition-all active:scale-95">
              <span className="material-symbols-outlined" data-icon="calculate">calculate</span>
              <span>New Quote</span>
            </a>
            <a className="flex items-center gap-3 px-3 py-2 text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-900 rounded-lg hover:translate-x-1 transition-all active:scale-95">
              <span className="material-symbols-outlined" data-icon="history">history</span>
              <span>Policy History</span>
            </a>
            <a className="flex items-center gap-3 px-3 py-2 text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-900 rounded-lg hover:translate-x-1 transition-all active:scale-95">
              <span className="material-symbols-outlined" data-icon="description">description</span>
              <span>Claims</span>
            </a>
            <a className="flex items-center gap-3 px-3 py-2 text-slate-600 dark:text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-900 rounded-lg hover:translate-x-1 transition-all active:scale-95">
              <span className="material-symbols-outlined" data-icon="settings">settings</span>
              <span>Settings</span>
            </a>
          </nav>
          <div className="mt-auto p-4 bg-teal-50 dark:bg-teal-900/20 rounded-xl border border-teal-100 dark:border-teal-800">
            <p className="text-xs text-teal-800 dark:text-teal-200 mb-2 font-semibold">Need help?</p>
            <button className="w-full py-2 bg-teal-600 text-white rounded-lg text-xs font-bold hover:bg-teal-700 transition-colors">Contact Support</button>
          </div>
        </aside>
        <main className="flex-1 p-gutter lg:p-section-padding max-w-[1600px] mx-auto w-full">
          <div className="mb-8">
            <div className="flex items-center gap-4 mb-2">
              <div className="flex items-center justify-center w-8 h-8 rounded-full bg-primary text-on-primary font-bold text-xs">1</div>
              <div className="h-1 w-24 bg-primary rounded-full"></div>
              <div className="flex items-center justify-center w-8 h-8 rounded-full bg-surface-container-highest text-on-surface-variant font-bold text-xs">2</div>
              <div className="h-1 w-24 bg-surface-container-highest rounded-full"></div>
              <div className="flex items-center justify-center w-8 h-8 rounded-full bg-surface-container-highest text-on-surface-variant font-bold text-xs">3</div>
            </div>
            <h1 className="font-headline-lg text-headline-lg text-on-background">Vehicle Premium Calculator</h1>
            <p className="font-body-lg text-body-lg text-on-surface-variant max-w-2xl">Configure your vehicle details and driving history to generate a precise insurance quote based on actuarial models.</p>
          </div>
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-gutter">
            <div className="lg:col-span-7 space-y-gutter">
              <section className="bg-surface-container-lowest p-card-padding rounded-xl border border-slate-200 shadow-[0px_10px_25px_rgba(15,23,42,0.05)]">
                <div className="flex items-center gap-3 mb-6">
                  <span className="material-symbols-outlined text-secondary" data-icon="directions_car">directions_car</span>
                  <h2 className="font-headline-md text-headline-md">Vehicle Details</h2>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-input-gap">
                  <div className="space-y-base">
                    <label className="font-label-bold text-label-bold text-on-surface-variant block">Make</label>
                    <select className="w-full p-3 border border-outline-variant rounded bg-white focus:ring-2 focus:ring-secondary focus:border-secondary outline-none transition-all">
                      <option>Select Manufacturer</option>
                      <option>Toyota</option>
                      <option>Tesla</option>
                      <option>BMW</option>
                      <option>Audi</option>
                    </select>
                  </div>
                  <div className="space-y-base">
                    <label className="font-label-bold text-label-bold text-on-surface-variant block">Model</label>
                    <input className="w-full p-3 border border-outline-variant rounded bg-white focus:ring-2 focus:ring-secondary focus:border-secondary outline-none transition-all" placeholder="e.g. Model 3" type="text" />
                  </div>
                  <div className="space-y-base">
                    <label className="font-label-bold text-label-bold text-on-surface-variant block">Year of Manufacture</label>
                    <input className="w-full p-3 border border-outline-variant rounded bg-white focus:ring-2 focus:ring-secondary focus:border-secondary outline-none transition-all" placeholder="2024" type="number" />
                  </div>
                  <div className="space-y-base">
                    <label className="font-label-bold text-label-bold text-on-surface-variant block">Vehicle Type</label>
                    <select className="w-full p-3 border border-outline-variant rounded bg-white focus:ring-2 focus:ring-secondary focus:border-secondary outline-none transition-all">
                      <option>Sedan</option>
                      <option>SUV (1.2x Multiplier)</option>
                      <option>Hatchback</option>
                      <option>Luxury Sport</option>
                    </select>
                  </div>
                </div>
                <div className="mt-8">
                  <label className="font-label-bold text-label-bold text-on-surface-variant block mb-4">Safety Features</label>
                  <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <label className="flex items-center gap-3 p-3 border border-outline-variant rounded-lg hover:bg-surface transition-colors cursor-pointer group">
                      <input defaultChecked className="w-5 h-5 rounded border-outline-variant text-secondary focus:ring-secondary" type="checkbox" />
                      <span className="text-label-sm font-label-sm">ABS</span>
                    </label>
                    <label className="flex items-center gap-3 p-3 border border-outline-variant rounded-lg hover:bg-surface transition-colors cursor-pointer group">
                      <input defaultChecked className="w-5 h-5 rounded border-outline-variant text-secondary focus:ring-secondary" type="checkbox" />
                      <span className="text-label-sm font-label-sm">Airbags</span>
                    </label>
                    <label className="flex items-center gap-3 p-3 border border-outline-variant rounded-lg hover:bg-surface transition-colors cursor-pointer group">
                      <input className="w-5 h-5 rounded border-outline-variant text-secondary focus:ring-secondary" type="checkbox" />
                      <span className="text-label-sm font-label-sm">ADAS</span>
                    </label>
                    <label className="flex items-center gap-3 p-3 border border-outline-variant rounded-lg hover:bg-surface transition-colors cursor-pointer group">
                      <input className="w-5 h-5 rounded border-outline-variant text-secondary focus:ring-secondary" type="checkbox" />
                      <span className="text-label-sm font-label-sm">Anti-Theft</span>
                    </label>
                  </div>
                </div>
              </section>
              <section className="bg-surface-container-lowest p-card-padding rounded-xl border border-slate-200 shadow-[0px_10px_25px_rgba(15,23,42,0.05)]">
                <div className="flex items-center gap-3 mb-6">
                  <span className="material-symbols-outlined text-secondary" data-icon="history">history</span>
                  <h2 className="font-headline-md text-headline-md">NCB History</h2>
                </div>
                <div className="space-y-6">
                  <div className="space-y-base">
                    <div className="flex justify-between items-end">
                      <label className="font-label-bold text-label-bold text-on-surface-variant block">Years of claim-free driving</label>
                      <span className="text-secondary font-bold text-lg">{ncb} Years</span>
                    </div>
                    <input className="w-full h-2 bg-surface-container-highest rounded-lg appearance-none cursor-pointer accent-secondary" max="10" min="0" step="1" type="range" value={ncb} onChange={handleNcbChange} />
                    <div className="flex justify-between text-label-sm font-label-sm text-outline">
                      <span>0 Years</span>
                      <span>5 Years</span>
                      <span>10 Years</span>
                    </div>
                  </div>
                  <div className="p-4 bg-secondary-container/20 rounded-lg border border-secondary/10 flex items-start gap-3">
                    <span className="material-symbols-outlined text-secondary text-xl" data-icon="info">info</span>
                    <p className="text-label-sm font-label-sm text-on-secondary-container">Your {ncb}-year No Claim Bonus (NCB) entitles you to a {Math.min(ncb * 10, 50)}% discount on your base premium.</p>
                  </div>
                </div>
              </section>
            </div>
            <div className="lg:col-span-5 space-y-gutter">
              <section className="bg-primary-container text-on-primary rounded-xl p-card-padding shadow-[0px_15px_35px_rgba(0,0,0,0.15)] relative overflow-hidden">
                <div className="absolute -right-12 -top-12 w-48 h-48 bg-secondary/10 rounded-full blur-3xl"></div>
                <div className="relative z-10">
                  <div className="flex justify-between items-center mb-8">
                    <span className="font-label-bold text-label-bold text-on-primary-container uppercase tracking-widest">Annual Premium</span>
                    <div className="bg-white/10 p-1 rounded-full flex gap-1">
                      <button className="px-4 py-1 rounded-full text-xs font-bold bg-white text-primary">Yearly</button>
                      <button className="px-4 py-1 rounded-full text-xs font-bold text-white/60 hover:text-white transition-colors">Monthly</button>
                    </div>
                  </div>
                  <div className="flex items-baseline gap-2 mb-8">
                    <span className="text-display-premium font-display-premium">${premium.toFixed(2)}</span>
                    <span className="text-on-primary-container font-label-bold text-label-bold">/ YEAR</span>
                  </div>
                  <button onClick={calculatePremium} className="w-full py-4 bg-secondary text-white font-bold rounded-lg hover:brightness-110 active:scale-[0.98] transition-all flex items-center justify-center gap-2">
                    <span>Calculate Premium</span>
                    <span className="material-symbols-outlined" data-icon="arrow_forward">arrow_forward</span>
                  </button>
                </div>
              </section>
              <section className="bg-surface-container-lowest p-card-padding rounded-xl border border-slate-200 shadow-[0px_10px_25px_rgba(15,23,42,0.05)]">
                <h3 className="font-label-bold text-label-bold text-on-surface-variant mb-6 uppercase tracking-widest border-b border-slate-100 pb-4">Detailed Breakdown</h3>
                <div className="space-y-4">
                  <div className="flex justify-between items-center group">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 rounded-lg bg-slate-50 flex items-center justify-center text-slate-400 group-hover:bg-slate-100 transition-colors">
                        <span className="material-symbols-outlined" data-icon="payments">payments</span>
                      </div>
                      <div>
                        <p className="text-body-md font-semibold text-on-surface">Base Premium</p>
                        <p className="text-label-sm font-label-sm text-outline">Market Standard Rate</p>
                      </div>
                    </div>
                    <span className="font-bold text-on-surface">$500.00</span>
                  </div>
                  <div className="flex justify-between items-center group">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 rounded-lg bg-slate-50 flex items-center justify-center text-slate-400 group-hover:bg-slate-100 transition-colors">
                        <span className="material-symbols-outlined" data-icon="trending_up">trending_up</span>
                      </div>
                      <div>
                        <p className="text-body-md font-semibold text-on-surface">Vehicle Multiplier</p>
                        <p className="text-label-sm font-label-sm text-outline">SUV Category (1.2x)</p>
                      </div>
                    </div>
                    <span className="font-bold text-error">+$100.00</span>
                  </div>
                  <div className="flex justify-between items-center group">
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 rounded-lg bg-slate-50 flex items-center justify-center text-slate-400 group-hover:bg-slate-100 transition-colors">
                        <span className="material-symbols-outlined" data-icon="redeem">redeem</span>
                      </div>
                      <div>
                        <p className="text-body-md font-semibold text-on-surface">NCB Discount</p>
                        <p className="text-label-sm font-label-sm text-outline">{ncb} Years Claim-Free (-{Math.min(ncb * 10, 50)}%)</p>
                      </div>
                    </div>
                    <span className="font-bold text-secondary">-${(500 * (Math.min(ncb * 10, 50) / 100)).toFixed(2)}</span>
                  </div>
                  <div className="pt-6 mt-4 border-t border-slate-100 flex justify-between items-center">
                    <span className="font-headline-md text-headline-md">Final Total</span>
                    <span className="font-headline-md text-headline-md text-primary">${premium.toFixed(2)}</span>
                  </div>
                </div>
                <div className="mt-8 flex gap-3">
                  <button className="flex-1 py-3 border border-secondary text-secondary font-bold rounded-lg hover:bg-secondary/5 transition-colors text-sm">Save Quote</button>
                  <button className="flex-1 py-3 border border-outline-variant text-outline font-bold rounded-lg hover:bg-slate-50 transition-colors text-sm">Clear Form</button>
                </div>
              </section>
              <div className="relative rounded-xl overflow-hidden h-40 group cursor-pointer">
                <img alt="Car driving on scenic road" className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-700" src="https://lh3.googleusercontent.com/aida-public/AB6AXuAMTHEdHlX7NfH1BijBPQil09p_WL9ZJ_Gnwx5zopKakS522xDHJTFRRhFxuJPezBblpVTeHzqwQGcV32eiSiEuslmav63WVVmfx_VwvsL_FRiJ1A0sJj1bBxu_uNzacaX-BUB7aqHFqXxh-1OevonNmyUF1uTNzlvxDd-0hvq3VfQjaZZlEOYXnB_HHMiUppD1mqdetSAUZNsYugu1yiRgXIvg9clb_v0uRO_4oAzzxcFPSx5SJ2vZXpvIpH417GwOnbVdg9c__GY" />
                <div className="absolute inset-0 bg-gradient-to-t from-primary-container to-transparent flex flex-col justify-end p-6">
                  <h4 className="text-white font-bold">New Policy Holder?</h4>
                  <p className="text-on-primary-container text-xs">Learn how to maximize your savings.</p>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  );
}

export default App;
