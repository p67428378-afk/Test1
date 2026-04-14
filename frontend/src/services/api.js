import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json'
  }
});

export const createUser = (userData) => {
  return apiClient.post('/users/', userData);
};

export const createAccount = (userId, accountData) => {
  return apiClient.post(`/accounts/?user_id=${userId}`, accountData);
};

export const getAccount = (accountId) => {
  return apiClient.get(`/accounts/${accountId}`);
};

export const createLoan = (userId, loanData) => {
  return apiClient.post(`/loans/?user_id=${userId}`, loanData);
};

export const getLoan = (loanId) => {
  return apiClient.get(`/loans/${loanId}`);
};

export const createDeposit = (accountId, depositData) => {
  return apiClient.post(`/deposits/?account_id=${accountId}`, depositData);
};

export const getDeposit = (depositId) => {
  return apiClient.get(`/deposits/${depositId}`);
};
