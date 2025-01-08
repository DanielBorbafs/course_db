import express from 'express'
import getRoutes from './routes/get.js'


const app = express()
app.use(express.json());

app.use('/', getRoutes)


app.listen(3000, () => console.log('Servidor rodando'));