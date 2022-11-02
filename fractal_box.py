from turtle import *
def fractal_box(n):
    if(n>1):
        color("blue")
        forward(20)
        left(90)
        forward(20)
        right(90)
        fractal_box(n-1)
    
   
    color("yellow")
    right(90)
    forward(20)
    left(90)
    forward(20)
    
    
    return
reset()
setworldcoordinates(0,0,200,200) 
fractal_box(6)
speed(1)
mainloop()