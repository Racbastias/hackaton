from flask import Flask, render_template

app = Flask(__name__)

# listo
class Carta:
    def __init__(self, nombre, costo):
        self.nombre = nombre
        self.costo = costo
    
    def display_info(self):
        return(f"{self.nombre}, {self.poder} y {self.resistencia}")
        
    def __repr__(self):
        return self
        
#casi listo
class Ninja(Carta):
    def __init__(self, nombre, costo, poder, resistencia):
        super().__init__(nombre, costo)
        self.poder = poder
        self.resistencia = resistencia
        #self.image


    #rival = carta ninja del oponente
    def attack(self, oponente):
        if isinstance(oponente, Ninja) == False:
            print('Esta carta no es del tipo Ninja')
            return
        oponente.resistencia -= self.poder
        if oponente.resistencia > 0:
            print(f"Has conseguido dañar en {self.poder} puntos a {oponente.nombre}")
        else:
            print(f"El ninja del oponente ha sido destruído")


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

cartas = [ninjarojo,ninjanegro,algoritmoduro,promesaNoManejada,programacionEnPareja]

#import pdb; pdb.set_trace()

cartas_por_mostrar = []

def jugada1():
    cartas_por_mostrar.append(ninjarojo)

def jugada2():
    algoritmoduro.affect(ninjarojo)
    cartas_por_mostrar.append(algoritmoduro)

def jugada3():
    cartas_por_mostrar.append(ninjanegro)

def jugada4():
    promesaNoManejada(ninjarojo)

jugadas = [jugada1, jugada2, jugada3]
app.sgte_jugada = 0

@app.route("/")
def hello_world():
    print(jugadas[app.sgte_jugada])
    jugadas[app.sgte_jugada]()
    app.sgte_jugada +=1
    #while app.sgte_jugada is None:
        #break

    return render_template('index.html', cartas=cartas_por_mostrar)


app.run(debug=True)

