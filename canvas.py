from tkinter import*
import time

from sprite.sprite import sprite
import random
from evemy.evemy_mob import mobs
class canvas(Canvas):
    def __init__(self):
        self.root=Tk()
        self.root.title('Shoot-the-enemy2')
        super(canvas,self).__init__(self.root,width=640,height=480,bg='#ffffff')
        self.pack()
        self.setp()
        self.time=0
        while True :
            self.loop()
            self.root.update()
            self.time+=1
            time.sleep(0.01)
        self.root.mainloop()
    
    def setp(self):
        self.sprite=sprite(self)
        self.mobs=mobs(self)
        self.dk=0
        self.asd=0

    def loop(self):
        if self.sprite.asd>1:
            self.sprite.loop(self.asd)
            if self.time % 5==0:
                if self.time<500:
                    self.dk+=0.5
                elif self.time>500 and self.time<3000:
                    self.dk+=1
                elif self.time>3000 and self.time<5000:
                    self.dk+=2.5
                else:
                    self.dk+=4
                if self.dk>1:
                    self.ra=random.randint(1,int(self.dk))%33
                    self.dk-=self.ra
                    self.mobs.ud(self.ra)
            self.asd=self.mobs.loop(self.sprite.xy,self.sprite.xys)
        else:
            self.create_text(240,320,text='你輸了'+str(self.time/100))
            while True:
                pass