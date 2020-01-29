from __future__ import unicode_literals
import youtube_dl
import tkinter as tk
from tkinter import filedialog, Text
import os

y = 25
linklist = []
mp3_opt = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'nocheckcertificate': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}
mp4_opt = {'format': 'bestvideo+bestaudio/best',
           'outtmpl': '%(title)s.mp4'}


def download(opt):

    with youtube_dl.YoutubeDL(opt) as dl:
        for song_url in linklist:
            dl.download([song_url])
            os.chdir(dirname)
    label2 = tk.Label(root, text="Download Complete")
    label2.pack()


def selectdir1():
    global dirname
    dirname = filedialog.askdirectory(
        initialdir="/home/sud0nim", title="Select Download Folder")
    os.chdir(dirname)
    download(mp3_opt)


def selectdir2():
    global dirname
    dirname = filedialog.askdirectory(
        initialdir="/home/sud0nim", title="Select Download Folder")
    os.chdir(dirname)
    download(mp4_opt)


def savelink():
    global y
    global linklist
    if links.get() != "":
        linklist.append(links.get())
        canvas.create_text(250, y, text=links.get())
        y += 15
        links.delete(0, 100)


root = tk.Tk()
root.resizable(False, False)
root.title('YouTube DL')
canvas = tk.Canvas(root, height=300, width=500, bg='#99ccff')
canvas.pack()
canvas.create_text(250, 10, text="Videos to download")
label1 = tk.Label(root, text="YouTube Link: ")
label1.pack()
links = tk.Entry(root, width=50)
links.pack()
save = tk.Button(root, text="Save",
                 fg="black", bg="white", command=savelink)
save.pack()
done = tk.Button(root, text="Download MP3",
                 fg="black", bg="white", command=selectdir1)
done.pack()
mp4 = tk.Button(root, text="Download MP4",
                fg="black", bg="white", command=selectdir2)
mp4.pack()


root.mainloop()
