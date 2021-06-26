#from flask import Flask, render_template

#app = Flask(__name__)

class Carta:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo
    
    def display_info(self):
        return(f"{self.nombre}, {self.poder} y {self.resistencia}")
        
    def __repr__(self):
        return self
        

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
        print (f"Has conseguido dañar en {self.poder} puntos al {oponente.nombre}. Su nueva resistencia es {oponente.resistencia}")

class Efectos(Carta):
    
    def __init__(self, nombre, costo, texto, stat, magnitud):
        super().__init__(nombre, costo)
        self.texto = texto
        self.stat = stat
        self.magnitud = magnitud
    
    def affect(self, target):
        if isinstance(target,Ninja) == False:
            print('Esta carta no es del tipo Ninja')
            return
        
        if self.stat == 'poder':
            target.poder += self.magnitud
        elif self.stat == 'resistencia':
            target.resistencia += self.magnitud

'''
class Jugador(Ninja, Efectos):
    def __init__(self, nombre, gemas):
        self.nombre = nombre
        self.gemas = gemas
'''

#cartas ninja
ninjarojo = Ninja('ninja_rojo', 3, 3, 4)
ninjanegro = Ninja('ninja_negro', 4, 5, 4)


#cartas efecto
algoritmoduro = Efectos('Algoritmo Duro', 2, 'Aumentar la resistencia del objetivo en 3','resistencia', 3 )
promesaNoManejada = Efectos("Promesa no manejada", 1, "Reducir la resistencia del objetivo en 2", "resistencia", -2)
programacionEnPareja = Efectos("Programación en pareja", 3, "Aumentar el poder del objetivo en 2", "ataque", 2)

'''
#jugadores
jugador1 = Jugador('Andrea', 100)
jugador2 = Jugador('Juan', 100)
jugador3 = Jugador('Ruben',100)
'''


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