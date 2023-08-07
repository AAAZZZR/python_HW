import turtle
def spiral():
    for i in range(1,11):
        turtle.forward(50*i)
        turtle.left(90)
        turtle.forward(50*i)
        turtle.left(90)
  
      
turtle.exitonclick()



if __name__ == "__main__" :
 spiral()