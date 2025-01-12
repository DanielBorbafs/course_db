import axios from 'axios';

// Referenciando a porta onde esta o backend
const api = axios.create({
  baseURL: 'http://localhost:3000',
});

export default api;
