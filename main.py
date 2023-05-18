import turtle
#from unidecode import unidecode
import pandas

screen = turtle.Screen()
screen.title("blank_states_img")
image = "Brazil Blank States2.gif"
screen.addshape(image)

turtle.shape(image)

#import turtle

#def get_mouse_click_coor(x, y):
#    print(x, y)

#turtle.onscreenclick(get_mouse_click_coor)

#turtle.mainloop()

game_is_on = True
estados_adivinhados = 0

df_estados = pandas.read_csv('brazil.csv', delimiter=';')

#Criando a lista com estados
lista_estados = df_estados["state"].to_list()

#Tornando todos os elementos em lowe case
lista_estados_lower = [element.lower() for element in lista_estados]

while game_is_on:
    answer_state = screen.textinput(title = "Adivinhe o Estado", prompt=f"({estados_adivinhados}/26) Qual é o nome de outro estado?")
    if answer_state.lower() in lista_estados_lower:
        estados_adivinhados +=1
        t = turtle.Turtle()
        t.color("green")
        t.hideturtle()
        t.penup()
        index = lista_estados_lower.index(answer_state.lower())
        nome_estado = df_estados.iloc[index]
        t.goto(nome_estado["x"],nome_estado["y"])
        t.write(nome_estado["state"], align="left", font=("Arial", 12, "normal"))
        lista_estados.remove(lista_estados[index])
        lista_estados_lower.remove(lista_estados_lower[index])
    if lista_estados ==26:
        game_is_on = False
    if answer_state =="end":
        game_is_on = False

print(lista_estados)
        

screen.exitonclick()






