from pytube import YouTube
 
url = input("Enter the YouTube URL : ")
print("now downloading...")
YouTube(url).streams.get_highest_resolution().download('./Downloads/YouTube')
print("fertig")