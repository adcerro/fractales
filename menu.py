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
        if(n==0):
            area=0
        else:
            area =((-7*(size**2)/9)-(size**2)*(1/9**n-1))/(size**2)*100
        print(f'Area ocuapada(blanco): {area}%')
    else:
        print('n no valido')

def hafferman(n):
    setworldcoordinates(0,n*100,n*100,0)
    boxdraw(0,0,n*100,n*100,'black')
    mainloop()

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
    print('2- Indefinido')
    opt = int(input('Seleccione una opción: '))
    if(opt>2 or opt<1):
        opt=0

if(opt==1):
    n = int(input('Digite n mayor o igual a 0: '))
    sierpinsky(n)
    