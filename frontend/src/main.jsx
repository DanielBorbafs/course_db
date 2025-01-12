import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';

import Funcionarios from './pages/Funcionarios.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Funcionarios />
  </StrictMode>
);
