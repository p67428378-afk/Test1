import React from 'react';
import Header from '../components/layout/Header';
import Footer from '../components/layout/Footer';
import CalculatorCard from '../components/insurance/CalculatorCard';

const PremiumCalculatorPage = () => {
    return (
        <>
            <Header />
            <main className='flex-grow flex flex-col items-center justify-center p-8 bg-surface-container-low'>
                <div className='text-center mb-10 max-w-2xl'>
                    <h1 className='text-4xl font-extrabold tracking-tight text-on-surface mb-3'>Vehicle Insurance Premium Calculator</h1>
                    <p className='text-on-surface-variant font-medium opacity-80'>Precision-engineered actuarial estimates for your premium vehicle assets.</p>
                </div>
                <div className='w-full max-w-lg'>
                    <CalculatorCard />
                    <div className='mt-12 rounded-xl overflow-hidden shadow-wash h-48 relative'>
                        <img className='w-full h-full object-cover' alt='luxury sports car tail light in a dark premium showroom with sleek reflections and moody dramatic lighting' src='https://lh3.googleusercontent.com/aida-public/AB6AXuA8H35JhViOzJ0TUlcPiE7SMRDTfQSgF238zKjcI9YDKiXXkRQizdN9eDHnhaSt01tw8vhk5fd5J7D9897YOJmieQtRnAtInjVLdPddtDP5KoVexGTYbVL0MSgXectB_oH5N5WQZMuZtZQtzoa-lA2I3iwYrjcN6ww1Ml02-Bd5bWj5SvPv3Cf6sJQnVjotTg9WfVqq7zRmGA_4-xUB_CSaDBB4U3FZJD6MYtnfjVxEdvJDouXouE397gyfXy_P9fFZr9S0WMK0SO0' />
                        <div className='absolute inset-0 bg-gradient-to-t from-on-surface/60 to-transparent flex items-end p-6'>
                            <p className='text-white text-sm font-medium'>Protecting what matters with actuarial precision.</p>
                        </div>
                    </div>
                </div>
            </main>
            <Footer />
        </>
    );
};

export default PremiumCalculatorPage;
