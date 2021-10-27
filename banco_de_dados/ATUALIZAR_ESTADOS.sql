UPDATE estados SET nome = 'Maranhão' 
WHERE sigla = 'MA';

SELECT nome, populacao, sigla FROM estados
WHERE sigla = 'MA';

UPDATE estados SET nome = 'Paraná', populacao = 11.32
WHERE sigla = 'PR';

SELECT nome, populacao, sigla FROM estados
WHERE sigla = 'PR';
