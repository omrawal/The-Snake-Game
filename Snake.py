import pygame
import random

pygame.init()

win=pygame.display.set_mode((500,500))
pygame.display.set_caption("Snake")

#     0
# 1       2
#     3


current_dir=2
x=200
y=200
size=35
vel=2
pos_lst=[(x,y)]
score=0
fruit_eaten=True
run=True
while run:
    pygame.time.delay(100)
    if fruit_eaten==True:
        fruit_x=random.randint(50,440)
        fruit_y=random.randint(50,440)
        while(((fruit_x ,fruit_y )in pos_lst) ):
            fruit_x=random.randint(50,440)
            fruit_y=random.randint(50,440)
        fruit_eaten=False
    if(x>500 or y>500 or x<0 or y<0):
        run=False
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            if current_dir!=1 and current_dir!=2:
                current_dir=1
        if event.key == pygame.K_RIGHT:
            if current_dir!=2 and current_dir!=1:
                current_dir=2
        if event.key == pygame.K_UP:
            if current_dir!=0 and current_dir!=3:
                current_dir=0
        if event.key == pygame.K_DOWN:
            if current_dir!=3 and current_dir!=0:
                current_dir=3
    if(current_dir==0):
        y-=vel
        x=pos_lst[-1][0]
        if(((fruit_x-10)< x <(fruit_x+10)) and ( (fruit_y-10)< y <(fruit_y+10) ) ):
            score+=1
            size+=5
            vel+=1
            fruit_eaten=True
        if((x,y)in pos_lst):
            break
        if(len(pos_lst)<size):
            pos_lst.append((x,y))
        else:
            pos_lst.pop(0)
            pos_lst.append((x,y))
    if(current_dir==1):
        x-=vel
        y=pos_lst[-1][1]
        if(((fruit_x-10)< x <(fruit_x+10)) and ( (fruit_y-10)< y <(fruit_y+10) ) ):
            score+=1
            size+=5
            vel+=1
            fruit_eaten=True

        if((x,y)in pos_lst):
            break
        if(len(pos_lst)<size):
            pos_lst.append((x,y))
        else:
            pos_lst.pop(0)
            pos_lst.append((x,y))
    if(current_dir==2):
        x+=vel
        y=pos_lst[-1][1]
        if(((fruit_x-10)< x <(fruit_x+10)) and ( (fruit_y-10)< y <(fruit_y+10) ) ):
            score+=1
            size+=5
            vel+=1
            fruit_eaten=True
        if((x,y)in pos_lst):
            break
        if(len(pos_lst)<size):
            pos_lst.append((x,y))
        else:
            pos_lst.pop(0)
            pos_lst.append((x,y))
    if(current_dir==3):
        y+=vel
        if(((fruit_x-10)< x <(fruit_x+10)) and ( (fruit_y-10)< y <(fruit_y+10) ) ):
            score+=1
            size+=5
            vel+=1
            fruit_eaten=True
        if((x,y)in pos_lst):
            break
        x=pos_lst[-1][0]
        if(len(pos_lst)<size):
            pos_lst.append((x,y))
        else:
            pos_lst.pop(0)
            pos_lst.append((x,y))
    win.fill((0,0,0))
    
    pygame.draw.circle(win, (255, 0, 0), (fruit_x,fruit_y), 10)
    for i,tup in enumerate(pos_lst):
        x1,y1=tup
        if (i==(size-1)):
            pygame.draw.circle(win, (14, 133, 1), (x1,y1), 8)
        else:
            # pygame.draw.circle(win, (0,255,0), (x1-(i+1)*15,y1), 10)
            pygame.draw.circle(win, (0,255,0), (x1,y1), 8)
    font=pygame.font.SysFont('calibri',30,True)
    if(score<10):
        text=font.render('SCORE:'+str(score),1,(0,0,225))
    elif(13>score>9):
        text=font.render('SCORE:'+str(score)+' Godlike',1,(0,0,225))
    else:
        text=font.render('SCORE:'+str(score)+' Just Die',1,(0,0,225))    
    win.blit(text,(240,10))
    pygame.display.update()

pygame.quit()