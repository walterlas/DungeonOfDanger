#a=[]
#for i in range(0,26):
#	a.append(i)

def createGrid(x,y):
	grid=[]
	for i in range(0,x*y):
		grid.append(i)
	return(grid)
	
def getIndex(x,y,columns):
	i=x+(columns*y)
	return(i)

def getX(i,columns):
	x=i%columns
	return(x)

def getY(i,columns):
	y=i//columns
	return(y)

def getXY(i,columns):
	x=i%columns
	y=i//columns
	xy=[x,y]
	return(xy)
	
def showGrid(grid,col):
	index=0
	for ol in range(0,col):
		for il in range(0,col):
			print('{0:2d}'.format(grid[index]),end=" ")
			index=index+1
		print("\n")
	return

def centerText(string,col):
	numspaces = len(string)-(col/2)
	

