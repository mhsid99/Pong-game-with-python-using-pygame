# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 23:47:57 2020

@author: Hamza
"""

import pygame as pg
import sys
import random
import winsound as ws

bspeed_x=7*random.choice((1,-1))
bspeed_y=7*random.choice((1,-1))
pspeed=0
ospeed=7
pscore=0
oscore=0    
screen_width=934
screen_height=700
t=False

pg.init()
clock=pg.time.Clock()
screen=pg.display.set_mode((screen_width,screen_height))
pg.display.set_caption('PonG')

ball=pg.Rect(screen_width/2-15,screen_height/2-15,30,30)
player=pg.Rect(screen_width-20,screen_height/2-70,10,140)
opponent=pg.Rect(10,screen_height/2-70,10,140)

def ball_movement():
    global bspeed_x,bspeed_y,pscore,oscore
    ball.x+=bspeed_x
    ball.y+=bspeed_y
    if ball.top<=0 or ball.bottom>=screen_height:
        bspeed_y*=-1
        ws.PlaySound(r"D:\Projects\Project Resources\bounce.wav",ws.SND_ASYNC)
    if ball.left<=0:
        pscore+=1
        ball_restart()
        ws.PlaySound(r"D:\Projects\Project Resources\button-3.wav",False)
    if ball.right>=screen_width:
        oscore+=1
        ball_restart()
        ws.PlaySound(r"D:\Projects\Project Resources\fail-buzzer-01.wav",False)
    if ball.colliderect(player) or ball.colliderect(opponent):
        bspeed_x*=-1
        ws.PlaySound(r"D:\Projects\Project Resources\bounce.wav",ws.SND_ASYNC)

def drawings():
    screen.fill(pg.Color('grey12'))
    pg.draw.rect(screen,(200,200,200),player)
    pg.draw.rect(screen,(200,200,200),opponent)
    pg.draw.ellipse(screen,(0,255,0),ball)
    pg.draw.aaline(screen,(200,200,200),(screen_width/2,0),(screen_width/2,screen_height))
    ptext=pg.font.Font("freesansbold.ttf",32).render(f"{pscore}",False,(200,200,200))
    screen.blit(ptext,(660,470))
    otext=pg.font.Font("freesansbold.ttf",32).render(f"{oscore}",False,(200,200,200))
    screen.blit(otext,(360,470))

def player_movement():
    player.y+=pspeed
    if player.top<=0:
        player.top=0
    if player.bottom>=screen_height:
        player.bottom=screen_height
        
def events_manager():
     global pspeed
     for event in pg.event.get():
        if event.type==pg.QUIT or event.type==pg.K_ESCAPE:
            pg.quit()
            sys.exit()
        if event.type==pg.KEYDOWN:
            if event.key==pg.K_UP:
                pspeed-=7
            if event.key==pg.K_DOWN:
                pspeed+=7
        if event.type==pg.KEYUP:
            if event.key==pg.K_UP:
                pspeed+=7
            if event.key==pg.K_DOWN:
                pspeed-=7

def opponent_movement():
    if opponent.top<ball.y:
        opponent.y+=ospeed
    if opponent.bottom>ball.y:
        opponent.y-=ospeed
    if opponent.top<=0:
        opponent.top=0
    if opponent.bottom>=screen_height:
        opponent.bottom=screen_height
    
def ball_restart():
    global bspeed_x,bspeed_y,t
    ball.center=(screen_width/2,screen_height/2)
    bspeed_y *=random.choice((1,-1))
    bspeed_x *=random.choice((1,-1))
    
    


while True:

    events_manager()
    drawings()        
    ball_movement()
    player_movement()
    opponent_movement()
    pg.display.flip()
    clock.tick(60)
    
