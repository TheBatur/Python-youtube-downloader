from pytube import YouTube
import os

def Download(link):
    youtubeObject = YouTube(link)
    try:

        if(secim=="3"):
            print("\nYükleniyor..")
            video = youtubeObject.streams.filter(only_audio=True).first()
            out_file=video.download("C:\YoutubeDownloader")

            base,ext = os.path.splitext(out_file)
            new_file = base+ '.mp3'
            os.rename(out_file, new_file)

        if(secim=="4"):
            print("\nYükleniyor..")
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            youtubeObject.download("C:\YoutubeDownloader")

    except:
        print("Hata")
    print('Yükleme konumu: "C:\YoutubeDownloader"')
    print("İşlem bitti\n\n")

while(True):
    link = input("Youtube video URL: ")
    youtubeObject = YouTube(link)

    print("\nBaşlık: ", youtubeObject.title)
    print("İzlenme sayısı: ", youtubeObject.views)
    print("Video Uzunluğu:", youtubeObject.length, "saniye\n")

    secim= input("Yapmak istediğiniz işlemi giriniz.\nMP3 için'3'\nMP4(720P) için '4' yazınız.\n")
    Download(link)

