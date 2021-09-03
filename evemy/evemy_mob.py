from evemy.mobs.none.aa.mob1 import *
from evemy.mobs.none.aa.mob2 import *
from evemy.mobs.none.aa.mob3 import *
from evemy.mobs.none.aa.mob4 import *
from evemy.mobs.none.ab.mob5 import *
from evemy.mobs.none.ab.mob6 import *
from evemy.mobs.none.ab.mob7 import *
from evemy.mobs.none.ab.mob8 import *
from evemy.mobs.none.ba.mob9 import *
from evemy.mobs.none.ba.mob10 import *

class mobs:
    def __init__(self,canvas):
        self.c=canvas
        self.mob1=mob1(self.c)
        self.mob2=mob2(self.c)
        self.mob3=mob3(self.c)
        self.mob4=mob4(self.c)
        self.mob5=mob5(self.c)
        self.mob6=mob6(self.c)
        self.mob7=mob7(self.c)
        self.mob8=mob8(self.c)
        self.mob9=mob9(self.c)
        self.mob10=mob10(self.c)

    def ud(self,rk):
        if rk==1:
            self.mob1.ud()
        elif rk==2:
            self.mob2.ud()
        elif rk==3:
            self.mob3.ud()
        elif rk==4:
            self.mob4.ud()
        elif rk==5:
            self.mob5.ud()
        elif rk==6:
            self.mob6.ud()
        elif rk==7:
            self.mob7.ud()
        elif rk==8:
            self.mob8.ud()
        elif rk==9:
            self.mob9.ud()
        elif rk==10:
            self.mob10.ud()
     