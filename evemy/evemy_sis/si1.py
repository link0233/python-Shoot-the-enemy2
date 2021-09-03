class si1:
    def __init__(self,canvas,speed=3):
        self.canvas=canvas
        self.items=[]
        self.speed=speed
    
    def ud(self,xy):
        self.items.append([self.canvas.create_rectangle(xy[0],xy[1],xy[2],xy[3]),xy[4]])
    
    def move(self):
        for item in self.items:
            self.canvas.move(item[0],item[1][0]*self.speed,item[1][1]*self.speed)
        for item in range(len(self.items)):
            if item<len(self.items):
                self.xy=self.canvas.coords(self.items[item][0])
                if self.xy[0]<0 or self.xy[2]>640 or self.xy[1]<0 or self.xy[3]>480:
                    self.canvas.delete(self.items[item][0])
                    del self.items[item]