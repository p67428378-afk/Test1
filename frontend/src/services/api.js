import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000', // Adjust this to your backend URL
  headers: {
    'Content-Type': 'application/json',
  },
});

export const register = (userData) => {
  return apiClient.post('/auth/register', userData);
};

export const login = (credentials) => {
  const formData = new URLSearchParams();
  formData.append('username', credentials.username);
  formData.append('password', credentials.password);

  return apiClient.post('/auth/token', formData, {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
  });
};

export const initiateTransfer = (transferData, token) => {
  return apiClient.post('/flat-transfer/initiate', transferData, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
};

// Add other API calls as needed
