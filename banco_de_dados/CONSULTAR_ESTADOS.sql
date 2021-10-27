-- seleciona todas as colunas
-- SELECT * FROM estados

-- seleção especifica
-- SELECT nome, sigla FROM estados

-- label
SELECT sigla, nome, populacao FROM estados

-- filtro
where populacao >= 10
order by populacao