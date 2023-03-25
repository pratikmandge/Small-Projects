'''Video Downloader for highest quality @copyright - Pratik Mandge'''
import pytube

video_urls = [# add videos link here in string form with comma "," separated]

videoNumber = # Enter count of videos to download here

# Loop through each URL and download the video
for url in video_urls:
    videoNumber += 1
    # Create a YouTube object from the URL
    youtube = pytube.YouTube(url)

    # Choose the highest resolution video (stream)
    video = youtube.streams.get_highest_resolution()

    # Download the video to the current directory
    print("Video", videoNumber," is downloading...")
    video.download()
    print("Video", videoNumber," downloaded")
