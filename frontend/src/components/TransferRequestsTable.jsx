import React from 'react';

const TransferRequestsTable = () => {
  const requests = [
    {
      flat: '402',
      seller: 'Aditya Sharma',
      buyer: 'Rohan Mehta',
      status: 'Document Upload',
      statusColor: 'bg-secondary-container',
      statusTextColor: 'text-on-secondary-container',
    },
    {
      flat: '105',
      seller: 'Meera Vora',
      buyer: 'Sunita Iyer',
      status: 'Final Approval',
      statusColor: 'bg-primary-container',
      statusTextColor: 'text-on-primary-container',
    },
    {
      flat: '312',
      seller: 'Karan Gupta',
      buyer: 'Priya Shah',
      status: 'Dues Verification',
      statusColor: 'bg-tertiary-fixed',
      statusTextColor: 'text-on-tertiary-fixed-variant',
    },
  ];

  return (
    <div className='bg-surface-container-lowest rounded-xl p-8'>
      <div className='flex justify-between items-center mb-10'>
        <h3 className='text-xl font-bold font-headline text-on-surface'>Active Transfer Requests</h3>
        <button className='text-sm font-semibold text-on-primary-fixed-variant hover:text-primary transition-colors flex items-center gap-1'>
          View All <span className='material-symbols-outlined text-xs'>arrow_forward</span>
        </button>
      </div>
      <div className='overflow-x-auto'>
        <table className='w-full text-left'>
          <thead>
            <tr className='bg-surface-container-high'>
              <th className='py-4 px-4 text-[10px] font-bold uppercase tracking-[0.1em] text-on-surface-variant rounded-l-lg'>Flat #</th>
              <th className='py-4 px-4 text-[10px] font-bold uppercase tracking-[0.1em] text-on-surface-variant'>Parties</th>
              <th className='py-4 px-4 text-[10px] font-bold uppercase tracking-[0.1em] text-on-surface-variant'>Status</th>
              <th className='py-4 px-4 text-[10px] font-bold uppercase tracking-[0.1em] text-on-surface-variant rounded-r-lg'>Actions</th>
            </tr>
          </thead>
          <tbody className='divide-y-0'>
            {requests.map((request, index) => (
              <tr key={index} className='group hover:bg-surface-container-low transition-colors'>
                <td className='py-6 px-4'>
                  <div className='flex items-center gap-3'>
                    <div className={`w-1 h-8 ${index === 0 ? 'bg-primary' : 'bg-transparent group-hover:bg-primary'} rounded-full transition-all`}></div>
                    <span className='font-headline font-bold text-on-surface'>{request.flat}</span>
                  </div>
                </td>
                <td className='py-6 px-4'>
                  <div className='space-y-0.5'>
                    <p className='text-sm font-semibold text-on-surface'>{request.seller}</p>
                    <p className='text-xs text-on-surface-variant'>Buyer: {request.buyer}</p>
                  </div>
                </td>
                <td className='py-6 px-4'>
                  <span className={`inline-flex items-center gap-1.5 px-3 py-1 rounded-full ${request.statusColor} ${request.statusTextColor} text-[11px] font-bold uppercase tracking-wider`}>
                    <span className={`h-1.5 w-1.5 rounded-full ${request.statusColor === 'bg-tertiary-fixed' ? 'bg-on-tertiary-fixed-variant' : 'bg-on-primary-container'}`}></span>
                    {request.status}
                  </span>
                </td>
                <td className='py-6 px-4'>
                  <button className='text-slate-400 hover:text-primary transition-colors'>
                    <span className='material-symbols-outlined'>more_horiz</span>
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default TransferRequestsTable;
