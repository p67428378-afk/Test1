import React, { useState } from 'react';
import { calculatePremium } from '../../services/insuranceApi';

const CalculatorCard = () => {
    const [policyHolderName, setPolicyHolderName] = useState('Jane Doe');
    const [vehicleType, setVehicleType] = useState('Sedan');
    const [ncbYears, setNcbYears] = useState(3);
    const [riskFactor, setRiskFactor] = useState(1.2);
    const [result, setResult] = useState(null);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        setResult(null);

        try {
            const data = await calculatePremium({
                policy_holder_name: policyHolderName,
                vehicle_type: vehicleType,
                ncb_years: parseInt(ncbYears, 10),
                vehicle_risk_factor: parseFloat(riskFactor)
            });
            setResult(data);
        } catch (err) {
            setError(err.detail || 'An unexpected error occurred.');
        }
        setLoading(false);
    };

    return (
        <div className='bg-surface-container-lowest p-6 rounded-lg shadow-wash border border-outline-variant/20'>
            <div className='mb-8'>
                <h2 className='text-xl font-bold text-on-surface tracking-tight'>Calculate Your Premium</h2>
                <div className='w-12 h-1 bg-primary mt-2 rounded-full'></div>
            </div>
            <form className='flex flex-col gap-4' onSubmit={handleSubmit}>
                <div className='flex flex-col gap-1.5'>
                    <label className='text-[10px] font-bold tracking-widest text-on-surface-variant uppercase'>Policy Holder Name</label>
                    <input 
                        className='w-full h-12 px-4 bg-surface-container-highest border-none rounded-[6px] text-on-surface placeholder:text-on-surface-variant/40 focus:ring-2 focus:ring-primary focus:bg-surface-container-lowest transition-all' 
                        placeholder='Enter full name' 
                        type='text' 
                        value={policyHolderName}
                        onChange={(e) => setPolicyHolderName(e.target.value)}
                    />
                </div>
                <div className='flex flex-col gap-1.5'>
                    <label className='text-[10px] font-bold tracking-widest text-on-surface-variant uppercase'>Vehicle Type</label>
                    <div className='relative'>
                        <select 
                            className='w-full h-12 px-4 bg-surface-container-highest border-none rounded-[6px] text-on-surface appearance-none focus:ring-2 focus:ring-primary focus:bg-surface-container-lowest transition-all'
                            value={vehicleType}
                            onChange={(e) => setVehicleType(e.target.value)}
                        >
                            <option>Sedan</option>
                            <option>SUV</option>
                            <option>Hatchback</option>
                            <option>Sports Car</option>
                        </select>
                        <span className='material-symbols-outlined absolute right-4 top-1/2 -translate-y-1/2 pointer-events-none text-on-surface-variant'>expand_more</span>
                    </div>
                </div>
                <div className='grid grid-cols-2 gap-4'>
                    <div className='flex flex-col gap-1.5'>
                        <label className='text-[10px] font-bold tracking-widest text-on-surface-variant uppercase'>NCB (Years 0-10)</label>
                        <input 
                            className='w-full h-12 px-4 bg-surface-container-highest border-none rounded-[6px] text-on-surface focus:ring-2 focus:ring-primary focus:bg-surface-container-lowest transition-all' 
                            max='10' 
                            min='0' 
                            placeholder='e.g., 3' 
                            type='number' 
                            value={ncbYears}
                            onChange={(e) => setNcbYears(e.target.value)}
                        />
                    </div>
                    <div className='flex flex-col gap-1.5'>
                        <label className='text-[10px] font-bold tracking-widest text-on-surface-variant uppercase'>Risk Factor (0.8-1.6)</label>
                        <input 
                            className='w-full h-12 px-4 bg-surface-container-highest border-none rounded-[6px] text-on-surface focus:ring-2 focus:ring-primary focus:bg-surface-container-lowest transition-all' 
                            max='1.6' 
                            min='0.8' 
                            placeholder='e.g., 1.2' 
                            step='0.1' 
                            type='number' 
                            value={riskFactor}
                            onChange={(e) => setRiskFactor(e.target.value)}
                        />
                    </div>
                </div>
                <button 
                    className='mt-4 w-full h-14 bg-gradient-to-br from-primary to-primary-container text-on-primary font-bold rounded-lg shadow-lg shadow-primary/20 hover:scale-[1.02] active:scale-[0.98] transition-all' 
                    type='submit'
                    disabled={loading}
                >
                    {loading ? 'Calculating...' : 'Calculate Premium'}
                </button>
            </form>
            {error && <div className="mt-4 text-red-500">{error}</div>}
            {result && (
                <div className='mt-8 pt-8 border-t border-outline-variant/10'>
                    <div className='flex items-center justify-between p-4 bg-surface-container-low rounded-lg border-l-4 border-primary'>
                        <div className='flex flex-col'>
                            <span className='text-[10px] font-bold tracking-widest text-on-surface-variant uppercase mb-1'>Estimated Quote</span>
                            <span className='text-3xl font-extrabold text-[#10B981] tracking-tighter'>${result.calculated_premium.toFixed(2)}</span>
                        </div>
                        <div className='text-right'>
                            <span className='text-[10px] font-bold tracking-widest text-on-surface-variant uppercase mb-1'>Policy ID</span>
                            <span className='block font-mono text-sm text-on-surface font-semibold'>{result.policy_id}</span>
                        </div>
                    </div>
                    <div className='mt-4 flex items-center gap-2 text-on-surface-variant text-xs font-medium'>
                        <span className='material-symbols-outlined text-sm' style={{fontVariationSettings: '\'FILL\' 1'}}>info</span>
                        This is an editorial estimate based on provided risk factors.
                    </div>
                </div>
            )}
        </div>
    );
};

export default CalculatorCard;
