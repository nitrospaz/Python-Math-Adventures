# set range of x values
xmin = -10
xmax = 10

# set range of y-values
ymin = -10
ymax = 10

# calculate the range
rangex = xmax - xmin
rangey = ymax - ymin

def setup():
    global xscl, yscl
    size(600,600) # total screen size
    xscl = width / rangex # calculating scaling for the x axis
    yscl = -height / rangey # calculating the scaling for the y axis
    
def draw():
    global xscl, yscl
    background(255) # white
    translate(width/2,height/2) # move origin from top left
    grid(xscl,yscl)
    graphFunction()
    
def f(x):
    # INSERT EQUATION BELOW
    return sin(x)

def graphFunction():
    x = xmin
    while x <= xmax:
        stroke(255,0,0)
        fill(0)
        line(x*xscl,f(x)*yscl,(x+0.1)*xscl,f(x+0.1)*yscl)
        x += 0.1
        
def grid(xscl,yscl):
    #draw grid for graphing
    #cayan lines
    strokeWeight(1) #line weight
    stroke(0,255,255) #RGB value
    for i in range(xmin,xmax + 1):
        line(i*xscl,ymin*yscl,i*xscl,ymax*yscl)
    for i in range(ymin,ymax+1):
        line(xmin*xscl,i*yscl,xmax*xscl,i*yscl)
    stroke(0) #black axis
    line(0,ymin*yscl,0,ymax*yscl)
    line(xmin*xscl,0,xmax*xscl,0)
    
    
