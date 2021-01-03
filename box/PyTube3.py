from pytube import YouTube
import os
import sys
import pathlib

url = input("Enter the YouTube URL : ")
YouTube(url).streams.get_highest_resolution().download('./Downloads/YouTube')

t = YouTube(url).title
title = t.replace('|', '')
Title = title.replace(' ', '')
print(Title)

abs = '/Users/keetane/Downloads/YouTube/'
oldpath = abs + title + '.mp4'
newpath = abs + Title + '.mp4' 
print(oldpath)
print(newpath)
os.rename(oldpath, newpath)

mp3path = abs + Title + '.mp3'
mp4 = str(newpath)
mp3 = str(mp3path)