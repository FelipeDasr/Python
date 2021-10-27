INSERT INTO cidades (nome, AREA, estado_id)
VALUES
	('Campinas', 795, 21),
	('Niterói', 133.9, 15);

INSERT INTO cidades(nome, AREA, estado_id)
VALUES
	('Caruaru', 920.6, (SELECT id FROM estados WHERE sigla = 'PE')),
	('Juazeiro do norte', 248.2, (SELECT id FROM estados WHERE sigla = 'CE'));