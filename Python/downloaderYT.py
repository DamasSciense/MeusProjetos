from pytubefix import YouTube

def download_video(url, output_path='.'):
    try:
        # Create a YouTube object with the URL
        yt = YouTube(url)
        
        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()
        
        print(f"Downloading: {yt.title}")
        
        # Download the video
        video_stream.download(output_path)
        
        print("Download completed!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input the YouTube video URL
    video_url = input("Enter the YouTube video URL: ")
    
    # Optional: Specify the output path
    output_directory = input("Enter the output directory (or press Enter to use current directory): ") or '.'

    download_video(video_url, output_directory)