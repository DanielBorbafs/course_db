import express from 'express';
import getRoutes from './routes/get.js';
import postRoutes from './routes/post.js';
import deleteRoutes from './routes/delete.js';

const app = express();
app.use(express.json());

app.use('/', getRoutes);
app.use('/', postRoutes);
app.use('/', deleteRoutes);

app.listen(3000, () => console.log('Servidor rodando'));
