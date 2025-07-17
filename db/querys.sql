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
