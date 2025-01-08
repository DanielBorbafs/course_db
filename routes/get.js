import express from 'express'
import db from '../db/conection.js'

const router = express.Router()


router.get('/listar-funcionarios', (req, res) => {
    db.query('SELECT * FROM funcionarios', (err, results) => {
        if (err) {
            console.error('Erro na consulta ao banco de dados:', err);
            return res.status(500).send('Erro na consulta');
        }
        res.json(results);  // Retorna os dados no formato JSON
    });
});

export default router