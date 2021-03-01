from pytube import YouTube
url = input("Enter the youtube link: ")
video = YouTube(url)
stream = video.streams.get_highest_resolution()
stream.download('path/to/folder')
