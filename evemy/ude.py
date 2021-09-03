import random as ra

def loop(items,canvas,randomm,spritexy):
    for item in range(len(items)):
        if item<len(items):
            xy=canvas.coords(items[item][0])
            if  xy[0]<0:
                canvas.move(items[item][0],10,0)
            elif  xy[2]>640:
                canvas.move(items[item][0],-10,0)
            elif  xy[1]<0:
                canvas.move(items[item][0],0,10)
            elif  xy[3]>480:
                canvas.move(items[item][0],0,-10)
            else:
                random=ra.randint(1,randomm)
                if random==1:
                    random=ra.randint(1,3)
                    if random==1:
                        random=ra.randint(1,2)
                        xy=canvas.coords(items[item][0])
                        if random==1:
                            if ((spritexy[0]+spritexy[2])//2)>((xy[0]+xy[2])//2):
                                canvas.move(items[item][0],10,0)
                            else:
                                canvas.move(items[item][0],-10,0)
                        else:
                            if ((spritexy[1]+spritexy[3])//2)>((xy[1]+xy[3])//2):
                                canvas.move(items[item][0],0,10)
                            else:
                                canvas.move(items[item][0],0,-10)
                    else:
                        random=ra.randint(1,4)
                        if random==1:
                            canvas.move(items[item][0],0,-10)
                        elif random==2:
                            canvas.move(items[item][0],10,0)
                        elif random==3:
                            canvas.move(items[item][0],0,10)
                        else:
                            canvas.move(items[item][0],-10,0)

def ud(items,canvas):
    randomt=ra.randint(1,2)
    if randomt==1:
        randomt=ra.randint(1,2)
        if randomt==1:
            randomt=ra.randint(0,590)
            items.append([canvas.create_rectangle(randomt,-50,randomt+50,0),0])
        else:
            randomt=ra.randint(0,590)
            items.append([canvas.create_rectangle(randomt,480,randomt+50,530),0])
    else:
        randomt=ra.randint(1,2)
        if randomt==1:
            randomt=ra.randint(0,430)
            items.append([canvas.create_rectangle(-50,randomt,0,randomt+50),0])
        else:
                randomt=ra.randint(0,590)
                items.append([canvas.create_rectangle(640,randomt,690,randomt+50),0])
    return items