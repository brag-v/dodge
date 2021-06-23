# -*- coding: utf-8 -*-
"""
Created on Wed Jan  9 08:47:31 2019

@author: Brage Vik

cos(a) =
"""
from math import cos,sin,atan,radians,degrees
import pygame as pygame
from random import randint
pygame.init()

dance = (pygame.image.load("dans/dans1.png"),pygame.image.load("dans/dans2.png"),pygame.image.load("dans/dans3.png"),pygame.image.load("dans/dans4.png"),pygame.image.load("dans/dans5.png"),pygame.image.load("dans/dans6.png"),pygame.image.load("dans/dans7.png"),pygame.image.load("dans/dans8.png"),pygame.image.load("dans/dans9.png"),pygame.image.load("dans/dans10.png"),pygame.image.load("dans/dans11.png"),pygame.image.load("dans/dans12.png"),pygame.image.load("dans/dans13.png"),pygame.image.load("dans/dans14.png"),pygame.image.load("dans/dans15.png"),pygame.image.load("dans/dans16.png"),pygame.image.load("dans/dans17.png"),pygame.image.load("dans/dans18.png"),pygame.image.load("dans/dans19.png"))

bomb_h = (pygame.image.load("bomb/bomb_h/bomb_h1.png"),pygame.image.load("bomb/bomb_h/bomb_h2.png"),pygame.image.load("bomb/bomb_h/bomb_h3.png"),pygame.image.load("bomb/bomb_h/bomb_h4.png"),pygame.image.load("bomb/bomb_h/bomb_h5.png"),pygame.image.load("bomb/bomb_h/bomb_h6.png"),pygame.image.load("bomb/bomb_h/bomb_h7.png"),pygame.image.load("bomb/bomb_h/bomb_h8.png"),pygame.image.load("bomb/bomb_h/bomb_h9.png"),pygame.image.load("bomb/bomb_h/bomb_h10.png"),pygame.image.load("bomb/bomb_h/bomb_h11.png"),pygame.image.load("bomb/bomb_h/bomb_h12.png"),pygame.image.load("bomb/bomb_h/bomb_h13.png"),pygame.image.load("bomb/bomb_h/bomb_h14.png"))
bomb_v = (pygame.image.load("bomb/bomb_v/bomb_v1.png"),pygame.image.load("bomb/bomb_v/bomb_v2.png"),pygame.image.load("bomb/bomb_v/bomb_v3.png"),pygame.image.load("bomb/bomb_v/bomb_v4.png"),pygame.image.load("bomb/bomb_v/bomb_v5.png"),pygame.image.load("bomb/bomb_v/bomb_v6.png"),pygame.image.load("bomb/bomb_v/bomb_v7.png"),pygame.image.load("bomb/bomb_v/bomb_v8.png"),pygame.image.load("bomb/bomb_v/bomb_v9.png"),pygame.image.load("bomb/bomb_v/bomb_v10.png"),pygame.image.load("bomb/bomb_v/bomb_v11.png"),pygame.image.load("bomb/bomb_v/bomb_v12.png"),pygame.image.load("bomb/bomb_v/bomb_v13.png"),pygame.image.load("bomb/bomb_v/bomb_v14.png"))

knust = (pygame.image.load("knust/knust1.png"),pygame.image.load("knust/knust2.png"),pygame.image.load("knust/knust3.png"),pygame.image.load("knust/knust4.png"))

pause = (pygame.image.load("text/text1.png"),pygame.image.load("text/text2.png"))
game_over_text = (pygame.image.load("text/text3.png"),pygame.image.load("text/text4.png"))

cross = (pygame.image.load("items/items1.png"),pygame.image.load("items/items2.png"))
speed_arrow = (pygame.image.load("items/items3.png"),pygame.image.load("items/items4.png"))
lightning = (pygame.image.load("items/items5.png"),pygame.image.load("items/items6.png"))


screenW = 1100
screenH = 600

screenC = (10,10,10)

win = pygame.display.set_mode((screenW,screenH))

pygame.display.set_caption("unrelated")


font = pygame.font.SysFont("freesansbold.ttf", 30)



def redrawGameWindow():
    
    win.fill(screenC)
    
    mannen.draw()
    
    for i in projectiles:
        i.draw()
        
    #for i in hitboxes:
        #pygame.draw.rect(win,[255,0,0],(i.x,i.y,i.width,i.height),1)
        
    for i in items:
        i.draw()
    
    box.draw()
    win.blit(score,(int(box.x+box.width-score.get_width()), int(box.y+box.height+10)))
    
    if not game:
        if not game_over:
            win.blit(pygame.transform.scale(pause[(pause_timer%32)//16],(300,300)),(screenW//2-150,screenH//2-150))
        
    if game_over:
        if pause_timer > 100:
            win.blit(pygame.transform.scale(game_over_text[(pause_timer%32)//16],(300,300)),(screenW//2-150,screenH//2-150))
        
        
    
    pygame.display.update()

def harzardUpdate():
    global hazards
    global hazardsCooldown
    global hazardsCost  
    if len(hazards) < 3 + difficulty//10000:
        for i in possibilities:
            if hazardsCooldown <= 0:
                if dif_cost[possibilities.index(i)]*(1+len(hazards)*2) + hazardsCost+(1+len(hazards)*2) <= difficulty:
                    if randint(0,1) == 0:
                        hazardsCooldown = 150//(difficulty/500)
                        
                        hazardsCost += dif_cost[possibilities.index(i)]
                        
                        if i == "bullet":
                            td = randint(0,3) 
                            if td == 0:
                                tx = box.x + box.width
                                ty = randint(box.y+1,box.y+box.height-1)
                                td = 180
                            elif td == 1:
                                tx = randint(box.x+1,box.x+box.width-1)
                                ty = box.y + box.height
                                td = 270
                            elif td == 2:
                                tx = box.x
                                ty = randint(box.y+1,box.y+box.height-1)
                                td = 0
                            else:
                                tx = randint(box.x+1,box.x+box.width-1)
                                ty = box.y
                                td = 90 
                            
                            if tx - mannen.x - mannen.size//2 == 0:
                                if ty < mannen.y:
                                    td = 270
                                else: 
                                    td = 90
                            else:
                                td = degrees(atan((ty-mannen.y-mannen.size//2)/(tx-mannen.x-mannen.size//2)))
                                if tx > mannen.x:
                                    td += 180
                            
                            hazards.append(bullet(tx,ty,td,1,5))
                            
                        if i == "accelerationBullet":
                            td = randint(0,3)
                            if td == 0:
                                tx = box.x + box.width
                                ty = randint(box.y+1,box.y+box.height-1)
                                td = 180
                            elif td == 1:
                                tx = randint(box.x+1,box.x+box.width-1)
                                ty = box.y + box.height
                                td = 270
                            elif td == 2:
                                tx = box.x
                                ty = randint(box.y+1,box.y+box.height-1)
                                td = 0
                            else:
                                tx = randint(box.x+1,box.x+box.width-1)
                                ty = box.y
                                td = 90 
                            
                            if tx - mannen.x - mannen.size//2 == 0:
                                if ty < mannen.y:
                                    td = 270
                                else: 
                                    td = 90
                            else:
                                td = degrees(atan((ty-mannen.y-mannen.size//2)/(tx-mannen.x-mannen.size//2)))
                                if tx > mannen.x:
                                    td += 180
                            hazards.append(accelerationBullet(tx,ty,td,0.2,0.6,5))
                        
                        if i == "bigAccelerationBullet":
                            td = randint(0,3)
                            if td == 0:
                                tx = box.x + box.width
                                ty = randint(box.y+1,box.y+box.height-1)
                                td = 180
                            elif td == 1:
                                tx = randint(box.x+1,box.x+box.width-1)
                                ty = box.y + box.height
                                td = 270
                            elif td == 2:
                                tx = box.x
                                ty = randint(box.y+1,box.y+box.height-1)
                                td = 0
                            else:
                                tx = randint(box.x+1,box.x+box.width-1)
                                ty = box.y
                                td = 90 
                            
                            if tx - mannen.x - mannen.size//2 == 0:
                                if ty < mannen.y:
                                    td = 270
                                else: 
                                    td = 90
                            else:
                                td = degrees(atan((ty-mannen.y-mannen.size//2)/(tx-mannen.x-mannen.size//2)))
                                if tx > mannen.x:
                                    td += 180
                            
                            hazards.append(bigAccelerationBullet(tx,ty,td,0.1,0.6,10))
                        
                        if i == "bomb":
                            hazards.append(bomb(randint(box.x+50,box.x+box.width-200),randint(box.y+50,box.y+box.height-200),randint(0,1)))
                        
                        if i == "block":
                            hazards.append(block(randint(0,3),0,0,0,0,0))
                        if i == "wallSpawner":
                            n = randint(0,1)
                            if n == 0:
                                n = -1                          
                            hazards.append(wallSpawner(randint(0,3),0.5*n))
                            
                        if i == "danceMan":
                            hazards.append(danceMan(randint(0,3)))
                            
        hazardsCooldown -= 1
        
    for i in hazards:    
        if not i in projectiles:  
            hazards.remove(i)
            i = str(type(i).__name__)
            hazardsCost -= dif_cost[possibilities.index(i)]
    
def itemUpdate():
    global item
    global itemsCooldown
    if item == 0:
        if itemsCooldown <= 0:
            for i in item_posibilities:
                if randint(0,1) == 1:
                    
                    if i == "health":
                        if mannen.health < 5:
                            item = health(box.x+box.width//2+randint(-box.width//4,box.width//4),box.y+box.height//2+randint(-box.height//4,box.height//4))
                            itemsCooldown = 1000
                    else:
                        itemsCooldown = 500
            
            if item == 0:
                itemsCooldown = 100
                
        itemsCooldown -= 1
        
    if item not in items:
        item = 0
        
def red(x):
    return (-1.2**(-0.05*x) + 1) * 255

def blue(x):
    return (-1.1**(-0.01*x) + 1) * 255

def green(x):
    return (-1.03**(-0.01*x) + 1) * 255



def scoreUpdate():
    global scoreColour
    global score
    
    if difficulty <= 20000:
        scoreColour[0] = red(difficulty)
        scoreColour[2] = blue(difficulty)
        scoreColour[1] = green(difficulty)
    else:
        scoreColour = [255,255,255]
    
    score = font.render(str(difficulty//10), True, scoreColour)
        
def to_Goal(x,goal,side):
    if abs(x-goal) <= 1:
        x = goal
    else:
        if x > goal:
            x += change_Box(side,-1 - (x-goal)//50)
        else:
            x += change_Box(side,1 - (x-goal)//50)
    return x

def change_Box(side,change):    
    if side == 2:
        box.width -= change
    if side == 3:
        box.height -= change
    return change
    
                   

class screenBox():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.xGoal = x
        self.yGoal = y
        self.widthGoal = x + width
        self.heightGoal = y + height
        self.colour = (255,255,255)
    
    def size(self):
        
        if difficulty <= 200000:
            self.xGoal = screenW//2-150 - difficulty//100
            self.yGoal = screenH//2-150 - difficulty//300
            self.widthGoal = self.xGoal + 300 + (difficulty//100)*2
            self.heightGoal = self.yGoal + 300 + (difficulty//300)*2
        
        if difficulty%10 == 0:
            self.x = to_Goal(self.x,self.xGoal,2)
            self.y = to_Goal(self.y,self.yGoal,3)
            self.width = to_Goal(self.width+self.x,self.widthGoal,0) - self.x
            self.height = to_Goal(self.height+self.y,self.heightGoal,1) - self.y
        
        if self.x < 0:
            self.width += self.x
            self.x = 0
        if self.y < 0:
            self.height += self.y
            self.y = 0
        if self.width + self.x > screenW:
            self.width = screenW - self.x
        if self.height + self.y > screenH:
            self.height = screenH - self.y
            
    
    def draw(self):
        pygame.draw.rect(win,self.colour,(self.x//1,self.y//1,self.width//1,self.height//1),3)
        pygame.draw.rect(win,self.colour,(self.x-5,self.y-5,self.width+10,self.height+10),5)
        pygame.draw.rect(win,screenC,(self.x-50,self.y-50,self.width+100,self.height+100),86)
        

class player():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.health = 3
        self.size = self.health * 10 
        self.direction = 0
        self.vel = 2
        self.colour = [255,10,10]
        self.hit = False
        self.item = 0
        self.invicibility = 0
        self.inventory = []
        
        self.knust_state = randint(0,2)
        self.knust = broken()
        self.shards = []

        
    def getInput(self,rightPress,leftPress,upPress,downPress,actionPress):
        self.upPress = upPress
        self.downPress = downPress
        self.rightPress = rightPress
        self.leftPress = leftPress
        self.actionPress = actionPress
        
        self.tempVel = self.vel
        if (self.upPress or self.downPress) and (self.rightPress or self.leftPress):
            self.tempVel = self.vel//1.5
        
    def move(self):
        if self.rightPress:
            self.x += self.tempVel
        if self.leftPress:
            self.x -= self.tempVel
        if self.upPress:
            self.y -= self.tempVel
        if self.downPress:
            self.y += self.tempVel
            
        if self.x < box.x:
            if difficulty%2 == 0:
                box.x += change_Box(2,-1)
            self.x = box.x
        if self.x + self.size > box.x + box.width:
            if difficulty%2 == 0:
                box.width += change_Box(0,1)
            self.x = box.x + box.width - self.size
        if self.y < box.y:
            if difficulty%2 == 0:
                box.y += change_Box(3,-1)
            self.y = box.y
        if self.y + self.size > box.y + box.height:
            if difficulty%2 == 0:
                box.height += change_Box(1,1)
            self.y = box.y + box.height - self.size
    
    def collide(self):
        global screenC
        
        self.hit = False
        screenC = (0,0,0)
        if self.invicibility == 0:
            for i in hitboxes:
                if not self.hit:
                    if self.x < i.x + i.width and self.x + self.size > i.x:
                        if self.y < i.y + i.height and self.y + self.size > i.y:
                            self.hit = True
                            screenC = (72,0,0)
                            
                            self.invicibility = 20
                            hitboxes.remove(i)
                    
                            
        else:
            self.invicibility -= 1 
        
        global items
        for i in items:
            if self.x < i.x + i.width and self.x + self.size > i.x:
                if self.y < i.y + i.height and self.y + self.size > i.y:
                    i = str(type(i).__name__)
                    self.item = i
                    items = []
                        
    def healthCheck(self):
        if self.hit:
            self.health -= 1
            self.knust_state = randint(0,2)
            
            if self.health <= 0:
                global game_over
                global pause_timer
                global game
                game_over = True
                game = False
                pause_timer = 0 
                
                for i in range(difficulty//300):
                    if i > 100:
                        break
                    self.shards.append(shard(self.x,self.y,i//5+1,randint(0,360)))
        
        if self.item == "health":
            self.health += 1
            self.x -= 5
            self.y -= 5
            self.item = 0
                
            
        self.size = self.health * 10 
        
    def draw(self):
        
        if self.hit:
            if self.health > 0:
                self.knust.draw(self.x+self.size//2,self.y+self.size//2,self.knust_state)
            else:
                self.knust.draw(self.x+self.size//2,self.y+self.size//2,3)
                
        if game_over and pause_timer > 30:
            for i in self.shards:
                if i.x < box.x - 10 or i.y < box.y - 10 or i.x >  box.x+box.width + 10 or i.y > box.y+box.height + 10:
                    self.shards.remove(i)
                else:
                    i.move()
                    i.draw()
                
            
        else:       
            pygame.draw.rect(win,self.colour,(self.x,self.y,self.size,self.size))
#items
        
class health():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.timer = 0
        items.append(self)
    
    def action(self):
        self.timer += 1
        if self.timer >= 2000:
            items.remove(self)
        self.timer += 1
        
    def draw(self): 
        win.blit(pygame.transform.scale(cross[(difficulty%8)//4],(self.width,self.height)),(self.x,self.y))
    
class zipper():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.timer = 0
        items.append(self)
        
    def action(self):
        self.timer += 1
        if self.timer >= 2000:
            items.remove(self)
        self.timer += 1
    
    def draw(self): 
        win.blit(pygame.transform.scale(lightning[(difficulty%8)//4],(self.width,self.height)),(self.x,self.y))
        

#Enemies  
        
class bullet():
    def __init__(self,x,y,d,vel,size):
        self.x = x
        self.y = y
        self.d = d
        self.vel = vel
        self.xVel = ((cos(radians(self.d)))*self.vel)
        self.yVel = ((sin(radians(self.d)))*self.vel)
        self.size = size
        self.width = self.size
        self.height = self.size
        self.colour = (255,255,255)
        hitboxes.append(self)
        projectiles.append(self)
            
    def action(self):
        self.x += self.xVel
        self.y += self.yVel
        
        if not self in hitboxes:
            projectiles.remove(self)
            
    
    def draw(self):
        pygame.draw.circle(win,self.colour,(int(self.x)+self.size//2,int(self.y)+self.size//2),self.size)
    
class accelerationBullet():
    def __init__(self,x,y,d,a,vel,size):
        self.x = x
        self.y = y
        self.d = d
        self.vel = vel
        self.a = a
        self.xVel = ((cos(radians(self.d)))*self.vel)
        self.yVel = ((sin(radians(self.d)))*self.vel)
        self.size = size
        self.width = self.size
        self.height = self.size
        self.colour = (255,255,255)
        hitboxes.append(self)
        projectiles.append(self)
    
    def action(self):
        self.x += self.xVel/(10*self.a)
        self.y += self.yVel/(10*self.a)
        self.xVel = self.xVel*(self.a/10+1)
        self.yVel = self.yVel*(self.a/10+1)
        if not self in hitboxes:
            projectiles.remove(self)
        
    def draw(self):
        pygame.draw.circle(win,self.colour,(int(self.x)+self.size//2,int(self.y)+self.size//2),self.size,self.size//2)
    
class wallSpawner():
    def __init__(self,d,vel):
        self.d = d
            
        if self.d%2 == 0:
            self.width = 7
            self.height = 70
        else:
            self.width = 70
            self.height = 7
            
        if self.d == 0:
            self.x = box.x + box.width - self.width
            self.y = box.y + box.height//2 - self.height//2
        if self.d == 1:
            self.x = box.x + box.width//2 - self.width//2
            self.y = box.y + box.height - self.height
        if self.d == 2:
            self.x = box.x
            self.y = box.y + box.height//2 - self.height//2
        if self.d == 3:
            self.x = box.x + box.width//2 - self.width//2
            self.y = box.y
        
        self.bullets = []
        self.max_sd = 185 + 90*self.d
        self.min_sd = self.max_sd-10
        self.sd = randint(0,70)
        self.angleChange = 2
        self.timer = 0
        self.vel = vel
        self.colour = [255,255,255]
        
        projectiles.append(self)
        
    def shoot(self):
        self.max_sd += self.angleChange
        if self.max_sd%90 >= 20 and self.max_sd%90 <= 80:
            self.angleChange = self.angleChange*-1
            self.max_sd += self.angleChange
        self.min_sd = self.max_sd - 10
        
        if self.timer%4 == 0:
            if self.d%2 == 0:
                self.bullets.append(bullet(self.x+self.width//2,self.y+self.sd,self.max_sd-self.sd//self.height,2,5))
            else:
                self.bullets.append(bullet(self.x+self.sd,self.y+self.height//2,self.max_sd-self.sd//self.width,2,5))
            
        self.sd += 20
        if self.sd > 70:
            self.sd = self.sd - 67
        
    
        
    def action(self):
        if self.timer >= 100 and self.timer <= 1000:
            if self.d%2 == 0:
                self.y += self.vel
                if self.y < box.y or self.y + self.height > box.y + box.height:
                    self.vel = self.vel*-1
                    self.y += self.vel
            else:
                self.x += self.vel
                if self.x < box.x or self.x + self.width > box.x + box.width:
                    self.vel = self.vel*-1
                    self.y += self.vel
            
            if self.timer%5 == 0:
                self.shoot()
        
        elif self.timer >= 1100:
            projectiles.remove(self)
        self.timer += 1
        
    
    def draw(self):
        pygame.draw.rect(win,self.colour,(self.x,self.y,self.width,self.height))

     
class bigAccelerationBullet():
    def __init__(self,x,y,d,a,vel,size):
        self.x = x
        self.y = y
        self.d = d
        self.vel = vel
        self.a = a
        self.xVel = ((cos(radians(self.d)))*self.vel)
        self.yVel = ((sin(radians(self.d)))*self.vel)
        self.size = size
        self.width = self.size
        self.height = self.size
        self.colour = (255,255,255)
        self.bullets = []
        
        if self.d == 90 or self.d == 270:
            self.yDif = self.yVel * 100
            self.ly = self.y
        else:
            self.xDif = self.xVel * 100
            self.lx = self.x
        
        hitboxes.append(self)
        projectiles.append(self)
        
        
        
    def shoot(self):
        if self.d == 90:
            if self.y >= self.ly + self.yDif:
                self.bullets.append(accelerationBullet(self.x,self.y,self.d+90,0.1,0.6,5))
                self.bullets.append(accelerationBullet(self.x,self.y,self.d-90,0.1,0.6,5))
                self.ly = self.ly + self.yDif
        elif self.d == 270:
            if self.y <= self.ly + self.yDif:
                self.bullets.append(accelerationBullet(self.x,self.y,self.d+90,0.1,0.6,5))
                self.bullets.append(accelerationBullet(self.x,self.y,self.d-90,0.1,0.6,5))
                self.ly = self.ly + self.yDif         
        else:
            if self.d%360 > 90 and self.d%360 < 270:
                if self.x <= self.lx + self.xDif:
                    self.bullets.append(accelerationBullet(self.x,self.y,self.d+90,0.1,0.6,5))
                    self.bullets.append(accelerationBullet(self.x,self.y,self.d-90,0.1,0.6,5))
                    self.lx = self.lx +self.xDif         
            else:
                if self.x >= self.lx + self.xDif:
                    self.bullets.append(accelerationBullet(self.x,self.y,self.d+90,0.1,0.6,5))
                    self.bullets.append(accelerationBullet(self.x,self.y,self.d-90,0.1,0.6,5))
                    self.lx = self.lx +self.xDif
            
        
        
    def action(self):
        self.x += self.xVel/(10*self.a)
        self.y += self.yVel/(10*self.a)
        self.xVel = self.xVel*(self.a/10+1)
        self.yVel = self.yVel*(self.a/10+1)
        
        self.shoot()
        
        if not self in hitboxes:
            projectiles.remove(self)
        
        
    def draw(self):
        pygame.draw.circle(win,self.colour,(int(self.x)+self.size//2,int(self.y)+self.size//2),self.size,self.size//2)
    

class explotion():
    def __init__(self,x,y,width,height,d):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.d = d
        
        hitboxes.append(self)
        projectiles.append(self)
        
    def action(self):
        if self.d == 0:
            self.y += 2
            self.x = box.x
            self.height -= 4
            self.width = box.width
        if self.d == 1:
            self.x += 2
            self.y = box.y
            self.width -= 4
            self.height = box.height        
        
        if self.width <= 0 or self.height <= 0:
            projectiles.remove(self)
            
            if self in hitboxes:
                hitboxes.remove(self)
        
    def draw(self):
        pygame.draw.rect(win,(255,255,255),(int(self.x),int(self.y),int(self.width),int(self.height)))


class bomb():
    def __init__(self,x,y,d):
        self.x = x
        self.y = y
        self.width = 120
        self.height = 120
        self.d = d
        self.timer = 0
        self.explode = 300 - difficulty//100
        if self.explode <= 75:
            self.explode = 75
        
        self.drawState = 0
        
        projectiles.append(self)
        
    
    def action(self):
        self.timer += 1
        if self.timer == self.explode:
            if self.d == 0:
                self.explotion = explotion(self.x,self.y+self.height//4,self.width,self.height//2,0)
            if self.d == 1:
                self.explotion = explotion(self.x+self.width//4,self.y,self.width//2,self.height,1)
        if self.timer >= self.explode+6:
            projectiles.remove(self)
        
    def draw(self):
        if self.timer >= self.explode/3:
            self.drawState = 1
        if self.timer >= (self.explode/3)*2:
            self.drawState = 2
        if self.timer >= (self.explode/6)*5:
            self.drawState = 3
        if self.timer >= self.explode:
            self.drawState = 4
        
        if self.d == 0:
            if self.drawState == 0:
                self.image = pygame.transform.scale(bomb_h[int((self.timer)//5)%4], (self.width, self.height))
            elif self.drawState == 1:
                self.image = pygame.transform.scale(bomb_h[int((self.timer)//5)%4+4], (self.width, self.height))
            elif self.drawState == 2:
                self.image = pygame.transform.scale(bomb_h[int((self.timer)//5)%2+8], (self.width, self.height))
            elif self.drawState == 3:
                self.image = pygame.transform.scale(bomb_h[10], (self.width, self.height))
            elif self.drawState == 4:
                self.image = pygame.transform.scale(bomb_h[((self.timer-self.explode)//2)+11], (self.width, self.height))
        
        if self.d == 1:
            if self.drawState == 0:
                self.image = pygame.transform.scale(bomb_v[int((self.timer)//5)%4], (self.width, self.height))
            elif self.drawState == 1:
                self.image = pygame.transform.scale(bomb_v[int((self.timer)//5)%4+4], (self.width, self.height))
            elif self.drawState == 2:
                self.image = pygame.transform.scale(bomb_v[int((self.timer)//5)%2+8], (self.width, self.height))
            elif self.drawState == 3:
                self.image = pygame.transform.scale(bomb_v[10], (self.width, self.height))
            elif self.drawState == 4:
                self.image = pygame.transform.scale(bomb_v[((self.timer-self.explode)//2)+11], (self.width, self.height))
        
        if self.timer >= 20:
            win.blit(self.image,(self.x//1,self.y//1))
            
        else:
            win.blit(self.image,(self.x//1,self.y//1))
            
        
class danceMan():
    def __init__(self,d):
        self.d = d   
        self.width = 100
        self.height = 100
        
        if self.d == 0:
            self.x = box.x + box.width - self.width - 5
            self.y = box.y + box.height//2 - self.height//2
            self.vel = -0.5
        if self.d == 1:
            self.x = box.x + box.width//2 - self.width//2
            self.y = box.y + box.height - self.height - 5
            self.vel = 0.5
        if self.d == 2:
            self.x = box.x + 5
            self.y = box.y + box.height//2 - self.height//2
            self.vel = 0.5
        if self.d == 3:
            self.x = box.x + box.width//2 - self.width//2
            self.y = box.y + 5
            self.vel = -0.5

        self.timer = 0
        self.sd = 0
        self.bullets = []
        self.drawCount = 0
        
        projectiles.append(self)
        
    def shoot(self):
        if self.timer < 1000:
            if self.timer%6 == 0:
                self.bullets.append(bullet(self.x+self.width//2,self.y+self.height//3,self.sd,1,5))
            self.sd += 37
        if self.timer >= 1175:
            if self.timer%5 == 0:
                for i in range(10):
                    self.bullets.append(bullet(self.x+self.width//2,self.y+self.height//3,36*i,(1205-self.timer)/15,5))
        
    def action(self):
        if self.timer > 100 and self.timer < 1200:    
            if self.d%2 == 0:
                self.y += self.vel
                if self.y <= box.y + 5:
                    self.vel = abs(self.vel)*-1
                    self.d = 1
                elif self.y + self.height >= box.y + box.height - 5:
                    self.vel = abs(self.vel)
                    self.d = 3
            else:
                self.x += self.vel
                if self.x <= box.x + 5:
                    self.vel = abs(self.vel)
                    self.d = 2
                elif self.x + self.width >= box.x + box.width - 5:
                    self.vel = abs(self.vel)*-1
                    self.d = 0  
                
            self.shoot()
        if self.timer >= 1200:
            projectiles.remove(self)
        self.timer += 1
        
        self.drawCount += 1
        if self.drawCount > 55:
            self.drawCount = 0

    
    def draw(self):
        if self.timer >= 10:
            win.blit(pygame.transform.scale(dance[self.drawCount//3], (self.width, self.height)),(self.x//1,self.y//1))
        else:
            win.blit(pygame.transform.scale(dance[self.drawCount//3], ((self.width*self.timer//10), self.height*self.timer//10)),(self.x//1,self.y//1))


class block():
    def __init__(self,d,x,y,width,height,force):
        self.d = d
        
        if width == 0 and height == 0:
            self.size = difficulty//200 + 70
            if self.size > 200:
                self.size = 200
            
            self.width = randint(25,self.size-25)
            self.height = self.size - self.width
        else:
            self.width = width
            self.height = height
        
        if x == 0 and y == 0:
            if self.d%2 == 0:
                self.y = randint(box.y+5,box.y+box.height-self.height-5)
                if d == 0:
                    self.x = box.x+box.width-1
                else:
                    self.x = box.x-self.width+1
            else:
                self.x = randint(box.x+5,box.x+box.width-self.width-5)
                if d == 1:
                    self.y = box.y+box.height-1
                else:
                    self.y = box.y-self.height+1
        else:
            self.x = x
            self.y = y
        
        if force == 0:
            if d%2 == 0:
                self.f = self.height//5
                self.f_len = self.height//self.f
            else:
                self.f = self.width//5
                self.f_len = self.width//self.f
        else:
            self.f = force
            
        self.vel = 0
        self.a = 0.02
        if self.size >= 200:
            self.a = 0.01
        self.timer = 0
        self.state = "spawn"
        
        projectiles.append(self)
        
    
    def action(self):
        if self.state == "spawn":
            if self.timer == 30:
                self.state = "move"
                self.vel = 0.1
                hitboxes.append(self)
            self.timer += 1
        
        else:
            
            if self.state == "move" or self.state == "change":
                if self.d == 0:
                    self.x -= self.vel
                    if self.x <= box.x:
                        self.state = "land"
                        self.f_pos = self.x - self.f_len
                if self.d == 1:
                    self.y -= self.vel
                    if self.y <= box.y:
                        self.state = "land"
                        self.f_pos = self.y - self.f_len
                if self.d == 2:
                    self.x += self.vel
                    if self.x + self.width >= box.x + box.width:
                        self.state = "land"
                        self.f_pos = self.x + self.f_len
                        
                if self.d == 3:
                    self.y += self.vel
                    if self.y + self.height >= box.y + box.height:
                        self.state = "land"
                        self.f_pos = self.y + self.f_len
                
                self.vel = self.vel *(self.a+1)
                
                if self.state == "move":
                    if self.d%2 == 0:
                        if abs((self.x + self.width//2)-(mannen.x+mannen.size//2)) < 20:
                            if mannen.y <= self.y:
                                self.d = 1
                                self.vel = 0.1
                            else:
                                self.d = 3
                                self.vel = 0.1
                            self.state = "change"
                    else:
                        if abs((self.y + self.height//2)-(mannen.y+mannen.size//2)) < 20:
                            if mannen.x <= self.x:
                                self.d = 0
                                self.vel = 0.1
                            else:
                                self.d = 2
                                self.vel = 0.1
                            self.state = "change"
            
            
            
            if self.state == "land":
                if self.d == 0:
                    self.x -= self.vel
                    if self.x <= self.f_pos - self.f_len:
                        self.f_pos -= self.f_len
                        self.x = self.f_pos
                        self.vel = 1
                        box.x += change_Box(2,-3)
                
                if self.d == 1:
                    self.y -= self.vel
                    if self.y <= self.f_pos - self.f_len:
                        self.f_pos -= self.f_len
                        self.y = self.f_pos
                        self.vel = 1
                        box.y += change_Box(3,-3)
                        
                if self.d == 2:
                    self.x += self.vel
                    if self.x >= self.f_pos + self.f_len:
                        self.f_pos += self.f_len
                        self.x = self.f_pos
                        self.vel = 1
                        box.width += change_Box(0,3)
                        
                if self.d == 3:
                    self.y += self.vel
                    if self.y >= self.f_pos + self.f_len:
                        self.f_pos += self.f_len
                        self.y = self.f_pos
                        self.vel = 1
                        box.height += change_Box(1,3)
            
            if self not in hitboxes:
                projectiles.remove(self)
            
    def draw(self):
        if self.state == "land":
            pygame.draw.rect(win,[255,255,255],(int(self.x) + randint(-3,3),int(self.y) + randint(-3,3),self.width,self.height),5)      
        else:
            pygame.draw.rect(win,[255,255,255],(int(self.x),int(self.y),self.width,self.height),5)

#Effects

class broken():
    def __init__(self):
        self.width = 250
        self.height = 250
        
        self.colour = [0,0,0]
    
    def draw(self,x,y,state):
        self.state = state
        if self.state == 3:
            self.width = self.width*2
            self.height = self.height*2
        
        self.x = x - self.width//2
        self.y = y - self.height//2
        
        pygame.draw.rect(win,self.colour,(self.x+1,self.y+1,self.width-2,self.height-2))
        win.blit(pygame.transform.scale(knust[state], (self.width,self.height)),(self.x,self.y))       

class shard():
    def __init__(self,x,y,vel,d):
        self.x = x
        self.y = y
        self.d = d
        self.vel = vel
        self.xVel = ((cos(radians(self.d)))*self.vel)
        self.yVel = ((sin(radians(self.d)))*self.vel)
        self.width = randint(3,6)
        self.height = randint(3,6)
        self.wait = randint(10,50)
    
    def move(self):
        self.x += self.xVel
        self.y += self.yVel
        
        if pause_timer % self.wait == 0:
            temp = self.height
            self.height = self.width
            self.width = temp
    
    def draw(self):
        pygame.draw.rect(win,mannen.colour,(int(self.x),int(self.y),self.width,self.height))
        
    

            
            
        
possibilities = ["danceMan","wallSpawner","block","bomb","bigAccelerationBullet","accelerationBullet","bullet"]
dif_cost = [2500,1500,1000,700,500,200,100]
hazards = []
hazardsCooldown = 200
hazardsCost = 0

item_posibilities = ["health"]
item = 0
items = []
itemsCooldown = 1000


hitboxes = []
projectiles = []


scoreColour = [0,0,0]

box = screenBox(screenW//2-150,screenH//2-150,300,300)
mannen = player(500,250)

difficulty = 0

pause_timer = 0

run = True
game = True
game_over = False
restart = False
while run:
    pygame.time.delay(10)
    
    keys = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_ESCAPE]:
        if pause_timer > 40:
            if game == False:
                game = True
                pause_timer = 0
            else:
                game = False
                pause_timer = 0         
            
        
    
    if mannen.hit:
        pygame.time.delay(300)
        mannen.hit = False
    
    if keys[pygame.K_r] or restart:
        mannen = player(500,250)
        hazards = []
        hazardsCooldown = 200
        hazardsCost = 0
        item = 0
        items = []
        itemsCooldown = 1000
        hitboxes = []
        projectiles = []
        difficulty = 0
        if keys[pygame.K_g]:
            difficulty = 100000
        box = screenBox(screenW//2-157,screenH//2-157,300,300)
        restart = False
        game_over = False
        game = True
        
  
    if game or game_over:
        
        if not game_over or pause_timer > 30:
            
            for i in projectiles:
                i.action()
                if i.x+i.width < box.x or i.x > box.x + box.width or i.y + i.height < box.y or i.y > box.y + box.height:
                    if i in projectiles:
                        projectiles.remove(i)
                    if i in hitboxes:
                        hitboxes.remove(i)
                        
            mannen.getInput(keys[pygame.K_RIGHT],keys[pygame.K_LEFT],keys[pygame.K_UP],keys[pygame.K_DOWN],keys[pygame.K_SPACE])
            mannen.move()
            
            for i in items:
                i.action()
        
            
            box.size()  
            scoreUpdate()
            
            if game:
                harzardUpdate()
                itemUpdate()
                        
                difficulty += 1
                
                mannen.collide()
                mannen.healthCheck()
    

    pause_timer += 1
    
    redrawGameWindow()
    
pygame.quit()
