import pyautogui as pygui
import time, random
import pygame.mixer_music as mu
import pygame.mixer as mi
import pygame,os

path="G:\Songs"  # Give folder path of songs
songs=[]
for track in os.listdir(path=path):
    a="G:\\Songs\\"+track
    songs.append(a)

def music_player(): #function defination
    mi.init()
    mu.set_volume(0.7)
    mu.load(random.choice(songs))
    print("*******************************************************************")
    print("\t\tWELCOME TO MY MUSIC_PLAYER")
    print("*******************************************************************")
    print("press 'a' to PLAY | press 'r' to RESUME | press 'n' for next song")
    print("press 's' to STOP | press 'p' to PAUSE")
    print("--------------------------------------------------------------------\n")
    while True:
        query=input("")
        if query=='a':
            mu.play()
            print("Player Start!")
        elif query=='r':
            mu.unpause()
            print("Song resume")
        elif query=='p':
            print("song pause!")
            mu.pause()
        elif query=='n':
            print("Listen next song!")
            mu.stop()
            time.sleep(1)
            mu.load(random.choice(songs))
            mu.play()
        elif query=='s':
            mu.stop()
            break
    print("Player get quit !")
mi.quit()

music_player() #function calling

