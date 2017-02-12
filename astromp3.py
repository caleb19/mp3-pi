#!/usr/bin/python
import time
import os
import pygame.mixer
import glob
from sense_hat import SenseHat
import numpy
import random
r = [255,0,0]
o = [255,127,0]
y = [255,255,0]
g = [0,255,0]
b = [0,0,255]
i = [75,0,130]
v = [159,0,255]
w = [255,255,255]
e = [0,0,0]
l = [128,255,128]
a = [0,180,180]

wave = [r,o,y,g,b,i,v,w,
        w,r,o,y,g,b,i,v,
        v,w,r,o,y,g,b,i,
        i,v,w,r,o,y,g,b,
        b,i,v,w,r,o,y,g,
        g,b,i,v,w,r,o,y,
        y,g,b,i,v,w,r,o,
        o,y,g,b,i,v,w,r]

rain = [g,e,e,g,e,e,l,e,
        g,e,e,g,e,g,l,e,
        l,e,g,l,e,g,w,g,
        l,e,g,l,e,l,e,g,
        w,e,l,w,e,l,e,l,
        e,e,l,e,e,w,e,l,
        e,e,w,e,e,e,g,l,
        e,e,e,e,e,e,g,w]

rainbow = [e,e,e,r,r,e,e,e,
           e,r,r,o,o,r,r,e,
           r,o,o,y,y,o,o,r,
           o,y,y,g,g,y,y,o,
           y,g,g,b,b,g,g,y,
           b,b,b,i,i,b,b,b,
           b,i,i,v,v,i,i,b,
           i,v,v,e,e,v,v,i]

square_1 = [a,a,a,a,a,a,a,a,
            a,e,e,e,e,e,e,a,
            a,e,e,e,e,e,e,a,
            a,e,e,e,e,e,e,a,
            a,e,e,e,e,e,e,a,
            a,e,e,e,e,e,e,a,
            a,e,e,e,e,e,e,a,
            a,a,a,a,a,a,a,a]

square_2 = [e,e,e,e,e,e,e,e,
            e,a,a,a,a,a,a,e,
            e,a,e,e,e,e,a,e,
            e,a,e,e,e,e,a,e,
            e,a,e,e,e,e,a,e,
            e,a,e,e,e,e,a,e,
            e,a,a,a,a,a,a,e,
            e,e,e,e,e,e,e,e]

square_3 = [e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,a,a,a,a,e,e,
            e,e,a,e,e,a,e,e,
            e,e,a,e,e,a,e,e,
            e,e,a,a,a,a,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e]

square_4 = [e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,a,a,e,e,e,
            e,e,e,a,a,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e,
            e,e,e,e,e,e,e,e]

squares = [square_1, square_2, square_3, square_4, square_3, square_2, square_1]

image = rainbow
current_pic = 0

pause_image = [e, e, e, e, e, e, e, e,
               e, w, w, e, e, w, w, e,
               e, w, w, e, e, w, w, e,
               e, w, w, e, e, w, w, e,
               e, w, w, e, e, w, w, e,
               e, w, w, e, e, w, w, e,
               e, w, w, e, e, w, w, e,
               e, e, e, e, e, e, e, e]

play_image = [e,e,e,e,e,e,e,e,
              e,w,e,e,e,e,e,e,
              e,w,w,e,e,e,e,e,
              e,w,w,w,e,e,e,e,
              e,w,w,w,w,e,e,e,
              e,w,w,w,e,e,e,e,
              e,w,w,e,e,e,e,e,
              e,w,e,e,e,e,e,e]

next_image = [e,e,e,e,e,e,e,e,
              e,w,e,e,e,w,w,e,
              e,w,w,e,e,w,w,e,
              e,w,w,w,e,w,w,e,
              e,w,w,w,w,w,w,e,
              e,w,w,w,e,w,w,e,
              e,w,w,e,e,w,w,e,
              e,w,e,e,e,w,w,e]

plus = [e,e,e,w,w,e,e,e,
        e,e,e,w,w,e,e,e,
        e,e,e,w,w,e,e,e,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        e,e,e,w,w,e,e,e,
        e,e,e,w,w,e,e,e,
        e,e,e,w,w,e,e,e]

minus = [e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         w,w,w,w,w,w,w,w,
         w,w,w,w,w,w,w,w,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e,
         e,e,e,e,e,e,e,e]

forwards = [e,e,e,e,e,e,e,e,
            w,e,e,e,w,e,e,e,
            w,w,e,e,w,w,e,e,
            w,w,w,e,w,w,w,e,
            w,w,w,w,w,w,w,w,
            w,w,w,e,w,w,w,e,
            w,w,e,e,w,w,e,e,
            w,e,e,e,w,e,e,e]

shuffle = [e,e,e,e,e,e,e,e,
           e,e,w,w,w,w,e,e,
           e,e,w,e,e,e,e,e,
           e,e,w,e,e,e,e,e,
           e,e,w,w,w,w,e,e,
           e,e,e,e,e,w,e,e,
           e,e,e,e,e,w,e,e,
           e,e,w,w,w,w,e,e]

no_shuffle = [r,e,e,e,e,e,e,r,
              e,r,w,w,w,w,r,e,
              e,e,r,e,e,r,e,e,
              e,e,w,r,r,e,e,e,
              e,e,w,r,r,w,e,e,
              e,e,r,e,e,r,e,e,
              e,r,e,e,e,w,r,e,
              r,e,w,w,w,w,e,r]

sense = SenseHat()

angles = [0, 90, 180, 270]
r = 0

s = False 

# Set audio output to Analogue Jack
os.system("sudo amixer cset numid=3 1")
# Set system volume to 100% then control using pygame
os.system("sudo amixer cset numid=1 100%")

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640,480))

volume = 0.2

# Get a list of all the music files
path_to_music = "/home/pi/Music"
os.chdir(path_to_music)
music_files = glob.glob("*.mp3")
music_files.sort()

current_track = 0
n_tracks = len(music_files)
paused = False
start_time = 0.0
sense.show_message("Hi Tim! Let's play some tunes!")

while True:
    pygame.mixer.music.load(music_files[current_track])
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    start_time = 0.0
    sense.set_pixels(image)
    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_u:
                    if paused == False:
                        pygame.mixer.music.pause()
                        sense.set_rotation(0)
                        sense.set_pixels(pause_image)
                    else:
                        pygame.mixer.music.unpause()
                        sense.set_rotation(0)
                        sense.set_pixels(play_image)
                        time.sleep(2)
                        sense.set_pixels(image)
                    paused = not paused
                if event.key == pygame.K_r:
                    current_track = current_track + 1
                    if current_track >= n_tracks:
                        current_track = 0
                    sense.set_rotation(0)
                    sense.set_pixels(next_image)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(music_files[current_track])
                    pygame.mixer.music.play()
                    if paused == True:
                        pygame.mixer.music.pause()
                    start_time = 0.0
                    time.sleep(1.5)
                    if paused == True:
                        sense.set_pixels(pause_image)
                    else:
                        sense.set_pixels(image)
                if event.key == pygame.K_l:
                    current_track = current_track - 1
                    if current_track < 0:
                        current_track = n_tracks - 1
                    sense.set_rotation(180)
                    sense.set_pixels(next_image)
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(music_files[current_track])
                    pygame.mixer.music.play()
                    if paused == True:
                        pygame.mixer.music.pause()
                    start_time = 0.0
                    time.sleep(1.5)
                    sense.set_rotation(0)
                    if paused == True:
                        sense.set_pixels(pause_image)
                    else:
                        sense.set_pixels(image)
                if event.key == pygame.K_RETURN:
                    if s == False:
                        s = True
                        pygame.mixer.music.stop()
                        current_track = random.randint(0, n_tracks - 1)
                        pygame.mixer.music.load(music_files[current_track])
                        pygame.mixer.music.play()
                        if paused == True:
                            pygame.mixer.music.pause()
                        sense.set_rotation(0)
                        sense.set_pixels(shuffle)
                        time.sleep(1.5)
                        sense.set_pixels(image)
                    else:
                        s = False
                        sense.set_rotation(0)
                        sense.set_pixels(no_shuffle)
                        time.sleep(1.5)
                        sense.set_pixels(image)
                if event.key == pygame.K_UP:
                    current_time = pygame.mixer.music.get_pos()/1000.0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play(start=start_time+current_time-15.0)
                    if paused == True:
                        pygame.mixer.music.pause()
                    start_time = start_time+current_time-15.0
                    if start_time < 0.0:
                        start_time = 0.0
                    sense.set_rotation(180)
                    sense.set_pixels(forwards)
                    time.sleep(2)
                    sense.set_rotation(0)
                    sense.set_pixels(image)
                if event.key == pygame.K_DOWN:
                    current_time = pygame.mixer.music.get_pos()/1000.0
                    pygame.mixer.music.stop()
                    pygame.mixer.music.play(start=start_time+current_time+15.0)
                    if paused == True:
                        pygame.mixer.music.pause()
                    start_time = start_time+current_time+15.0
                    sense.set_rotation(0)
                    sense.set_pixels(forwards)
                    time.sleep(2)
                    sense.set_pixels(image)
                if event.key == pygame.K_d:
                    sense.set_rotation(0)
                    sense.show_message(os.path.splitext(music_files[current_track])[0], back_colour=[0,0,0], text_colour=[255,0,0])
                    sense.set_pixels(image)
                if event.key == pygame.K_b:
                    volume = volume + 0.05
                    sense.set_pixels(plus)
                    time.sleep(1)
                    sense.set_pixels(image)
                    if volume >= 1.0:
                        volume = 1.0
                        sense.set_rotation(0)
                        sense.show_message("MAX")
                    pygame.mixer.music.set_volume(volume)
                if event.key == pygame.K_a:
                    sense.set_rotation(0)
                    volume = volume - 0.05
                    sense.set_pixels(minus)
                    time.sleep(1)
                    sense.set_pixels(image)
                    if volume <= 0.0:
                        volume = 0.0
                        sense.set_rotation(0)
                        sense.show_message("MIN")
                    pygame.mixer.music.set_volume(volume)
                if event.key == pygame.K_RIGHT:
                    current_pic = current_pic + 1
                    if current_pic > 3:
                        current_pic = 0
                if event.key == pygame.K_LEFT:
                    current_pic = current_pic - 1
                    if current_pic < 0:
                        current_pic = 3
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    if current_pic == 0:
                        image = rainbow
                    if current_pic == 1:
                        image = wave
                    if current_pic == 2:
                        image = rain
                    if current_pic == 3:
                        image = squares[0]
                    sense.set_pixels(image)
        if paused == False:
            if current_pic==0:
                sense.set_rotation(angles[r])
                r = r + 1
                if r >= 4:
                    r = 0
            else:
                sense.set_rotation(0)
            if current_pic==1:
                image = numpy.roll(image, 8, axis=0)
            if current_pic==2:
                image = numpy.roll(image, 8, axis=0)
            if current_pic==3:
                squares = numpy.roll(squares, 1, axis=0)
                image = squares[0]
            sense.set_pixels(image)
            time.sleep(0.2)
        else:
            sense.set_rotation(0)
            sense.set_pixels(pause_image)
    sense.set_rotation(0)    
    sense.show_message("Track ended")
    if s == False:
        current_track = current_track + 1
        if current_track >= n_tracks:
            current_track = 0
    else:
        current_track = random.randint(0, n_tracks - 1)

        
