from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    for i in range(1,n+1):
       espace = ' ' * (n - i)
       chiffres = ''
        for j in range(1,i+1):
            chiffres += str(j)
        for i in range(i-1,0,-1):
            print(espace + chiffres)
      
if __name__ == "__main__":
  app.run(debug=True)
