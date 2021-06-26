#from flask import Flask, render_template

#app = Flask(__name__)

class Ninja():
    def __init__(self, nombre, costo, poder, resistencia):
        self.nombre = nombre
        self.costo = costo
        self.poder = poder
        self.resistencia = resistencia
    
    #rival = carta ninja del oponente
    def attack(self, oponente):
        if oponente.rival is None:
            oponente.gemas -= self.poder
            print (f"Has conseguido quitarle {self.poder} gemas a {oponente.nombre}")
        else:    
            oponente.rival.resistencia -= self.poder
            print (f"Has conseguido dañar en  {self.poder} puntos a {oponente.rival} de {oponente.nombre}")

class Efectos():
    
    def __init__(self, efecto, costo, texto, stat, magnitud):
        self.costo = costo
        self.efecto = efecto
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

#cartas ninja
ninjarojo = Ninja('ninja_rojo', 3, 3, 4)
ninjanegro = Ninja('ninja_negro', 4, 5, 4)

#cartas efecto
algoritmoduro = Efectos('algoritmoduro', 2, 'Aumentar la resistencia del objetivo en 3','Resistencia', 3 )

#jugadores
jugador1 = Jugador('Andrea', 100)
jugador2 = Jugador('Juan', 100)
jugador3 = Jugador('Ruben',100)

jugador1.ninjarojo.algoritmoduro()

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