#importar modulos
import turtle
import random

#abrir tela
tela = turtle.screen()
tela.bgcolor('lavender')

#definir funcao para delimitar area pela qual a tartaruga ira se mover
def desenhaparede():
    caneta = turtle.Turtle
    caneta.speed(0)
    caneta.up()
    caneta.goto(-199, 199)
    caneta.down()
    for i in range(4):
        caneta.forward(400)
        caneta.right(90)
    caneta.hideturtle

#definir movimentos da tartaruga
def esquerda():
    tartaruga.goto(tartaruga.xcor() - 10, tartaruga.ycor())
    if tartaruga.xcor() < -199:
        tartaruga.setx(-199)

def direita():
    tartaruga.goto(tartaruga.xcor() + 10, tartaruga.ycor())
    if tartaruga.xcor() > 191:
        tartaruga.setx(191)

def cima():
    tartaruga.goto(tartaruga.xcor(), tartaruga.ycor() + 10)
    if tartaruga.ycor() > 191:
        tartaruga.sety(191)

def baixo():
    tartaruga.goto(tartaruga.xcor(), tartaruga.ycor() - 10)
    if tartaruga.ycor() < -191:
        tartaruga.sety(-191)

#definir morte e akimentacao da tartaruga
def morte():
    global vidas 
    if tartaruga.distance(veneno)<25:
        vidas -= 1
        veneno.goto(random.randint(-200, 200), random.randint(-200, 200))
    if vidas == 2:
        vidav3.hiderturtle()
    if vidas == 1:
        vidav2.hiderturtle()
    if vidas == 0:
        vidav1.hiderturtle()
        tela.bye()

def alimentacao():
    global pontos 
    if tartaruga.distance(comida)<25:
        vidas += 1
        apagarpontos()
        escreverpontos()
        comida.goto(random.randint(-200, 200), random.randint(-200, 200))

#definir movimentacao automatica da comida e do veneno
def automovi():
    comida.bk(5)
    limite(comida)
    alimentacao()

    veneno.fd(5)
    limite(veneno)
    morte()

    turtle.ontimer(automovi(), 1000//24)

#definir limites da movimentacao automatica
def limite(obj):
    if 199 < obj.ycor():
        obj.sety(199)
        obj.left(random.randint(0,180))
    if -199 > obj.ycor():
        obj.sety(-199)
        obj.left(random.randint(0,180))
    if -199 > obj.xcor():
        obj.setx(-199)
        obj.left(random.randint(0,180))
    if 199 < obj.xcor():
        obj.setx(199)
        obj.left(random.randint(0,180))

#criar parede
desenhaparede()

#criar letreiro
letreiro = turtle.Turtle()
letreiro.speed(0)
letreiro.penup()
letreiro.hideturtle
letreiro.goto(0, 200)
letreiro.write('pontos: ', align='center', font=16)

#criar placar
poontos = 0
placar = turtle.Turtle()
placar.speed(0)
placar.goto(0,0)
placar.pensize(0)
placar.penup()
placar.pendown
placar.hideturtle

def escreverpontos():
    placar_write = pontos 
    placar.write(placar_write)

def apagarpontos():
    placar.undo()
    placar.setposition(25, 200)

#criar vidas da tartaruga
vidas = 3

vidav1 = turtle.Turtle()
vidav1.shape('turtle')
vidav1.color('sea green')
vidav1.penup()
vidav1.goto(-199, 211)
vidav1.speed(0)

vidav2 = turtle.Turtle()
vidav2.shape('turtle')
vidav2.color('sea green')
vidav2.penup()
vidav2.goto(-179, 211)
vidav2.speed(0)

vidav3 = turtle.Turtle()
vidav3.shape('turtle')
vidav3.color('sea green')
vidav3.penup()
vidav3.goto(-159, 211)
vidav3.speed(0)

#criar tartaruga
tartaruga = turtle.Turtle
tartaruga.shape('turtle')
tartaruga.color('sea green')
tartaruga.penup()
turtle.onkeypress(cima, 'Up')
turtle.onkeypress(baixo, 'Down')
turtle.onkeypress(esquerda, 'Left')
turtle.onkeypress(baixo, 'Right')
turtle.listen()

#criar comida e veneno
comida = turtle.Turtle
comida.shape('circle')
comida.color('crimson')
comida.penup()
comida.speed(10)
comida.setposition(random.randint(-200, 200), random.randint(-200, 200))

veneno = turtle.Turtle
veneno.shape('circle')
veneno.color('purple')
veneno.penup()
veneno.speed(10)
veneno.setposition(random.randint(-200, 200), random.randint(-200, 200))

automovi()

#manter tela aberta
tela.mainloop()
