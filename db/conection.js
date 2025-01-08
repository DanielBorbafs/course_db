import mysql2 from 'mysql2'
import dotenv from 'dotenv'

dotenv.config()

const db = mysql2.createConnection({
    host: process.env.MYSQLHOST,      // Endereço do banco de dados
    user: process.env.MYSQLUSER,           // Usuário do banco de dados
    password: process.env.MYSQLPASS,           // Senha do banco de dados
    database: 'empresa'     // Nome do banco de dados
});


// Conectar ao banco de dados
db.connect((err) => {
    if (err) {
        console.error('Erro ao conectar ao banco de dados:', err);
        return;
    }
    console.log('Conectado ao banco de dados MySQL!');
});


export default db