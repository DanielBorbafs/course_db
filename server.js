import express from 'express';
import getRoutes from './routes/get.js';
import postRoutes from './routes/post.js';
import deleteRoutes from './routes/delete.js';
import putRoutes from './routes/put.js';
import cors from 'cors';

const app = express();
app.use(cors()); // Permite requisições de origens diferentes
app.use(express.json());

app.use('/', getRoutes);
app.use('/', postRoutes);
app.use('/', deleteRoutes);
app.use('/', putRoutes);

app.listen(3000, () => console.log('Servidor rodando'));
