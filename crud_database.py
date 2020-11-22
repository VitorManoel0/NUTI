import sqlite3
from datetime import date, datetime, timedelta

banco =  sqlite3.connect('MyDatabase.db', check_same_thread=False)
cursor = banco.cursor()  

def Create_Table():
  cursor.execute("CREATE TABLE Cidade (id integer PRIMARY KEY AUTOINCREMENT,Nome text NOT NULL unique)")
  cursor.execute("CREATE TABLE Aviao (id integer PRIMARY KEY AUTOINCREMENT,Nome text NOT NULL unique)")
  cursor.execute("CREATE TABLE Voo (id integer PRIMARY KEY AUTOINCREMENT,idAviao integer NOT NULL,idCidadeOrigem integer NOT NULL,idCidadeDestino integer NOT NULL, Data text NOT NULL, Horario text NOT NULL, Duracao_Voo text NOT NULL)")
  banco.commit()
  return 0

def Add_airplane(nome):
  
  cursor.execute("SELECT * FROM Aviao WHERE (Nome=?)",(nome,))
  entry = cursor.fetchone()

  if entry is None:
    cursor.execute("INSERT INTO Aviao(Nome) Values(?)",(nome,))
    banco.commit()
    return 0
  else:
    return 1

def Add_city(nome):
  
  cursor.execute("SELECT * FROM Cidade WHERE (Nome=?)",(nome,))
  entry = cursor.fetchone()
  if entry is None:
    cursor.execute("INSERT INTO Cidade(Nome) Values(?)",(nome,))
    banco.commit()
    return 0
  else:
    return 1

def Add_flights(idAviao,idCidadeOrigem,idCidadeDestino,data,horario,duracao_Voo):

  idAviao = search_in_airplane(idAviao)
  idCidadeOrigem = search_in_cidade(idCidadeOrigem)
  idCidadeDestino = search_in_cidade(idCidadeDestino)

  cursor.execute("SELECT * FROM Voo WHERE (idAviao=?)",(idAviao[0],)) 
  entry = cursor.fetchall() 

  if datetime.fromisoformat(data+" "+horario) <= datetime.now(): 
    return 2

  if int(idCidadeOrigem[0]) == int(idCidadeDestino[0]):
    return 1
  
  if len(entry) == 0:
    cursor.execute("INSERT INTO Voo(idAviao,idCidadeOrigem,idCidadeDestino,Data,Horario,Duracao_Voo) Values(?,?,?,?,?,?)",(idAviao[0],idCidadeOrigem[0],idCidadeDestino[0],data,horario,duracao_Voo))
    banco.commit()
    return 0

  else:
    dados = entry[-1]
    tempo_voo = dados[6].split(":")

    if datetime.fromisoformat(dados[4]+" "+dados[5]) + timedelta(hours=int(tempo_voo[0]), minutes = int(tempo_voo[1])) >= datetime.fromisoformat(data+" "+horario):
      return 2

    if int(dados[3]) != int(idCidadeOrigem[0]):
      return 3
      
    else:
      cursor.execute("INSERT INTO Voo(idAviao,idCidadeOrigem,idCidadeDestino,Data,Horario,Duracao_Voo) Values(?,?,?,?,?,?)",(idAviao[0],idCidadeOrigem[0],idCidadeDestino[0],data,horario,duracao_Voo))
      banco.commit()
      return 0


def list_airplanes():
  cursor.execute("SELECT * FROM Aviao")
  return cursor.fetchall()
  
def list_city():
  cursor.execute("SELECT * FROM Cidade")
  return cursor.fetchall()

def list_flights():
  cursor.execute("SELECT * FROM Voo")
  return cursor.fetchall()

def search_in_airplane(idAviao):
  avioes = list_airplanes()
  for i,nome in avioes:
    if idAviao == nome:
      return i,nome

def search_in_cidade(idCidade):
  cidades = list_city()
  for i,nome in cidades:
    if idCidade == nome:
      return i,nome

def name_for_id():
  flights=[]
  lista = list_flights()
  for i in lista:
    voo = []
    voo.append(i[0])

    avioes = list_airplanes()
    for j,nome in avioes:
      if i[1] == j:
        voo.append(nome)

    cidades = list_city()
    for j,nome in cidades:
      if i[2] == j:
        voo.append(nome)
        
    cidades = list_city()
    for j,nome in cidades:
      if i[3] == j:
        voo.append(nome)
    voo.append(i[4])
    voo.append(i[5])
    voo.append(i[6])

    flights.append(tuple(voo)) 

  return flights