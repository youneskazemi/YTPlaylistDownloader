import argparse
from pytube import Playlist, YouTube
from tqdm import tqdm
import os

os.system("cls" if os.name == "nt" else "clear")


def download_playlist(playlist_url, output_path="."):
    """
    Downloads all videos in a YouTube playlist and saves them to the specified output path.

    Parameters:
    - playlist_url (str): The URL of the YouTube playlist.
    - output_path (str): The directory where the videos will be saved. Default is the current directory.

    Returns:
    - None
    """
    # Create a playlist object from the URL
    playlist = Playlist(playlist_url)
    # Print the total number of videos in the playlist
    print(f"Total videos in the {playlist.title} playlist: {len(playlist.video_urls)}")
    values = range(len(playlist.video_urls))

    progress_bar = tqdm(values, unit="item")

    # Loop through each video in the playlist and download it
    for url, _ in zip(playlist.video_urls, progress_bar):
        downloaded = False
        retry = 0
        while not downloaded:
            try:
                youtube = YouTube(url)

                # Get the stream with the highest resolution
                video = youtube.streams.get_highest_resolution()
                mime_type = video.mime_type
                # Extract the video type from the mime type string
                video_type = mime_type.split("/")[1]
                video_title = video.title
                output_filename = f"{video_title}.{video_type}"

                # Check if the output file already exists
                if os.path.exists(f"{output_path}/{output_filename}"):
                    progress_bar.set_description(
                        f"Skipping {video_title}. Already exists."
                    )
                    break

                # Download the video and update the progress bar
                video.download(output_path)
                progress_bar.set_description(f"Downloading {video_title}")
                progress_bar.update()
                # Add the URL to the downloaded_urls list
                downloaded = True

            except Exception as e:
                retry += 1
                with open(f"{output_path}/logs.txt", "a") as log:
                    log.write(f"{e}\n")
                print(f"\nError: {e}.")
                print("retrying!")
                if retry == 5:
                    print("Timeout!")
                    break
    progress_bar.close()
    print("Playlist downloaded!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Download videos from a YouTube playlist"
    )
    parser.add_argument(
        "playlist_url", type=str, help="the URL of the YouTube playlist"
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default=".",
        help="the directory where the videos will be saved",
    )

    args = parser.parse_args()

    download_playlist(args.playlist_url, args.output_path)
