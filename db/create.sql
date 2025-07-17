CREATE TABLE users (
    id INT PRIMARY KEY IDENTITY(1,1),
    username VARCHAR(100),
    role VARCHAR(50), -- 'aluno' ou 'professor'
    created_at DATETIME DEFAULT GETDATE()
);

CREATE TABLE follows (
    following_user_id INT,
    followed_user_id INT,
    created_at DATETIME DEFAULT GETDATE(),
    PRIMARY KEY (following_user_id, followed_user_id),
    FOREIGN KEY (following_user_id) REFERENCES users(id),
    FOREIGN KEY (followed_user_id) REFERENCES users(id)
);

CREATE TABLE posts (
    id INT PRIMARY KEY IDENTITY(1,1),
    title VARCHAR(255),
    body VARCHAR(MAX), -- conteúdo do post
    user_id INT NOT NULL,
    status VARCHAR(50),
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE cursos (
    id INT PRIMARY KEY IDENTITY(1,1),
    titulo VARCHAR(255),
    id_professor INT NOT NULL,
    data_criacao DATE DEFAULT GETDATE(),
    FOREIGN KEY (id_professor) REFERENCES users(id)
);

CREATE TABLE aulas (
    id INT PRIMARY KEY IDENTITY(1,1),
    id_curso INT NOT NULL,
    titulo VARCHAR(255),
    duracao_minutos INT,
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);

CREATE TABLE matriculas (
    id_aluno INT,
    id_curso INT,
    data_matricula DATE DEFAULT GETDATE(),
    PRIMARY KEY (id_aluno, id_curso),
    FOREIGN KEY (id_aluno) REFERENCES users(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);

CREATE TABLE avaliacoes (
    id INT PRIMARY KEY IDENTITY(1,1),
    id_aluno INT,
    id_curso INT,
    nota INT CHECK (nota BETWEEN 1 AND 5),
    comentario VARCHAR(MAX),
    FOREIGN KEY (id_aluno) REFERENCES users(id),
    FOREIGN KEY (id_curso) REFERENCES cursos(id)
);
