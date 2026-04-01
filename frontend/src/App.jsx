import React from 'react';
import Header from './components/Header';
import WelcomeHero from './components/WelcomeHero';
import ApplicationProgressTracker from './components/ApplicationProgressTracker';
import FeaturedCardOfferings from './components/FeaturedCardOfferings';
import QuickControl from './components/QuickControl';
import RecentActivity from './components/RecentActivity';
import BottomNavBar from './components/BottomNavBar';

function App() {
  return (
    <div className='bg-background text-on-background font-body selection:bg-primary-fixed-dim selection:text-on-primary-fixed'>
      <Header />
      <main className='pt-24 pb-32 px-6 max-w-5xl mx-auto space-y-10'>
        <WelcomeHero />
        <ApplicationProgressTracker />
        <FeaturedCardOfferings />
        <section className='grid grid-cols-1 lg:grid-cols-12 gap-8'>
          <QuickControl />
          <RecentActivity />
        </section>
      </main>
      <BottomNavBar />
      {/* Decorative Gradients to mimic 'Information Luxury' */}
      <div className='fixed top-0 right-0 w-1/3 h-screen bg-primary/5 -z-10 blur-[120px] pointer-events-none'></div>
      <div className='fixed bottom-0 left-0 w-1/4 h-1/2 bg-on-primary-container/5 -z-10 blur-[100px] pointer-events-none'></div>
    </div>
  );
}

export default App;
