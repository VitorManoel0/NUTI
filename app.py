from flask import Flask, request, render_template, redirect, flash
import crud_database

app = Flask(__name__, template_folder='templates_folder')

#Criando Database se inexiste
try:
  crud_database.Create_Table()
except:
  pass

#Rota para index
@app.route("/", methods = ["GET"])
def index():

  aviao = crud_database.list_airplanes()
  cidade = crud_database.list_city()
  return render_template('Index.html' , aviao = aviao, cidade = cidade)

#Listar voos/aviões/cidades no banco de dados
@app.route("/view", methods = ["GET","POST"])
def view():

  formulario = request.form

  if "voo" in formulario:
    lista = (crud_database.name_for_id())
    return render_template('Voos.html', nome = lista)
  elif "aviao" in formulario:
    lista = (crud_database.list_airplanes())
    return render_template('Aviao.html', nome = lista)
  elif "cidade" in formulario:
    lista = (crud_database.list_city())
    return render_template('Cidade.html', nome = lista)

#Tratamendo de erros
@app.route("/erro/1", methods = ["GET"])
def erro_dado_cadastrado():
  erro = "Dado ja cadastrado"
  return render_template('Erro.html', erro = erro)
@app.route("/erro/2", methods = ["GET"])
def erro_horario_invalid():
  erro = "Horário/Data invalido"
  return render_template('Erro.html', erro = erro)
@app.route("/erro/3", methods = ["GET"])
def erro_local_invalid():
  erro = "Local do voo indisponivel"
  return render_template('Erro.html', erro = erro)

#Adicionar dados no banco de dados se validados
@app.route("/add", methods = ["POST","GET"])
def add_voo():
  
  formulario = request.form

  if "aviao" in formulario:  
    if crud_database.Add_airplane(formulario["aviao"]) == 1:
      return redirect ("/erro/1")

  elif "cidade" in formulario:
    if crud_database.Add_city(formulario["cidade"]) == 1:
      return redirect ("/erro/1")

  elif "idAviao" in formulario:
    
    teste = crud_database.Add_flights(formulario["idAviao"],formulario["idCidadeOrigem"],formulario["idCidadeDestino"],formulario["data"],formulario["horario"],formulario["duracao_Voo"])

    if teste == 1:
      return redirect ("/erro/1")
    if teste == 2:
      return redirect ("/erro/2")
    if teste == 3:
      return redirect ("/erro/3")
    
  return redirect("/")
    
if __name__ == "__main__":
  app.run(debug=True)