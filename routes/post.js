import express from 'express';
import db from '../db/conection.js';

const router = express.Router();

router.post('/adicionar-funcionarios', (req, res) => {
  const { matricula, nome, departamento, sexo, salario, formado } = req.body;
  console.log('Corpo da requisição:', req.body);
  const query = `
      INSERT INTO Funcionarios (matricula, nome, departamento, sexo, salario, formado)
      VALUES (?, ?, ?, ?, ?, ?)
    `;
  db.execute(
    query,
    [matricula, nome, departamento, sexo, salario, formado],
    (err, result) => {
      if (err) {
        console.error('Erro ao inserir dados:', err);
        res.status(500).json({ message: 'Erro ao adicionar funcionário' });
      } else {
        res.status(200).json({
          message: 'Funcionário adicionado com sucesso',
        });
      }
    }
  );
});

export default router;
