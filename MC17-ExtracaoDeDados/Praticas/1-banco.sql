CREATE TABLE globo(
	noticia varchar(500),
	link varchar(1000)
);

COPY globo FROM '/Users/zegildo/Desktop/UFERSA/Disciplinas/2017.2/MineracaoDeDados/DataMining-Projects/MC17-ExtracaoDeDados/Praticas/globo.csv' (DELIMITER '|');
