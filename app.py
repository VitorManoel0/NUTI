from flask import Flask, request, render_template, redirect, flash
import crud_database

app = Flask(__name__, template_folder='templates_folder')

try:
  crud_database.Create_Table()
except:
  pass

@app.route("/", methods = ["GET"])
def index():

  aviao = crud_database.list_airplanes()
  cidade = crud_database.list_city()
  return render_template('Index.html' , aviao = aviao, cidade = cidade)

@app.route("/view", methods = ["GET","POST"])
def view():

  formulario = request.form

  if "voo" in formulario:
    lista = (crud_database.list_flights())
    return render_template('Voos.html', nome = lista)
  elif "aviao" in formulario:
    lista = (crud_database.list_airplanes())
    return render_template('Aviao.html', nome = lista)
  elif "cidade" in formulario:
    lista = (crud_database.list_city())
    return render_template('Cidade.html', nome = lista)

@app.route("/erro", methods = ["GET"])
def erro():

  return render_template('Erro.html')

@app.route("/add", methods = ["POST","GET"])
def add_voo():
  
  formulario = request.form

  if "aviao" in formulario:  
    if crud_database.Add_airplane(formulario["aviao"]) == 5:
      return redirect ("/erro")

  elif "cidade" in formulario:
    if crud_database.Add_city(formulario["cidade"]) == 5:
      return redirect ("/erro")

  elif "idAviao" in formulario:
    crud_database.list_flights()
    if crud_database.Add_flights(formulario["idAviao"],formulario["idCidadeOrigem"],formulario["idCidadeDestino"],formulario["data"],formulario["horario"],formulario["duracao_Voo"]) == 5:
      return redirect ("/erro")
    
  return redirect("/")
    
if __name__ == "__main__":
  app.run(debug=True)