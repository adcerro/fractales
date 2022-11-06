import numpy as np
from PIL import Image
from turtle import *
def sierpinsky(n):
    if(n>=0):
        #code  to draw the carpet taken from https://www.geeksforgeeks.org/python-sierpinski-carpet/  
        size = 3**n
  
        square = np.empty([size, size, 3], dtype = np.uint8)
        color = np.array([255, 255, 255], dtype = np.uint8)
  
        square.fill(0)
  
        for i in range(0, n + 1):
            stepdown = 3**(n - i)
            for x in range(0, 3**i):
          
                if x % 3 == 1:
                    for y in range(0, 3**i):
                        if y % 3 == 1:
                      
                            square[y * stepdown:(y + 1)*stepdown, x * stepdown:(x + 1)*stepdown] = color
    

        Image.fromarray(square).save("sierpinski.jpg")
  
        i = Image.open("sierpinski.jpg")
        i.show()
        f=np.zeros(n+2)
        f[0]=0
        for i in range(1,n+1):
            f[i] = f[i-1]+8**(i-1)/9**(i)
        area =f[n]
        print(f'Area ocuapada(blanco): {area}%')
    else:
        print('n no valido')

def hafferman(n):
    speed(0)
    setworldcoordinates(0,n*100,n*100,0)
    boxdraw(0,0,n*100,n*100,'black')
    haff(n,n*49,n*49,n*100)
    mainloop()

def haff(n,x,y,a):
    divide = a//3
    boxdraw(x,y,divide,divide,'white')
    if(n>0):
        haff(n-1,x+divide,y+divide,divide)

def boxdraw(x,y,a,b,color):
    up()
    goto(x,y)
    down()
    begin_fill()
    left(90) 
    forward(b)
    right(90)
    forward(a)
    right(90)   
    forward(b)
    fillcolor(color)
    right(90)
    forward(a)
    right(180)
    end_fill()

opt=0
while(opt==0):
    print('Menu')
    print('1- Sirpinsky')
    print('2- Hafferman')
    opt = int(input('Seleccione una opción: '))
    if(opt>2 or opt<1):
        opt=0

if(opt==1):
    n = int(input('Digite n mayor o igual a 0: '))
    sierpinsky(n)
else:
     n = int(input('Digite n mayor o igual a 1: '))
     hafferman(n)
    