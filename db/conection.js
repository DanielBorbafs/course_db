import mysql from 'mysql2/promise';
import dotenv from 'dotenv';

dotenv.config();

/*
const db = mysql2.createConnection({
    host: process.env.MYSQLHOST,      // Endereço do banco de dados
    user: process.env.MYSQLUSER,           // Usuário do banco de dados
    password: process.env.MYSQLPASS,           // Senha do banco de dados
    database: 'empresa'     // Nome do banco de dados
});
*/

const db = mysql.createPool({
  host: process.env.MYSQLHOST || 'localhost',
  user: process.env.MYSQLUSER || 'root',
  password: process.env.MYSQLPASS || '1578',
  database: process.env.MYSQLDB || 'empresa',
});

db.getConnection()
  .then(() => console.log('Conexão ao banco de dados bem-sucedida!'))
  .catch((err) => {
    console.error('Erro ao conectar ao banco de dados:', err.message);
    process.exit(1); // Encerra o processo em caso de erro
  });

export default db;
