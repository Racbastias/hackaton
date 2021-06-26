from flask import Flask, render_template

app = Flask(__name__)


objetos = [
    {
        'nombre': 'Pepe',
        'edad': 34
    },
    {
        'nombre': 'Juana',
        'edad': 23
    },
    {
        'nombre': 'Julia',
        'edad': 12
    }
]

@app.route("/")
def hello_world():
    return render_template('index.html', objetos=objetos)
'''
#turno 1
red_ninja = Unit('red Ninja'. 3.3.7)

turno 2
hard_alg = Unit (hard algorthm, 2, resistencia, 3
hard_alg.play(redninja))
'''