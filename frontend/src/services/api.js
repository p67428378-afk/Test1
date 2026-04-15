import axios from 'axios';

const apiClient = axios.create({
  baseURL: '/api/v1',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const calculatePremium = (data) => {
  return apiClient.post('/premium/calculate', data);
};
