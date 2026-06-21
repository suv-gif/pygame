import pgzrun
import pgzero.screen
import random
WIDTH=600
HEIGHT=600
score=0
#making the satelite
player=Actor("satelite",(300,200))
v1=Actor("virus",(400,200))
score=0
#draw
def draw():
    screen.clear()
    screen.fill("black")
    player.draw()
    v1.draw()
    screen.draw.text("score={}".format(score),(10,10),color="white")
def update():
    global score
    if player.colliderect(v1):
        v1.x=random.randint(50,550)
        v1.y=random.randint(50,550)
        score= score+1
def on_mouse_move(pos):
    player.pos=pos
pgzrun.go()