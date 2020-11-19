import sqlite3
import csv

banco =  sqlite3.connect('MyDatabase.db', check_same_thread=False)
cursor = banco.cursor()  

def Create_Table():
  cursor.execute("CREATE TABLE Cidade (id integer PRIMARY KEY AUTOINCREMENT,Nome text)")
  cursor.execute("CREATE TABLE Aviao (id integer PRIMARY KEY AUTOINCREMENT,Nome text)")
  cursor.execute("CREATE TABLE Voo (id integer PRIMARY KEY AUTOINCREMENT,idAviao integer,idCidadeOrigem integer,idCidadeDestino integer, Data text, Horario interger, Duracao_Voo integer)")
  banco.commit()

def Add_airplane(nome):
  cursor.execute(f"INSERT INTO Aviao(Nome) Values('{nome}')")
  banco.commit()

def Add_city(nome):
  cursor.execute(f"INSERT INTO Cidade(Nome) Values('{nome}')")
  banco.commit()

def Add_flights(nome,idCidadeDestino,idCidadeOrigem,data,idAviao,horario,duracao_Voo):
  cursor.execute(f"INSERT INTO Voo(idAviao,idCidadeOrigem,idCidadeDestino,Data,Horario,Duracao_Voo) Values('{idAviao}','{idCidadeOrigem}','{idCidadeDestino}','{data}','{horario}','{duracao_Voo}')")
  banco.commit()




#Add_flights(cursor, nome, idCidadeDestino, idCidadeOrigem,data, idAviao, horario, duracao_Voo)
