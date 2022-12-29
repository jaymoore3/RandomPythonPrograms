import pytube

# Set the URL of the YouTube video you want to download
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Create a YouTube object
yt = pytube.YouTube(url)

# Get the first video in the list of videos available for the YouTube object
video = yt.get('mp4', '720p')

# Set the destination path for the downloaded video
destination = './'

# Download the video
video.download(destination)
