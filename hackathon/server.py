from flask import Flask, render_template

app = Flask(__name__)

# listo
class Carta:
    def __init__(self, nombre, costo, image):
        self.nombre = nombre
        self.costo = costo
        self.image = image
    
    def display_info(self):
        return(f"{self.nombre}, {self.poder} y {self.resistencia}")
        
    def __repr__(self):
        return self
        
#casi listo
class Ninja(Carta):
    def __init__(self, nombre, costo, imagen, poder, resistencia):
        super().__init__(nombre, costo, imagen)
        self.poder = poder
        self.resistencia = resistencia

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
    def __init__(self, nombre, costo, image, texto, stat, magnitud):
        super().__init__(nombre, costo, image)
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

#cartas ninja
ninjarojo = Ninja('Ninja Rojo', 3, 'ninjarojo.jpg', 3, 4)
ninjanegro = Ninja('Ninja Negro', 4, 'ninjanegro.jpg', 5, 4)

#cartas efecto
algoritmoduro = Efectos('Algoritmo Duro', 2, 'algoritmoduro.jpeg', 'Aumentar la resistencia del objetivo en 3','Resistencia', 3 )
promesaNoManejada = Efectos('Promesa no manejada', 1, 'promesa.jpeg', 'Reducir la resistencia del objetivo en 2', 'Resistencia', -2)
programacionEnPareja = Efectos('Programacion en pareja', 3,'programacion.jpeg', 'Aumentar el poder del objetivo en 2', "Ataque", 2)

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
    promesaNoManejada.affect(ninjarojo)

def jugada5():
    promesaNoManejada.affect(ninjanegro)

def jugada6():
    programacionEnPareja.affect(ninjarojo)
    cartas_por_mostrar.append(programacionEnPareja)
def jugada7():
    ninjarojo.attack(ninjanegro)
    cartas_por_mostrar.append(promesaNoManejada)
    

jugadas = [jugada1, jugada2, jugada3, jugada4, jugada5, jugada6, jugada7]
app.sgte_jugada = 0

@app.route("/")
def hello_world():
    print(jugadas[app.sgte_jugada])
    jugadas[app.sgte_jugada]()
    app.sgte_jugada +=1
    
    return render_template('index.html', cartas=cartas_por_mostrar)


app.run(debug=True)

