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
from evemy.mobs.none.ba.mob11 import *
from evemy.mobs.none.ba.mob12 import *
from evemy.mobs.none.bb.mob13 import *
from evemy.mobs.none.bb.mob14 import *
from evemy.mobs.none.bb.mob15 import *
from evemy.mobs.none.bb.mob16 import *
from evemy.mobs.speed.aa.mob17 import *
from evemy.mobs.speed.aa.mob18 import *
from evemy.mobs.speed.aa.mob19 import *
from evemy.mobs.speed.aa.mob20 import *
from evemy.mobs.speed.ab.mob21 import *
from evemy.mobs.speed.ab.mob22 import *
from evemy.mobs.speed.ab.mob23 import *
from evemy.mobs.speed.ab.mob24 import *
from evemy.mobs.speed.ba.mob25 import *
from evemy.mobs.speed.ba.mob26 import *
from evemy.mobs.speed.ba.mob27 import *
from evemy.mobs.speed.ba.mob28 import *
from evemy.mobs.speed.bb.mob29 import *
from evemy.mobs.speed.bb.mob30 import *
from evemy.mobs.speed.bb.mob31 import *
from evemy.mobs.speed.bb.mob32 import *

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
        self.mob11=mob11(self.c)
        self.mob12=mob12(self.c)
        self.mob13=mob13(self.c)
        self.mob14=mob14(self.c)
        self.mob15=mob15(self.c)
        self.mob16=mob16(self.c)
        self.mob17=mob16(self.c)
        self.mob18=mob16(self.c)
        self.mob19=mob16(self.c)
        self.mob20=mob16(self.c)
        self.mob21=mob16(self.c)
        self.mob22=mob16(self.c)
        self.mob23=mob16(self.c)
        self.mob24=mob16(self.c)
        self.mob25=mob16(self.c)
        self.mob26=mob16(self.c)
        self.mob27=mob16(self.c)
        self.mob28=mob16(self.c)
        self.mob29=mob16(self.c)
        self.mob30=mob16(self.c)
        self.mob31=mob16(self.c)
        self.mob32=mob16(self.c)

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
        elif rk==11:
            self.mob11.ud()
        elif rk==12:
            self.mob12.ud()
        elif rk==13:
            self.mob13.ud()
        elif rk==14:
            self.mob14.ud()
        elif rk==15:
            self.mob15.ud()
        elif rk==16:
            self.mob16.ud()
        elif rk==17:
            self.mob17.ud()
        elif rk==18:
            self.mob18.ud()
        elif rk==19:
            self.mob19.ud()
        elif rk==20:
            self.mob20.ud()
        elif rk==21:
            self.mob21.ud()
        elif rk==22:
            self.mob22.ud()
        elif rk==23:
            self.mob23.ud()
        elif rk==24:
            self.mob24.ud()
        elif rk==25:
            self.mob25.ud()
        elif rk==26:
            self.mob26.ud()
        elif rk==27:
            self.mob27.ud()
        elif rk==28:
            self.mob28.ud()
        elif rk==29:
            self.mob29.ud()
        elif rk==30:
            self.mob30.ud()
        elif rk==31:
            self.mob31.ud()
        elif rk==32:
            self.mob32.ud()
     
    def loop(self,spritexy,sixy):
        self.asd=0
        self.asd+=self.mob1.loop(spritexy,sixy)
        self.asd+=self.mob2.loop(spritexy,sixy)
        self.asd+=self.mob3.loop(spritexy,sixy)
        self.asd+=self.mob4.loop(spritexy,sixy)
        self.asd+=self.mob5.loop(spritexy,sixy)
        self.asd+=self.mob6.loop(spritexy,sixy)
        self.asd+=self.mob7.loop(spritexy,sixy)
        self.asd+=self.mob8.loop(spritexy,sixy)
        self.asd+=self.mob9.loop(spritexy,sixy)
        self.asd+=self.mob10.loop(spritexy,sixy)
        self.asd+=self.mob11.loop(spritexy,sixy)
        self.asd+=self.mob12.loop(spritexy,sixy)
        self.asd+=self.mob13.loop(spritexy,sixy)
        self.asd+=self.mob14.loop(spritexy,sixy)
        self.asd+=self.mob15.loop(spritexy,sixy)
        self.asd+=self.mob16.loop(spritexy,sixy)
        self.asd+=self.mob17.loop(spritexy,sixy)
        self.asd+=self.mob18.loop(spritexy,sixy)
        self.asd+=self.mob19.loop(spritexy,sixy)
        self.asd+=self.mob20.loop(spritexy,sixy)
        self.asd+=self.mob21.loop(spritexy,sixy)
        self.asd+=self.mob22.loop(spritexy,sixy)
        self.asd+=self.mob23.loop(spritexy,sixy)
        self.asd+=self.mob24.loop(spritexy,sixy)
        self.asd+=self.mob25.loop(spritexy,sixy)
        self.asd+=self.mob26.loop(spritexy,sixy)
        self.asd+=self.mob27.loop(spritexy,sixy)
        self.asd+=self.mob28.loop(spritexy,sixy)
        self.asd+=self.mob29.loop(spritexy,sixy)
        self.asd+=self.mob30.loop(spritexy,sixy)
        self.asd+=self.mob31.loop(spritexy,sixy)
        self.asd+=self.mob32.loop(spritexy,sixy)
        return self.asd