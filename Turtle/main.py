# from turtle import Turtle,Screen

# timmy = Turtle()
# timmy1 = Turtle()
# timmy1.shape("classic")
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy1.backward(200)
# timmy1.right(134)
# timmy1.forward(43)
# myscreen = Screen()
# myscreen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
print(table)
table.add_column("pokemon name",['pari','vallal','sasi','kala'])
table.add_column('age',[32,31,5,3])
table.align = "l"
print(table)