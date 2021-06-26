#from flask import Flask, render_template

#app = Flask(__name__)
# listo
class Carta:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo
        
#casi listo
class Ninja(Carta):
    def __init__(self, nombre, costo, poder, resistencia):
        super().__init__(nombre, costo)
        self.poder = poder
        self.resistencia = resistencia
    
    #rival = carta ninja del oponente
    def attack(self, oponente):
        if isinstance(oponente, Ninja) == False:
            print('Esta carta no es del tipo Ninja')
            return
        oponente.resistencia -= self.poder
        print (f"Has conseguido dañar en {self.poder} puntos a {oponente.nombre}")

class Efectos(Carta):
    def __init__(self, nombre, costo, texto, stat, magnitud):
        super().__init__(nombre, costo)
        self.texto = texto
        self.stat = stat
        self.magnitud = magnitud

    def algoritmoDuro(self):
        self.costo 
        self.resistencia += self.magnitud
    
    def promesaNoManejada(self, rival):
        rival.resistencia -= 2
    
    def programacionEnPareja(self):
        self.poder += 2

class Jugador(Ninja, Efectos):
    def __init__(self, nombre, gemas):
        self.nombre = nombre
        self.gemas = gemas


import pdb; pdb.set_trace()



'''
# turno 1
red_jinja = Unit('Red Ninja', 3, 3, 7)
# turno 2
hard_alg = Unit('Hard Algorithm', 2, 'resistencia', 3)
hard_alg.play(red_jinja)

cards = [red_jinja, hard_alg]


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
'''