import turtle

def drawPolygon(t, sideLength, numSides):
    for i in range(numSides):
        t.forward(sideLength)
        t.left(360/numSides)

def Main(): # I only feel like doing this so moving to another language like c++ (cpp) can be easier
  wn = turtle.Screen()
  geo = turtle.Turtle()
  
  user_shape = int(input("Enter the length of the side(s) > "))
  user_sidenumber = int(input("Enter the number of sides > "))
  
  drawPolygon(geo, user_shape, user_sidenumber)
  #drawPolygon(geo, 30, 10)  # draw a decagon
  
  wn.exitonclick()

Main()
