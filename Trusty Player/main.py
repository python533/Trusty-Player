import tkinter as tk
import fnmatch
import os

import pygame.display
from pygame import mixer

canvas =tk.Tk()
canvas.title("Trusty Player")
canvas.geometry("400x250")

#Müzik Dizini
rootpath=''

#Mp3 Deseni
desen="* .mp3"

#Liste Görünümü
listBox=tk.Listbox(canvas,fg="cyan",bg="black",width=100,font=('ds-digital',14))
listBox.pack(padx=15,pady=15)


#Dizindeki Şarkıları Getirme
for root,dirs,files in os.walk(rootpath):
    for filename in fnmatch.filter(files,desen):
        listBox.index('end',filename)


#Şarkı Seçimleri İçin Kullanılan Kısmın Tasarımı
Label=tk.Label(canvas,text='',bg='black',fg='yellow',font=('ds-digitale',18))
Label.pack(pady=15)


top=tk.Frame(canvas,bg='black')
top.pack(padx=10,pady=5,anchor='center')


prevButton = tk.Button(canvas, text = "Prev")
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(canvas, text = "Stop")
prevButton.pack(pady = 15, in_ = top, side = 'left')




prevButton = tk.Button(canvas, text = "Prev", image = '', bg = 'black', borderwidth = 0 )
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(canvas, text = "Stop", image = '', bg = 'black', borderwidth = 0 )
stopButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(canvas, text = "Play", image = '', bg = 'black', borderwidth = 0 )
playButton.pack(pady = 15, in_ = top, side = 'left')

pauseButton = tk.Button(canvas, text = "Pause", image = '', bg = 'black', borderwidth = 0 )
pauseButton.pack(pady = 15, in_ = top, side = 'left')

nextButton = tk.Button(canvas, text = "Next", image = '', bg = 'black', borderwidth = 0)
nextButton.pack(pady = 15, in_ = top, side = 'left')


#Fonksiyonlar Kısmı
def select():
    Label.config()
    mixer.music.load()
    mixer.music.play()
    mixer.init()

playButton=tk.Button(canvas,text='Play',image='',bg='black',borderwidth=0)
nextButton.pack(pady = 15, in_ = top, side = 'left')


def stop():
    mixer.music.stop()
    listBox.select_clear('active')

    stopButton.pack(pady=15, in_=top, side='left')



def play_next(listen=None):
    next_song=listBox.curselection()
    next_song=next_song[0]+1
    next_song_name=listBox.get(next_song)
    Label.config(text=next_song_name)

    mixer.music.load(rootpath+"\\"+next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listen.select_set(next_song)



nextButton = tk.Button(canvas, text = "Next", image = '', bg = 'black', borderwidth = 0)
nextButton.pack(pady = 15, in_ = top, side = 'left')



def prev_song(listen=None):
    prev_song=listBox.curselection()
    prev_song=prev_song[0]-1
    prev_song_name = listBox.get(prev_song)
    Label.config(text=prev_song_name)

    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(prev_song)
    listen.select_set(prev_song)

    mixer.music.load(rootpath + " \\ " + prev_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(prev_song)
    listen.select_set(prev_song)

    prevButton = tk.Buttons(canvas, text="Prev", image='', bg='black', borderwidth=0, command=play_next())
    prevButton.pack(pady=15, in_=top, side='left')


def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"

    else:
     mixer.music.unpause()
     pauseButton["text"] = "Pause"


tk.mainloop()