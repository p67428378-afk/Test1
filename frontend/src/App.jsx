import React, { useState, useEffect } from 'react';
import axios from 'axios';

const App = () => {
  const [formData, setFormData] = useState({
    vehicle_value: '',
    tax_bracket: '',
    ncb: 20,
    vehicle_type: 'sedan',
    addons: [],
  });
  const [premium, setPremium] = useState(null);
  const [breakdown, setBreakdown] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleCheckboxChange = (e) => {
    const { name, checked } = e.target;
    if (checked) {
      setFormData({ ...formData, addons: [...formData.addons, name] });
    } else {
      setFormData({ ...formData, addons: formData.addons.filter((addon) => addon !== name) });
    }
  };

  const handleNcbChange = (e) => {
    setFormData({ ...formData, ncb: parseInt(e.target.value, 10) });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post('http://localhost:8000/api/v1/insurance/premium/calculate', formData);
      setPremium(res.data.annual_premium);
      setBreakdown(res.data.breakdown);
    } catch (error) {
      console.error('Error calculating premium:', error);
    }
  };

  const handleClear = () => {
    setFormData({
      vehicle_value: '',
      tax_bracket: '',
      ncb: 20,
      vehicle_type: 'sedan',
      addons: [],
    });
    setPremium(null);
    setBreakdown(null);
  };

  return (
    <div className='min-h-screen bg-gray-100 text-gray-800 font-sans'>
      <header className='bg-white shadow-md'>
        <nav className='container mx-auto px-6 py-4 flex justify-between items-center'>
          <div className='text-2xl font-bold text-blue-600'>AutoInsure</div>
          <div className='flex space-x-4'>
            <a href="#" className='text-gray-600 hover:text-blue-600'>Home</a>
            <a href="#" className='text-gray-600 hover:text-blue-600'>Products</a>
            <a href="#" className='text-gray-600 hover:text-blue-600'>Claims</a>
            <a href="#" className='text-gray-600 hover:text-blue-600'>About Us</a>
          </div>
        </nav>
      </header>

      <main className='container mx-auto px-6 py-8'>
        <div className='grid grid-cols-1 lg:grid-cols-3 gap-8'>
          {/* Form Section */}
          <div className='lg:col-span-2 bg-white p-8 rounded-lg shadow-lg'>
            <h1 className='text-3xl font-bold mb-6 text-gray-700 pr-4'>Vehicle Insurance Premium Calculator</h1>
            <form onSubmit={handleSubmit}>
              <div className='grid grid-cols-1 md:grid-cols-2 gap-6 items-center'>
                <div className="form-group">
                  <label htmlFor="vehicle_value" className='block text-sm font-medium text-gray-600'>Vehicle Value ($)</label>
                  <input type="number" id="vehicle_value" name="vehicle_value" value={formData.vehicle_value} onChange={handleInputChange} className='mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500' required />
                </div>
                <div className="form-group">
                  <label htmlFor="tax_bracket" className='block text-sm font-medium text-gray-600'>Tax Bracket (%)</label>
                  <input type="number" id="tax_bracket" name="tax_bracket" value={formData.tax_bracket} onChange={handleInputChange} className='mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500' required />
                </div>
                <div className="form-group">
                  <label htmlFor="vehicle_type" className='block text-sm font-medium text-gray-600'>Vehicle Type</label>
                  <select id="vehicle_type" name="vehicle_type" value={formData.vehicle_type} onChange={handleInputChange} className='mt-1 block w-full px-3 py-2 bg-white border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500'>
                    <option value="sedan">Sedan</option>
                    <option value="suv">SUV</option>
                    <option value="hatchback">Hatchback</option>
                  </select>
                </div>
                <div className='md:col-span-2 form-group'>
                  <label htmlFor="ncb" className='block text-sm font-medium text-gray-600'>No-Claim Bonus (NCB): {formData.ncb}%</label>
                  <input type="range" id="ncb" name="ncb" min="20" max="50" step="5" value={formData.ncb} onChange={handleNcbChange} className='mt-1 w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer' />
                </div>
                <div className='md:col-span-2 form-group'>
                  <p className='block text-sm font-medium text-gray-600'>Add-ons</p>
                  <div className='mt-2 flex items-center space-x-4'>
                    <label className='flex items-center'>
                      <input type="checkbox" name="adas" checked={formData.addons.includes('adas')} onChange={handleCheckboxChange} className='h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500' />
                      <span className='ml-2 text-sm'>ADAS</span>
                    </label>
                    <label className='flex items-center'>
                      <input type="checkbox" name="anti_theft" checked={formData.addons.includes('anti_theft')} onChange={handleCheckboxChange} className='h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500' />
                      <span className='ml-2 text-sm'>Anti-Theft Device</span>
                    </label>
                  </div>
                </div>
              </div>
              <div className='mt-8 flex justify-end space-x-4'>
                <button type="submit" className='px-6 py-2 bg-blue-600 text-white font-semibold rounded-md shadow-sm hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500'>Calculate Premium</button>
                <button type="button" onClick={handleClear} className='px-6 py-2 bg-gray-300 text-gray-800 font-semibold rounded-md shadow-sm hover:bg-gray-400 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-gray-500'>Clear Form</button>
              </div>
            </form>
          </div>

          {/* Results Section */}
          <div className='space-y-8'>
            <div className='bg-white p-6 rounded-lg shadow-lg'>
              <h2 className='text-xl font-bold text-gray-700 mb-4'>Annual Premium</h2>
              <div className='text-4xl font-extrabold text-blue-600'>
                {premium !== null ? `$${premium.toFixed(2)}` : '$0.00'}
              </div>
            </div>
            {breakdown && (
              <div className='bg-white p-6 rounded-lg shadow-lg'>
                <h2 className='text-xl font-bold text-gray-700 mb-4'>Detailed Breakdown</h2>
                <ul className='space-y-2 text-sm'>
                  <li className='flex justify-between'><span>Base Premium:</span> <span>${breakdown.base_premium.toFixed(2)}</span></li>
                  <li className='flex justify-between'><span>NCB Discount ({breakdown.ncb_discount_percentage}%):</span> <span className='text-green-600'>-${breakdown.ncb_discount_amount.toFixed(2)}</span></li>
                  <li className='flex justify-between'><span>Add-ons Cost:</span> <span>+${breakdown.addons_cost.toFixed(2)}</span></li>
                  <li className='flex justify-between font-bold border-t pt-2 mt-2'><span>Subtotal:</span> <span>${breakdown.subtotal.toFixed(2)}</span></li>
                  <li className='flex justify-between'><span>Tax ({breakdown.tax_percentage}%):</span> <span>+${breakdown.tax_amount.toFixed(2)}</span></li>
                  <li className='flex justify-between font-bold text-lg border-t pt-2 mt-2'><span>Final Premium:</span> <span>${breakdown.final_premium.toFixed(2)}</span></li>
                </ul>
              </div>
            )}
             <div className='bg-white p-6 rounded-lg shadow-lg text-center'>
                <img src="https://picsum.photos/seed/picsum/200/300" alt="Happy family with car" className='mx-auto mb-4 rounded-lg'/>
                <h3 className='font-bold text-gray-700'>New Policy Holder?</h3>
                <p className='text-sm text-gray-600'>Learn how to maximize your savings.</p>
             </div>
          </div>
        </div>
      </main>
    </div>
  );
};

export default App;
