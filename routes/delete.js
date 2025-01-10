import express from 'express';
import db from '../db/conection.js';

const router = express.Router();

router.delete('/deletar-funcionarios/:id', (req, res) => {
  const itemId = req.params.id; // Obtém o ID do funcionário dos parâmetros da rota
  console.log('ID recebido para exclusão:', itemId);

  const query = `
        DELETE FROM funcionarios WHERE matricula = ?
    `;

  // Executa a query e passa o callback para lidar com o resultado
  db.execute(query, [itemId], (err, result) => {
    if (err) {
      console.error('Erro ao deletar funcionário:', err);
      return res.status(500).json({ message: 'Erro ao deletar funcionário' });
    }

    // Verifica se algum registro foi excluído
    if (result.affectedRows > 0) {
      res.status(200).json({ message: 'Funcionário deletado com sucesso!' });
    } else {
      res.status(404).json({ message: 'Funcionário não encontrado!' });
    }
  });
});

export default router;
