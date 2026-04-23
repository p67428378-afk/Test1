import React from 'react';

const Header = () => {
    return (
        <header className='docked w-full top-0 sticky z-50 bg-[#f9f9ff]/85 backdrop-blur-md shadow-wash font-['Inter'] tracking-tight antialiased'>
            <div className='flex justify-between items-center h-16 px-12 max-w-[1920px] mx-auto'>
                <div className='flex items-center gap-8'>
                    <span className='text-xl font-bold tracking-tighter text-[#151c27]'>Precision Ledger</span>
                    <nav className='hidden md:flex gap-6'>
                        <a className='text-[#0058be] border-b-2 border-[#0058be] font-semibold transition-transform active:scale-95' href='#'>Calculator</a>
                        <a className='text-[#151c27]/60 hover:text-[#0058be] hover:bg-[#f0f3ff] transition-colors duration-300 transition-transform active:scale-95' href='#'>Policies</a>
                        <a className='text-[#151c27]/60 hover:text-[#0058be] hover:bg-[#f0f3ff] transition-colors duration-300 transition-transform active:scale-95' href='#'>Claims</a>
                        <a className='text-[#151c27]/60 hover:text-[#0058be] hover:bg-[#f0f3ff] transition-colors duration-300 transition-transform active:scale-95' href='#'>Support</a>
                    </nav>
                </div>
                <div className='flex items-center gap-4'>
                    <button className='p-2 rounded-full hover:bg-[#f0f3ff] transition-colors duration-300 transition-transform active:scale-95'>
                        <span className='material-symbols-outlined text-[#151c27]/60'>notifications</span>
                    </button>
                    <button className='p-2 rounded-full hover:bg-[#f0f3ff] transition-colors duration-300 transition-transform active:scale-95'>
                        <span className='material-symbols-outlined text-[#151c27]/60'>account_circle</span>
                    </button>
                </div>
            </div>
            <div className='bg-[#f0f3ff] h-[1px] w-full'></div>
        </header>
    );
};

export default Header;
