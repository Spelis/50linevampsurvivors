import pygame,random,math
def find_closest_enemy(bullet_position,enemies_positions):return min(enemies_positions,key=lambda enemy: ((enemy[0]-bullet_position[0]) ** 2+(enemy[1]-bullet_position[1]) ** 2) ** 0.5)
def move(x,y,tx,ty,speed):dx,dy=tx-x,ty-y;dirx,diry=dx / math.sqrt(dx*dx+dy*dy),dy / math.sqrt(dx*dx+dy*dy);x,y=x+dirx*speed*0.3,y+diry*speed*0.3;return x,y
screen,clock=pygame.display.set_mode((500,500)),pygame.time.Clock();info=[[],[0,0,0],[0,0],[],[]] #? 0: enemies. 1: player. 2: camera. 3: bullets
lerp=lambda start,end,t: start+(end-start)*t;frame=0;mkenemy=lambda: info[0].append([random.randint(info[1][0]-500,info[1][0]+500),random.randint(info[1][1]-500,info[1][1]+500)]) if abs(random.randint(info[1][0]-500,info[1][0]+500)-info[1][0]) > 100 and abs(random.randint(info[1][1]-500,info[1][1]+500)-info[1][1]) > 100 else None
while True:
    running=True
    while running:
        pygame.event.get()
        if frame % 15 == 10: mkenemy()
        if frame % 30 == 25:info[3].append([info[1][0],info[1][1],find_closest_enemy(info[1],info[0]),300]);info[4].append(pygame.Rect(info[1][0]+5,info[1][1]+15,5,5))
        info[1][0] += (int(pygame.key.get_pressed()[pygame.K_d])-int(pygame.key.get_pressed()[pygame.K_a]))*4;info[1][1] += (int(pygame.key.get_pressed()[pygame.K_s])-int(pygame.key.get_pressed()[pygame.K_w]))*4;info[2][0]=lerp(info[2][0],info[1][0],0.2);info[2][1]=lerp(info[2][1],info[1][1],0.2)
        for x in range(len(info[0])):
            info[0][x]=move(info[0][x][0],info[0][x][1],info[1][0],info[1][1],2);collindex=pygame.Rect(info[0][x][0],info[0][x][1],20,40).collidelist(info[4])
            if pygame.Rect(info[0][x][0],info[0][x][1],20,40).colliderect(pygame.Rect(info[1][0],info[1][1],20,40)):info=[[],[0,0,0],[0,0],[],[]];running=False;break
            if collindex != -1:info[0].pop(x);info[4].pop(collindex);info[3].pop(collindex);break
        screen.fill("green")
        for x in range(len(info[3])):info[3][x][0],info[3][x][1]=move(info[3][x][0],info[3][x][1],info[3][x][2][0],info[3][x][2][1],20);info[4][x]=pygame.Rect(info[3][x][0]+5,info[3][x][1]+15,10,10);pygame.draw.rect(screen,(255,255,255),info[4][x].move(-info[2][0]+260,-info[2][1]+270))
        [pygame.draw.rect(screen,(0,128,0),pygame.Rect(info[0][x][0]-info[2][0]+260,info[0][x][1]-info[2][1]+270,20,40)) for x in range(len(info[0]))];pygame.draw.rect(screen,(0,0,0),pygame.Rect(info[1][0]-info[2][0]+260,info[1][1]-info[2][1]+270,20,40));pygame.display.flip();clock.tick(30);frame+=1
