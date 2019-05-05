from tkinter import *
from pygame import mixer # Load the required library
#pip3 install pygame


mixer.init()

root = Tk() # create tkinter window

filename = 'cancion.mp3'
mixer.music.load(filename)

def play():
	mixer.music.play()
def stop():
	mixer.music.stop()
def pause():
	mixer.music.pause()
def unpause():	
	mixer.music.unpause()

playB = Button(root, text = 'Play', command = play)
stopB = Button(root, text = 'Stop', command = stop)
pauseB = Button(root, text = 'Pause', command = pause)
unpauseB = Button(root, text = 'Unpause', command = unpause)

playB.pack()
stopB.pack()
pauseB.pack()
unpauseB.pack()

root.mainloop()