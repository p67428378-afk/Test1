import React from 'react';
import Sidebar from '../components/Sidebar';
import Header from '../components/Header';
import MetricCard from '../components/MetricCard';
import TransferRequestsTable from '../components/TransferRequestsTable';
import AuditActivity from '../components/AuditActivity';

const Dashboard = () => {
  return (
    <div className='flex h-screen bg-surface'>
      <Sidebar />
      <div className='flex-1 flex flex-col overflow-hidden'>
        <Header />
        <main className='flex-1 overflow-x-hidden overflow-y-auto bg-surface p-10 space-y-10'>
          <div className='flex justify-between items-end'>
            <div className='space-y-1'>
              <h2 className='text-3xl font-extrabold font-headline tracking-tight text-on-background'>Society Overview</h2>
              <p className='text-on-surface-variant font-body'>Manage property assets and administrative transfers.</p>
            </div>
            <button className='primary-gradient text-on-primary px-8 py-3 rounded-lg font-headline font-bold text-sm flex items-center gap-2 active:scale-95 duration-150'>
              <span className='material-symbols-outlined'>send</span>
              Initiate New Transfer
            </button>
          </div>

          <div className='grid grid-cols-12 gap-6'>
            <MetricCard title='Pending Transfers' value='14' unit='Requests' icon='swap_horiz' />
            <MetricCard title='Ownership Verifications' value='08' unit='Pending' icon='verified' />
            <MetricCard title='Total Dues Outstanding' value='₹4.2M' icon='account_balance_wallet' />
          </div>

          <div className='grid grid-cols-12 gap-8'>
            <div className='col-span-12 lg:col-span-8'>
              <TransferRequestsTable />
            </div>
            <div className='col-span-12 lg:col-span-4'>
              <AuditActivity />
            </div>
          </div>
        </main>
      </div>
    </div>
  );
};

export default Dashboard;
