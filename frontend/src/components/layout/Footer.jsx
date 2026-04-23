import React from 'react';

const Footer = () => {
    return (
        <footer className='w-full py-8 mt-auto bg-[#f0f3ff] font-['Inter'] text-xs tracking-widest uppercase text-[#151c27]/50'>
            <div className='flex flex-col md:flex-row justify-between items-center px-12 gap-4 max-w-[1920px] mx-auto'>
                <span>© 2024 Precision Ledger Insurance. All calculations are editorial estimates.</span>
                <div className='flex gap-8'>
                    <a className='text-[#151c27]/40 hover:text-[#151c27] underline decoration-[#0058be] decoration-2 underline-offset-4 opacity-80 hover:opacity-100 transition-opacity' href='#'>Terms of Service</a>
                    <a className='text-[#151c27]/40 hover:text-[#151c27] underline decoration-[#0058be] decoration-2 underline-offset-4 opacity-80 hover:opacity-100 transition-opacity' href='#'>Privacy Policy</a>
                    <a className='text-[#151c27]/40 hover:text-[#151c27] underline decoration-[#0058be] decoration-2 underline-offset-4 opacity-80 hover:opacity-100 transition-opacity' href='#'>Contact Underwriting</a>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
