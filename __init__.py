from flask import Flask
from flask import render_template
from flask import json                                                                                                                                     
app = Flask(__name__)                                                                                                                  

@app.route('/max', methods=['POST'])
def trouver_max():
    data = request.form['valeurs']
    try:
        liste = [int(x.strip()) for x in data.split(',')]
    except ValueError:
        return "Erreur : veuillez entrer uniquement des nombres séparés par des virgules."
        
    max_val = None
    for val in liste:
        if max_val is None or val > max_val:
            max_val = val

    return f"La valeur maximale est : {max_val}"

if __name__ == '__main__':
    app.run(debug=True)
