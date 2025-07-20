-- Liste os cursos que têm menos de 5 alunos matriculados.
SELECT C.TITULO, COUNT(M.ID_ALUNO) AS QTD_ALUNO
FROM CURSOS C
JOIN MATRICULAS M
ON C.ID = M.ID_CURSO
GROUP BY C.TITULO
HAVING (COUNT(M.ID_ALUNO)) < 5

-- Liste os cursos com média de avaliação maior ou igual a 4.
SELECT C.TITULO, AVG(A.NOTA) AS media
FROM cursos C 
JOIN avaliacoes A
ON C.id = A.id_curso 
GROUP BY C.titulo
HAVING (AVG(A.NOTA)) >= 4
GO

-- Mostre os alunos que nunca avaliaram nenhum curso.
SELECT U.USERNAME
FROM USERS U 
LEFT JOIN AVALIACOES A ON U.ID = A.id_aluno
WHERE U.ROLE = 'ALUNO'
AND A.ID_ALUNO IS NULL


-- Mostre os professores que criaram mais de 3 cursos.
SELECT U.USERNAME, COUNT(C.id_professor) AS QTD_CURSOS
FROM USERS U 
JOIN CURSOS C 
ON U.id = C.id_professor
WHERE U.role = 'professor'
GROUP BY U.USERNAME
HAVING COUNT(C.id_professor) > 3

-- Liste o total de posts criados por cada usuário, ordenado do maior para o menor.
SELECT U.USERNAME, COUNT(P.ID) AS [QUANTIDADE POSTS]
FROM users U
INNER JOIN POSTS P
ON U.ID = P.user_id
GROUP BY U.USERNAME
ORDER BY [QUANTIDADE POSTS] DESC
GO

-- Liste todos os usuários que seguiram mais de 2 outros usuários.
SELECT 
    U.username,
    COUNT(F.followed_user_id) AS qtd_seguidos
FROM 
    users U
JOIN 
    follows F ON U.id = F.following_user_id
GROUP BY 
    U.username
HAVING 
    COUNT(F.followed_user_id) > 1
ORDER BY 
    qtd_seguidos DESC;


-- Mostre todos os posts publicados por professores.
 SELECT P.TITLE, P.BODY, P.STATUS, U.USERNAME
 FROM POSTS P
 JOIN USERS U 
 ON P.user_id = U.id
 WHERE U.role = 'PROFESSOR'
 GO

 -- Para cada curso, mostre a média de avaliação.
SELECT C.TITULO, AVG(A.NOTA) AS [MEDIA DE NOTA]
FROM CURSOS C 
JOIN avaliacoes A
ON C.id = A.id_curso
GROUP BY C.TITULO
ORDER BY [MEDIA DE NOTA] DESC


-- Mostre o tempo total (em minutos) de cada curso somando as aulas.
SELECT C.TITULO, SUM(A.DURACAO_MINUTOS) [DURACAO CURSO]
FROM CURSOS C
JOIN AULAS A 
ON C.id = A.id_curso
GROUP BY C.TITULO
ORDER BY [DURACAO CURSO] DESC