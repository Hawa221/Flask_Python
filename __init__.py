from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    chiffre = ''
    for j in range(valeur):
        for i in range(1,j+2):
            chiffre += str(i)
        for i in range(j, 0, -1);
            chiffre += str(i)
        chiffre += '<br>'
    return chiffre
if __name__ == "__main__":
  app.run(debug=True)
