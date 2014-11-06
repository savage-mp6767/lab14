#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in colision detection - and STOP the target when you catch it!

from Tkinter import *
import math
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")
direction = -10

class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
	        self.w = 480
	        self.h = 320
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.up = Button(self.myContainer1)
       	        self.up.configure(text="up", background= "green")
       	        self.up.grid(row=0,column=0)
       	        # Bind an event to the first button
       	        self.up.bind("<Button-1>", self.upClicked)
       	    
       	        self.down = Button(self.myContainer1)
       	        self.down.configure(text="down", background= "green")
       	        self.down.grid(row=0,column=1)
       	        self.down.bind("<Button-1>", self.downClicked)
       	    
       	        self.left = Button(self.myContainer1)
       	        self.left.configure(text="left", background= "green")
       	        self.left.grid(row=0,column=2)
       	        self.left.bind("<Button-1>", self.leftClicked)
       	    
       	        self.right = Button(self.myContainer1)
       	        self.right.configure(text="right", background= "green")
       	        self.right.grid(row=0,column=3)
       	        self.right.bind("<Button-1>", self.rightClicked)
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		
        def regObj(self,obj):
                self.objects.append(obj)
		
        def upClicked(self, event): 
                if self.edgeDetect():
                    global oval
                    global player
                    drawpad.move(player,0,-20)
	  
        def downClicked(self, event):   
                if self.edgeDetect():
                    global oval
                    global player
                    drawpad.move(player,0,20)
	   
        def leftClicked(self, event):
                if self.edgeDetect():  
                    global oval
                    global player
                    drawpad.move(player,-20,0)
	   
        def rightClicked(self, event):
                if self.edgeDetect():  
                    global oval
                    global player
                    drawpad.move(player,20,0)
        
	def collisionDetect(self):
                global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player) #top left, top right, bottom left, bottom right
                plyW = x2 - x1
                plyH = y2 - y1
                tx1,ty1,tx2,ty2 = drawpad.coords(target)
                tarW = tx2 - tx1
                tarH = ty2 - ty1
                #this.Max.X < other.Min.X || min top left 

                #this.Max.Y < other.Min.Y || max bottom right
                #this.Min.X > other.Max.X || 
                #this.Min.Y > other.Max.Y) 
                #if abs(x1 - tx1) < plyW + tarW:
                #    if abs(y1 - ty1) < plyH + tarH:
                #        return True
                if x1 > tx1 or x1 == tx1:
                    if y1 > ty1 or y1 == ty1:
                        if x2 < tx2 + tarW or x2 == tx2:
                            if y2 < ty2 + tarH or y2 == ty2:
                                return True
                return False
                #fix this gay edge detection shit
        def edgeDetect(self):
            global drawpad
            x1,y1,x2,y2 = drawpad.coords(player)
            if x2 > drawpad.winfo_width(): 
                return False
            elif x1 > 0:
                return False
            elif y1 > drawpad.winfo_height():
                return False
            elif y2 < 0:
                return False
            return True
                
        # Ensure that we are doing our collision detection
	# After we move our object!
	def Update(self):
	    global drawpad
	    global target
	    global direction
            col = self.collisionDetect()
            self.edgeDetect()
            if col:
                drawpad.itemconfig(target,fill='red')
            else:
                drawpad.itemconfig(target,fill='blue')
                self.targetAnim()
                
            drawpad.after(1,self.Update)
	# Use a function to do our collision detection
	# This way we only have to write it once, and call it from
	# every button click function.
	def targetAnim(self):
	    global direction
	    global target
	    global drawpad
	    x1, y1, x2, y2 = drawpad.coords(target)
            if x2 > drawpad.winfo_width(): 
                direction = -direction
            elif x1 < 0:
                direction = -direction
            drawpad.move(target,direction,0)
		
myapp = MyApp(root)
myapp.Update()
root.mainloop()