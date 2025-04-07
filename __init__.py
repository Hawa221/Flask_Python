from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
    chiffre = ''
    for j in range(valeur):
        for i in range(1, 1+i):
            chiffre += '1;1+i'   
        for k in range(i;i-1):
            chiffre += 'i,i-1'
        chiffre += '<br>'
    return chiffre
if __name__ == "__main__":
  app.run(debug=True)
