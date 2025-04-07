from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  


@app.route('/<int:valeur>')
def exercice(valeur):
   int = ''
    for j in range(valeur):
        for i in range(1,j+2):
            int += str(i)
        for i in range(j, 0, -1);
            int += str(i)
        int += '<br>'
    return int
if __name__ == "__main__":
  app.run(debug=True)
