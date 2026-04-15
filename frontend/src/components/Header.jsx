import React from 'react';

const Header = () => {
  return (
    <header className='fixed top-0 left-0 right-0 z-50 bg-slate-50 dark:bg-slate-900 tonal-shift flex justify-between items-center w-full px-12 py-4 max-w-[1920px] mx-auto'>
      <div className='text-2xl font-bold tracking-tight text-blue-900 dark:text-blue-50 font-headline'>Anchor Insurance</div>
      <nav className='hidden md:flex items-center gap-8'>
        <a className='text-slate-500 dark:text-slate-400 font-medium hover:text-blue-700 dark:hover:text-blue-300 transition-colors' href="#">Dashboard</a>
        <a className='text-slate-500 dark:text-slate-400 font-medium hover:text-blue-700 dark:hover:text-blue-300 transition-colors' href="#">Policies</a>
        <a className='text-slate-500 dark:text-slate-400 font-medium hover:text-blue-700 dark:hover:text-blue-300 transition-colors' href="#">Claims</a>
        <a className='text-slate-500 dark:text-slate-400 font-medium hover:text-blue-700 dark:hover:text-blue-300 transition-colors' href="#">Support</a>
      </nav>
      <div className='flex items-center gap-4'>
        <button className='bg-secondary-container text-on-secondary-container px-6 py-2 rounded-lg font-semibold hover:opacity-90 transition-all scale-100 active:scale-95'>Log Out</button>
        <button className='bg-primary text-on-primary px-6 py-2 rounded-lg font-semibold hover:bg-primary-container transition-all scale-100 active:scale-95'>New Quote</button>
        <div className='w-10 h-10 rounded-full overflow-hidden border-2 border-outline-variant'>
          <img alt='User Profile Avatar' className='w-full h-full object-cover' src='https://lh3.googleusercontent.com/aida-public/AB6AXuDqfmtL6mI325a4oNar5gt34KAZ5XiQCS0LXsumPdSydVdRX0bDEj5cEnEsfFhx0Zt1yg_o1F6D2Ax_qDEmcprwpgbSkfpdgsMsK_4Q7Bq9Yao8YQpi4YAKaY7LcG2ZythPyehv38OFWQTLQjXDWXs3yQdbH1KAtpJ-Un4mxnV1SJDJZ5XzOd4pEVuGjtkpAfPG_BHZ0knwxa7GIVtk4rH7YOFknPgt1slcbpHdVdxAX1LmykeJCZ2GjSnXt3gNDGccEGXYqk939W8' />
        </div>
      </div>
    </header>
  );
};

export default Header;
