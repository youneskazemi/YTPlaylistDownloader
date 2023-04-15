# Youtube Playlist Downloader

A Python script to download all the videos in a Youtube playlist.

## Installation

<br />

1. Clone the repository:
   To list the contents of the current directory, use the `ls` command.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

<br />

## Usage

<br />

1. Open a terminal and navigate to the project directory.

2. Run the script with the following command:

```bash
python playlist_downloader.py <playlist_url> [--output_path OUTPUT_PATH]
```

### Required Arguments:

- `playlist_url`: The URL of the Youtube playlist.

### Optional Arguments:

- `output_path`: The directory where the videos will be saved. Default is the current directory.

<br />

## Examples

Download all the videos in the playlist with the default output directory:

```arduino
python playlist_downloader.py https://www.youtube.com/playlist?list=PLAYLIST_ID
```

Download all the videos in the playlist and save them to a specific directory:

```bash
python playlist_downloader.py https://www.youtube.com/playlist?list=PLAYLIST_ID --output_path /path/to/directory
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/ParadoX9798/YTPlaylistDownloader-/blob/main/LICENSE) file for details.
