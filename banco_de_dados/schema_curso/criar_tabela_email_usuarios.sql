USE usuarios;

CREATE TABLE IF NOT EXISTS nomes(
	
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	nome VARCHAR(300) NOT NULL,
	PRIMARY KEY (id)
	
);

CREATE TABLE IF NOT EXISTS emails(
	
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	email VARCHAR(300) NOT NULL,
	UNIQUE KEY (email),
	PRIMARY KEY (id)
		
); 

CREATE TABLE IF NOT EXISTS senhas(

	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
	senha VARCHAR(300) NOT NULL,
	PRIMARY KEY (id)
		
);

CREATE TABLE IF NOT EXISTS usuario(
	
	id_usuario INT UNSIGNED NOT NULL AUTO_INCREMENT,
	id_nome VARCHAR(300) NOT NULL,
	id_email VARCHAR(300) NOT NULL,
	id_senha VARCHAR(300) NOT NULL,
	PRIMARY KEY (id_usuario, id_nome, id_email, id_senha)
	
);