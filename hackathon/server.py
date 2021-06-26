from flask import Flask, render_template

app = Flask(__name__)

class Ninja(self, nombre):
    
    def __init__(self, nombre, costo, poder, resistencia):
        self.nombre = nombre
        self.costo = costo
        self.poder = poder
        self.resistencia = resistencia
    
    def attack(self):
        raise NotImplementedError

class Efectos(Ninja):
    
    def __init__(self, nombre, efecto, costo, texto, stat, magnitud):
        super().__init__(nombre)
        self.costo = costo
        self.efecto = efecto
        self.texto = texto
        self.stat = stat
        self.magnitud = magnitud

    def algoritmoduro(self):
        self.resistencia += 3
    
    def promesanomanejada(self, rival):
        rival.resistencia -= 2








'''
# turno 1
red_jinja = Unit('Red Ninja', 3, 3, 7)
# turno 2
hard_alg = Unit('Hard Algorithm', 2, 'resistencia', 3)
hard_alg.play(red_jinja)

cards = [red_jinja, hard_alg]
'''

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


app.run()