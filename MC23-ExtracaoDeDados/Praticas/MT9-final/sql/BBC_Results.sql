--Remover tabela atual
drop table bbc;

--Criar tabela
create table bbc(
	ttamp timestamp,
	hours_sleeped varchar(100),
	recogn_score varchar(100),
	temporal_memory varchar(100)
);

-- Inserir dados na tabela bbc
COPY bbc FROM '/Users/zegildo/Desktop/UFERSA/Disciplinas/2017.2/MineracaoDeDados/DataMining-Projects/MC17-ExtracaoDeDados/Praticas/MT9-final/BBC_Results_sql.csv' (DELIMITER ',');

-- Converter tipo das colunas
ALTER TABLE bbc ALTER COLUMN hours_sleeped TYPE NUMERIC USING CASE WHEN hours_sleeped ~ E'\\d+\\.\\d+|\\d+' THEN hours_sleeped::NUMERIC ELSE NULL END; 
ALTER TABLE bbc ALTER COLUMN recogn_score TYPE NUMERIC USING CASE WHEN recogn_score ~ '^[-+0-9]+$' THEN recogn_score::NUMERIC ELSE NULL END; 
ALTER TABLE bbc ALTER COLUMN temporal_memory TYPE NUMERIC USING CASE WHEN temporal_memory ~ '^[-+0-9]+$' THEN temporal_memory::NUMERIC ELSE NULL END; 

-- Verifica integridade da tabela
select * from bbc;

--Validacao
select count(*) from bbc 
	where hours_sleeped is null 
	or recogn_score is null 
	or temporal_memory is null 
	or hours_sleeped < 0 or hours_sleeped > 24 
	or recogn_score < 0 or recogn_score > 100
	or temporal_memory < 0 or temporal_memory > 100


--Limpeza
update bbc set hours_sleeped = (select avg(hours_sleeped) from bbc) where hours_sleeped is null or hours_sleeped < 0 or hours_sleeped > 24 
update bbc set recogn_score = (select avg(recogn_score) from bbc) where recogn_score is null or recogn_score < 0 or recogn_score > 100
update bbc set temporal_memory = (select avg(temporal_memory) from bbc) where temporal_memory is null or temporal_memory < 0 or temporal_memory > 100

select * from bbc;
