import random

smokeList = []
smokeListDel = []
smokeTimer=0
smokeMovementTimer=0

UFOList=[]
UFOListDel=[]
UFOTimer=0

def smoke(X,Y,speed,movement):
    global smokeList,smokeListDel,smokeTimer,smokeMovementTimer
    background(255)
    fill(0)
    quad(800,900,1100,900,1000,200,900,200)
    smokeTimer=(smokeTimer+1)%12
    if(smokeTimer==11):
        smokeList.append([950,200,X,Y,movement])
    for el in smokeList:
        if(el[1]>0):
            fill(128,128,128)
            ellipse(el[0],el[1],el[2],el[3])
            el[1]-= speed
            smokeMovementTimer=(smokeMovementTimer+1)%2
            if(smokeMovementTimer==0):
                el[0]+=movement
        else:
            smokeListDel.append(el)
    try:
        for el in smokeListDel:
            if(len(smokeListDel)!=0):
                smokeList.remove(el)
    except:
        pass

def UFOS(X,Y,direction):
    global UFOList,UFOListDel,UFOTimer
    background(20)
    UFOTimer=(UFOTimer+1)%60
    if(UFOTimer==59):
        UFOList.append([X,Y,direction])
    for UFOS in UFOList:
        if(UFOS[1]>0):
            fill(128,128,128)
            ellipse(UFOS[0],UFOS[1],100,50)
            UFOS[0]+= UFOS[2]
        else:
            UFOSListDel.append(UFOS)
    try:
        for UFOS in UFOListDel:
            if(len(UFOListDel)!=0):
                UFOList.remove(UFOS)
    except:
        pass


def setup():
    size(1200,900)
    
def draw():
    global smokeTimer
    smokeRandomWidth=random.randint(50,100)
    smokeRandomHeight=random.randint(40,80)
    smokeRandomSpeed=random.randint(1,5)
    smokeMovement=random.randint(-1,1)
    
    UFORandom=random.randint(0,1)
    UFOY=random.randint(100,300)
    if(UFORandom==1):
        UFOX=0
        UFODirection=3
    else:
        UFOX=1200
        UFODirection=-3
    UFOS(UFOX,UFOY,UFODirection)
    smoke(smokeRandomWidth,smokeRandomHeight,smokeRandomSpeed,smokeMovement)
