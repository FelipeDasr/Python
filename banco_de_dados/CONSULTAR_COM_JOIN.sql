SELECT c.nome, e.nome, e.regiao FROM estados e, cidades c
WHERE e.id = c.estado_id;