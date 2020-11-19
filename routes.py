from flask import Flask, request, render_template
import crud_database

app = Flask(__name__, template_folder='templates_folder')
try:
  crud_database.Create_Table()
except:
  pass

@app.route("/", methods = ["POST", "GET"])
def index():

  if request.method == "POST":
    body = request.get_json()
    crud_database.Add_airplane(body["aviao"])
    crud_database.Add_city(body["cidade"])
    
    print(body)
    
  render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)