import pymysql
import requests
from lxml import html

"""SQL

CREATE DATABASE PARTICIPANTESDB2;
USE PARTICIPANTESDB2;
CREATE TABLE TBL_PARTICIPANTE(
	ID INT NOT NULL AUTO_INCREMENT,
	TX_FOTO VARCHAR(255) NOT NULL,
	TX_NOME VARCHAR(255) NOT NULL,
	TX_LOCALIZACAO VARCHAR(255) NOT NULL,
	DATA_CRIADO DATETIME NOT NULL,
	PRIMARY KEY (ID)
);

"""


class meuMySQL(object):
	def __init__(self, usuario, senha, addr, bd):
		self.usuario = usuario
		self.senha = senha
		self.addr = addr
		self.bd = bd
		self.usavel = False
		self.conectado = False
		self.conn = None
		self.erro = None
		self.erro_msg = None
	def SetErro(self, erro, erro_msg=None):
		self.erro = erro
		self.erro_msg = erro_msg
	def Conectar(self):
		retorno = None
		if not self.conectado and self.conn is None:
			try:
				conn = pymysql.connect(host=self.addr, user=self.usuario, password=self.senha, db=self.bd)
				cur = conn.cursor()
			except Exception as e:
				self.SetErro(True, e)
			else:
				cur.close()
				self.conn = conn
				self.conectado = True
				self.usavel = True
				self.SetErro(False)
				retorno = True
		return retorno
	def Insert(self, query):
		retorno = None
		if self.usavel and self.conectado:
			try:
				with self.conn.cursor() as cur:
					retorno = cur.execute(query)
			except Exception as e:
				self.SetErro(True, e)
			else:
				self.conn.commit()
				self.SetErro(False)
		return retorno
	def Select(self, query):
		retorno = None
		if self.usavel and self.conectado:
			try:
				with self.conn.cursor() as cur:
					cur.execute(query)
					resp = cur.fetchall()
					if len(resp)>0:
						desc = cur.description
						colunas = []
						for i in desc:
							colunas.append(i[0])
						retorno = []
						for i in resp:
							data = {}
							for y in range(len(colunas)):
								data[colunas[y]] = i[y]
							retorno.append(data)
			except Exception as e:
				self.SetErro(True, e)
			else:
				self.SetErro(False)
		return retorno
	def SelectOne(self, query):
		retorno = None
		if self.usavel and self.conectado:
			try:
				with self.conn.cursor() as cur:
					cur.execute(query)
					resp = cur.fetchone()
					if len(resp)>0:
						desc = cur.description
						colunas = []
						for i in desc:
							colunas.append(i[0])
						retorno = []
						data = {}
						for i in range(len(resp)):
							data[colunas[i]] = resp[i]
						retorno.append(data)
			except Exception as e:
				self.SetErro(True, e)
			else:
				self.SetErro(False)
		return retorno





class Participante2(object):
	def __init__(self, inst_sql):
		self.inst_sql = inst_sql
		self.usavel = inst_sql.usavel
		self.Conectar()
		self.participante = self.Participante(self.inst_sql)
	def Conectar(self):
		retorno = None
		if self.usavel:
			if not self.inst_sql.conectado:
				retorno = self.inst_sql.Conectar()
			else:
				retorno = self.inst_sql.conectado
		return retorno
	class Participante(object):
		class ParticipanteData(object):
			def __init__(self, ID=None, TX_FOTO=None, TX_NOME=None, TX_LOCALIZACAO=None, DATA_CRIADO=None):
				self.ID = ID
				self.TX_FOTO = TX_FOTO
				self.TX_NOME = TX_NOME
				self.TX_LOCALIZACAO = TX_LOCALIZACAO
				self.DATA_CRIADO = DATA_CRIADO
			def SetID(self, valor):
				self.ID = valor
			def SetFoto(self, valor):
				self.TX_FOTO = valor
			def SetNome(self, valor):
				self.TX_NOME = valor
			def SetLocalizacao(self, valor):
				self.TX_LOCALIZACAO = valor
			def SetDataCriado(self, valor):
				self.DATA_CRIADO = valor
			def GetID(self):
				return self.ID
			def GetFoto(self):
				return self.TX_FOTO
			def GetNome(self):
				return self.TX_NOME
			def GetLocalizacao(self):
				return self.TX_LOCALIZACAO
			def GetDataCriado(self):
				return self.DATA_CRIADO
		def __init__(self, inst_sql):
			self.inst_sql = inst_sql
			self.tabela = 'TBL_PARTICIPANTE'
		def Adicionar(self, TX_FOTO=None, TX_NOME=None, TX_LOCALIZACAO=None, DATA_CRIADO=None):
			retorno = None
			if self.inst_sql.usavel and self.inst_sql.conectado:
				participante_data = self.ParticipanteData(TX_FOTO=TX_FOTO, TX_NOME=TX_NOME, TX_LOCALIZACAO=TX_LOCALIZACAO, DATA_CRIADO=DATA_CRIADO)
				query = ("INSERT INTO %s (TX_FOTO, TX_NOME, TX_LOCALIZACAO, DATA_CRIADO) VALUES ('%s', '%s', '%s', NOW())" % (self.tabela, participante_data.GetFoto(), participante_data.GetNome(), participante_data.GetLocalizacao()))
				retorno = self.inst_sql.Insert(query)
			return retorno
		def BuscarID(self, valor):
			retorno = None
			if self.inst_sql.usavel and self.inst_sql.conectado:
				participante_data = self.ParticipanteData(ID = int(valor))
				query = ("SELECT * FROM %s WHERE ID = %d" % (self.tabela, participante_data.GetID()))
				resp = self.inst_sql.SelectOne(query)
				if len(resp)>0:
					dados = resp[0]
					participante_data.SetFoto(dados['TX_FOTO'])
					participante_data.SetNome(dados['TX_NOME'])
					participante_data.SetLocalizacao(dados['TX_LOCALIZACAO'])
					participante_data.SetDataCriado(dados['DATA_CRIADO'])
					retorno = participante_data
			return retorno
		def BuscarNome(self, valor):
			retorno = None
			if self.inst_sql.usavel and self.inst_sql.conectado:
				query = "SELECT * FROM " + self.tabela + " WHERE TX_NOME LIKE '%" + valor + "%'"
				resp = self.inst_sql.Select(query)
				if len(resp)>0:
					retorno = []
					for i in resp:
						participante_data.SetFoto(i['TX_FOTO'])
						participante_data.SetNome(i['TX_NOME'])
						participante_data.SetLocalizacao(i['TX_LOCALIZACAO'])
						participante_data.SetDataCriado(i['DATA_CRIADO'])
						retorno.append(participante_data)
			return retorno
		def PegarTodos(self):
			retorno = None
			if self.inst_sql.usavel and self.inst_sql.conectado:
				resp = self.inst_sql.Select(query)
				if len(resp)>0:
					retorno = []
					for i in resp:
						participante_data.SetFoto(i['TX_FOTO'])
						participante_data.SetNome(i['TX_NOME'])
						participante_data.SetLocalizacao(i['TX_LOCALIZACAO'])
						participante_data.SetDataCriado(i['DATA_CRIADO'])
						retorno.append(participante_data)
			return retorno





def meucsv(path):
	import csv
	from datetime import datetime
	import os
	retorno = None
	if os.path.isfile(path):
		try:
			retorno = []
			with open(path) as csvf:
				r = csv.DictReader(csvf)
				for linha in r:
					data = {}
					for i in linha.keys():
						data[i] = linha[i]
					retorno.append(data)
		except Exception as e:
			print (e)
	return retorno





def main():
	db_usuario = 'root'
	db_senha = 'legalizeit'
	db_host = 'localhost'
	db_db = 'ParticipantesDB2'
	sql = meuMySQL(db_usuario, db_senha, db_host, db_db)
	sql.Conectar()
	handler = Participante2(sql)
	path = raw_input('digite caminho do CSV de participantes: ')
	csv = meucsv(path)
	if csv is not None:
		for i in csv:
			coluna_foto = i['foto']
			coluna_nome = i['nome']
			coluna_localizacao = i['localizacao']
			handler.participante.Adicionar(coluna_foto, coluna_nome, coluna_localizacao)


if __name__ == '__main__':
	main()