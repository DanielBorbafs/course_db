
-- Professores
INSERT INTO users (username, role) VALUES 
('professor_silva', 'professor'),
('professora_oliveira', 'professor'),
('professor_costa', 'professor'),
('professora_santos', 'professor'),
('professor_ribeiro', 'professor');

-- Alunos
INSERT INTO users (username, role) VALUES 
('aluno_joao', 'aluno'),
('aluna_maria', 'aluno'),
('aluno_pedro', 'aluno'),
('aluna_ana', 'aluno'),
('aluno_carlos', 'aluno'),
('aluna_julia', 'aluno'),
('aluno_lucas', 'aluno'),
('aluna_sophia', 'aluno'),
('aluno_mateus', 'aluno'),
('aluna_laura', 'aluno');


-- Seguidores (alunos seguindo professores e outros alunos)
INSERT INTO follows (following_user_id, followed_user_id) VALUES
(6, 1), (7, 1), (8, 1), -- alunos seguindo professor_silva
(6, 2), (9, 2),         -- alunos seguindo professora_oliveira
(10, 3), (11, 3),        -- alunos seguindo professor_costa
(7, 6), (8, 6),          -- alunos seguindo outros alunos
(9, 7), (10, 8);



-- Cursos ministrados pelos professores
INSERT INTO cursos (titulo, id_professor) VALUES
('Introdução à Programação', 1),
('Banco de Dados Avançado', 1),
('Matemática Discreta', 2),
('Algoritmos e Estruturas de Dados', 3),
('Inteligência Artificial', 4),
('Desenvolvimento Web', 5);



-- Matrículas dos alunos nos cursos
INSERT INTO matriculas (id_aluno, id_curso) VALUES
-- Alunos no curso de Introdução à Programação
(6, 1), (7, 1), (8, 1), (9, 1), (10, 1),
-- Alunos no curso de Banco de Dados
(6, 2), (7, 2), (11, 2),
-- Alunos no curso de Matemática Discreta
(8, 3), (9, 3), (12, 3),
-- Alunos no curso de Algoritmos
(10, 4), (11, 4), (12, 4),
-- Alunos no curso de IA
(13, 5), (14, 5), (15, 5),
-- Alunos no curso de Desenvolvimento Web
(6, 6), (8, 6), (10, 6), (12, 6), (14, 6);



-- Aulas para cada curso
INSERT INTO aulas (id_curso, titulo, duracao_minutos) VALUES
-- Aulas do curso 1 (Introdução à Programação)
(1, 'Variáveis e Tipos de Dados', 60),
(1, 'Estruturas Condicionais', 45),
(1, 'Loops e Iterações', 50),
(1, 'Funções', 55),

-- Aulas do curso 2 (Banco de Dados)
(2, 'Modelagem Relacional', 70),
(2, 'SQL Básico', 65),
(2, 'Consultas Avançadas', 80),
(2, 'Índices e Otimização', 60),

-- Aulas do curso 3 (Matemática Discreta)
(3, 'Lógica Proposicional', 50),
(3, 'Teoria dos Conjuntos', 45),
(3, 'Relações e Funções', 55),

-- Aulas do curso 4 (Algoritmos)
(4, 'Complexidade de Algoritmos', 70),
(4, 'Algoritmos de Ordenação', 80),
(4, 'Estruturas de Dados Lineares', 75),

-- Aulas do curso 5 (IA)
(5, 'Introdução à IA', 60),
(5, 'Aprendizado de Máquina', 90),
(5, 'Redes Neurais', 85),

-- Aulas do curso 6 (Desenvolvimento Web)
(6, 'HTML e CSS', 50),
(6, 'JavaScript Básico', 60),
(6, 'Frameworks Front-end', 70),
(6, 'Back-end com Node.js', 80);


-- Posts de usuários (alunos e professores)
INSERT INTO posts (title, body, user_id, status) VALUES
-- Posts do professor 1
('Dica de Programação', 'Sempre comentem seu código!', 1, 'public'),
('Novo Material', 'Upload do material da aula 3 disponível', 1, 'public'),

-- Posts da professora 2
('Prova Marcada', 'A prova será dia 15/10 na sala 203', 2, 'public'),

-- Posts de alunos
('Dúvida sobre loops', 'Alguém pode me ajudar com while em Python?', 6, 'public'),
('Resumo de Matemática', 'Compartilhando meu resumo para a prova', 8, 'public'),
('Trabalho Final', 'Preciso de grupo para o trabalho de BD', 10, 'public'),
('Dica de Livro', 'Recomendo "Clean Code" para todos', 7, 'public');



-- Avaliações dos cursos pelos alunos
INSERT INTO avaliacoes (id_aluno, id_curso, nota, comentario) VALUES
-- Avaliações para o curso 1
(6, 1, 5, 'Ótimo curso para iniciantes!'),
(7, 1, 4, 'Conteúdo muito bem explicado'),
(8, 1, 5, 'Professor muito didático'),

-- Avaliações para o curso 2
(6, 2, 4, 'Conteúdo avançado, mas bem apresentado'),
(7, 2, 3, 'Poderia ter mais exemplos práticos'),

-- Avaliações para o curso 3
(8, 3, 5, 'Matemática nunca foi tão clara'),
(9, 3, 4, 'Bom material de apoio'),

-- Avaliações para o curso 4
(10, 4, 5, 'Excelente abordagem de algoritmos'),
(11, 4, 4, 'Exercícios desafiadores'),

-- Avaliações para o curso 5
(13, 5, 5, 'Conteúdo de ponta na área de IA'),
(14, 5, 4, 'Poderia ter mais laboratórios'),

-- Avaliações para o curso 6
(6, 6, 5, 'Curso completo de desenvolvimento web'),
(8, 6, 4, 'Bom equilíbrio entre teoria e prática');