import random
import evemy.ude as ude
from evemy.evemy_sis.si1 import si1
from evemy.evemy_sis.si2 import si2

class mob9:
    def __init__(self,canvas,ife=1,sk=30,uf=100,rk=1):
        self.canvas=canvas
        self.items=[]
        self.sk=sk
        self.uf=uf
        self.rk=rk
        if ife==1:
            self.si=si1(self.canvas)
        else:
            self.si=si2(self.canvas)
    def ud(self):
        self.items=ude.ud(self.items,self.canvas)

    def loop(self,spritexy,sixy):
        ude.loop(self.items,self.canvas,self.sk,spritexy)
        for itme in self.items:
            self.random=random.randint(1,self.uf)
            if self.random==1:
                for t in range(self.rk):
                    self.random=random.randint(1,4)
                    self.xy=self.canvas.coords(itme[0])
                    if self.random==1:
                        self.xy=[self.xy[0],self.xy[1]-20,self.xy[0]+5,self.xy[1],[0,-1]]
                        self.si.ud(self.xy)
                        self.xy=[self.xy[2]+5,self.xy[1]-20,self.xy[0],self.xy[1],[0,-1]]
                        self.si.ud(self.xy)
                    elif self.random==2:
                        self.xy=[self.xy[2]+20,self.xy[1],self.xy[2],self.xy[1]-5,[1,0]]
                        self.si.ud(self.xy)
                        self.xy=[self.xy[2]+20,self.xy[3]-5,self.xy[2],self.xy[1],[1,0]]
                        self.si.ud(self.xy)
                    elif self.random==3:
                        self.xy=[self.xy[0],self.xy[1],self.xy[0]+5,self.xy[1]+20,[0,1]]
                        self.si.ud(self.xy)
                        self.xy=[self.xy[2]-5,self.xy[1],self.xy[0],self.xy[1]+20,[0,1]]
                        self.si.ud(self.xy)
                    else:
                        self.xy=[self.xy[2]-20,self.xy[1],self.xy[2],self.xy[1]+5,[-1,0]]
                        self.si.ud(self.xy)
                        self.xy=[self.xy[2]-20,self.xy[3]-5,self.xy[2],self.xy[1],[-1,0]]
                        self.si.ud(self.xy)
        for item in range(len(self.items)):
            if item<len(self.items):
                for sixyy in sixy:
                    self.xy=self.canvas.coords(self.items[item][0])
                    if sixyy[2]>self.xy[0] and self.xy[2]>sixyy[0] and sixyy[1]<self.xy[3] and self.xy[1]<sixyy[3]:
                        self.canvas.delete(self.items[item][0])
                        del self.items[item]
        return self.si.move(spritexy)