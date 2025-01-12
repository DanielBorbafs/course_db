import { useState } from 'react';
import './Funcionarios.css';
import api from '../services/api.js'; // Certifique-se de que esse caminho está correto

function Funcionarios() {
  const [matricula, setMatricula] = useState('');
  const [funcionario, setFuncionario] = useState(null); // Inicialmente null, pois não há dados
  const [erro, setErro] = useState('');

  // Função para buscar funcionário pela matrícula
  async function getFuncionario(e) {
    e.preventDefault(); // Impede o comportamento de submissão do formulário

    if (!matricula) {
      setErro('Por favor, insira uma matrícula.');
      return;
    }

    try {
      const response = await api.get(`/listar-funcionarios/${matricula}`); // Corrigido para interpolar a matrícula
      if (response.data && response.data.length > 0) {
        setFuncionario(response.data[0]); // Pega o primeiro item do array
        setErro(''); // Limpa a mensagem de erro
      } else {
        setFuncionario(null); // Caso o funcionário não seja encontrado
        setErro('Funcionário não encontrado.');
      }
    } catch (error) {
      setFuncionario(null); // Limpa os dados do funcionário em caso de erro
      setErro('Erro ao buscar o funcionário.');
      console.error('Erro ao buscar usuário:', error);
    }
  }

  return (
    <div className="container">
      <form onSubmit={getFuncionario}>
        {' '}
        {/* Previne o envio do formulário */}
        <h1>Funcionários</h1>
        {/* Formulário para busca do funcionário */}
        <div className="input-group mb-3">
          <span className="input-group-text" id="basic-addon1">
            Matrícula
          </span>
          <input
            type="text"
            className="form-control"
            placeholder="Digite a matrícula"
            aria-label="Matrícula"
            value={matricula}
            onChange={(e) => setMatricula(e.target.value)} // Atualiza a matrícula
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Buscar
        </button>
        {/* Exibe os dados do funcionário se encontrado */}
        {funcionario && (
          <div className="mt-3 card-funcionario">
            <h3>Detalhes do Funcionário</h3>

            <p>Nome: {funcionario.nome}</p>
            <p>Departamento: {funcionario.departamento}</p>
            <p>Sexo:{funcionario.sexo}</p>
            <p>Salario: R${funcionario.salario}</p>
          </div>
        )}
        {/* Exibe erro, se houver */}
        {erro && (
          <div className="mt-3 text-danger">
            <strong>Erro:</strong> {erro}
          </div>
        )}
      </form>
    </div>
  );
}

export default Funcionarios;
