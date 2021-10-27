INSERT INTO prefeitos (nome, cidade_id)
VALUES
	('Rodrigo neves', (SELECT id FROM cidades WHERE nome = 'Niterói')),
	('Raquel Lyra', (SELECT id from cidades WHERE nome = 'Caruaru')),
	('Felipe dos anjos', NULL);