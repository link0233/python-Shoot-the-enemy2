from tkinter import*
import time

from sprite.sprite import sprite

from evemy.evemy_mob import mobs
class canvas(Canvas):
    def __init__(self):
        self.root=Tk()
        self.root.title('Shoot-the-enemy2')
        super(canvas,self).__init__(self.root,width=640,height=480,bg='#ffffff')
        self.pack()
        self.setp()
        while True :
            self.loop()
            self.root.update()
            time.sleep(0.01)
        self.root.mainloop()
    
    def setp(self):
        self.sprite=sprite(self)
        self.mobs=mobs(self)
        self.dk=0

    def loop(self):
        self.sprite.loop()
        self.dk+=1
        if self.dk>100:
            self.dk=0
            self.mobs.ud(9)
        self.mobs.loop(self.sprite.xy)