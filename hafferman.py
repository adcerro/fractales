from textwrap import fill
from turtle import *
reset()
setworldcoordinates(0,900,900,0)
def hafferman(n):
    xparts=window_width()//n**2
    yparts=window_height()//n**2
    xi=0
    yi=0
    for i in range(n**2):
        for j in range(n**2):
            if(j%2==0 and i%2==0):
                boxdraw(xi,yi,xparts,yparts,"black")
                xi=xi+xparts
            if(j%2!=0 and i%2==0):
                boxdraw(xi,yi,xparts,yparts,"white")
                xi=xi+xparts
            if(j%2==0 and i%2!=0):
                boxdraw(xi,yi,xparts,yparts,"white")
                xi=xi+xparts
            if(j%2!=0 and i%2!=0):
                boxdraw(xi,yi,xparts,yparts,"black")
                xi=xi+xparts
        xi=0
        yi=yi+yparts
def ha(n):
    if(n==1):
        boxdraw(window_width()//2,window_height()//2,window_width()//n,window_height()//n,"black")
    else:
        boxdraw(window_width()//n,window_height()//n,window_width()//n**2,window_height()//n**2,"black")
        boxdraw(window_width()//n+2*window_width()//n**2,window_height()//n+window_height()//n**2,window_width()//n**2,window_height()//n**2,"black")
        boxdraw(window_width()//n+window_width()//n**2,window_height()//n+2*window_height()//n**2,window_width()//n**2,window_height()//n**2,"black")
        boxdraw(window_width()//n+2*window_width()//n**2,window_height()//n+2*window_height()//n**2,window_width()//n**2,window_height()//n**2,"black")
        boxdraw(window_width()//n+2*window_width()//n**2,window_height()//n+3*window_height()//n**2,window_width()//n**2,window_height()//n**2,"black")
        boxdraw(window_width()//n+3*window_width()//n**2,window_height()//n+2*window_height()//n**2,window_width()//n**2,window_height()//n**2,"black")
        boxdraw(window_width()//n+3*window_width()//n**2,window_height()//n+3*window_height()//n**2,window_width()//n**2,window_height()//n**2,"black")
        
        ha(n-1)

def haf(x,y,a,b,n):
    if(n==1):
        boxdraw(x,y,a,b,"black")
    else:
        boxdraw(x,y,a,b,"white")
        haf(x+a,y+b,a,b,n-1)
        haf(x+a,y,a,b,n-1)
        haf(x,y+b,a,b,n-1)

def haf2(n):
    xparts=window_width()//n**2
    yparts=window_height()//n**2
    xi=0
    yi=0
    haf(xi,yi,xparts,yparts,n)

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

speed(0) 
#hafferman(5)
#hafferman(2)  
ha(3)      
mainloop()