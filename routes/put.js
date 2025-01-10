import express from 'express';
import db from '../db/conection.js';

const router = express.Router();

router.put('/atualizar-funcionarios/:id', (req, res) => {
  const itemId = req.params.id; // ID do funcionário vindo do parâmetro da URL
  const updates = req.body; // Dados vindos do corpo da requisição

  // Valida se o corpo não está vazio
  if (!updates || Object.keys(updates).length === 0) {
    return res.status(400).json({ message: 'Nenhum dado para atualizar' });
  }

  // Cria dinamicamente os pares "campo = ?" para a query SQL
  const fields = Object.keys(updates)
    .map((field) => `${field} = ?`)
    .join(', ');
  const values = Object.values(updates);

  const query = `
        UPDATE funcionarios 
        SET ${fields}
        WHERE matricula = ?
    `;
  // Adiciona o ID como o último valor para o placeholder da condição WHERE
  values.push(itemId);
  db.execute(query, values, (err, result) => {
    if (err) {
      console.error('Erro ao atualizar funcionário:', err);
      return res.status(500).json({ message: 'Erro ao atualizar funcionário' });
    }

    // Verifica se algum registro foi atualizado
    if (result.affectedRows > 0) {
      res.status(200).json({ message: 'Funcionário atualizado com sucesso!' });
    } else {
      res.status(404).json({ message: 'Funcionário não encontrado!' });
    }
  });
});

export default router;
