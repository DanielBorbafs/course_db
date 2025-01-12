import express from 'express';
import db from '../db/conection.js';

const router = express.Router();

router.get('/listar-funcionarios', async (req, res) => {
  try {
    const [results] = await db.query('SELECT * FROM funcionarios'); // Usando a versão promise do query
    res.json(results); // Retorna os dados no formato JSON
  } catch (err) {
    console.error('Erro na consulta ao banco de dados:', err);
    res.status(500).json({ error: 'Erro na consulta ao banco de dados' });
  }
});

// permite listar o funcionário por matrícula
router.get('/listar-funcionarios/:matricula', async (req, res) => {
  const { matricula } = req.params;
  try {
    const result = await db.query(
      'SELECT * FROM funcionarios WHERE matricula = ?',
      [matricula]
    );
    if (result.length > 0) {
      res.json(result[0]); // Retorna apenas o funcionário encontrado
    } else {
      res.status(404).json({ error: 'Funcionário não encontrado' });
    }
  } catch (err) {
    res.status(500).json({ error: 'Erro ao buscar funcionário' });
  }
});

export default router;
