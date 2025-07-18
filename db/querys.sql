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

