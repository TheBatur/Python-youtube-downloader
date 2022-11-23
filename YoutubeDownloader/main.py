from pytube import YouTube
import os

def Download(link):
    youtubeObject = YouTube(link)
    try:

        if(secim=="3"):
            print("\nDownloading..")
            video = youtubeObject.streams.filter(only_audio=True).first()
            out_file=video.download("C:\YoutubeDownloader")

            base,ext = os.path.splitext(out_file)
            new_file = base+ '.mp3'
            os.rename(out_file, new_file)

        if(secim=="4"):
            print("\nDownloading..")
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            youtubeObject.download("C:\YoutubeDownloader")

    except:
        print("Error")
    print('Download Location: "C:\YoutubeDownloader"')
    print("Transaction Finished\n\n")

while(True):
    link = input("Youtube video URL: ")
    youtubeObject = YouTube(link)

    print("\nTitle: ", youtubeObject.title)
    print("Views: ", youtubeObject.views)
    print("Video Length:", youtubeObject.length, "Second\n")

    secim= input("Enter the action you want to do.\n'3' for MP3\n'4' for MP4(720P)\n")
    Download(link)
