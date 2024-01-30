import yt_dlp
import csv
from colorama import Fore, Style


def download_videos_as_mp3(url_list, outlet_name):
    """
    Downloads videos from a list of URLs and saves them as MP3 files.

    Args:
        url_list (list[str]): A list of URLs of the videos to be downloaded.
        outlet_name (str): The name of the outlet or source.

    Returns:
        None
    """
    total_urls = len(url_list)
    for index, url in enumerate(url_list, start=1):
        with yt_dlp.YoutubeDL({}) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_type = 'short' if info_dict['duration'] <= 90 else 'long'
            options = {
                'format': 'bestaudio/best',
                'extractaudio': True,  # Only keep the audio
                'audioformat': 'mp3',  # Convert to mp3
                'outtmpl': f'audio/{outlet_name}_{video_type}_%(upload_date)s_%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            }
            print(f"Processing URL {index}/{total_urls}")
            with yt_dlp.YoutubeDL(options) as ydl_download:
                ydl_download.download([url])
        percent_complete = (index / total_urls) * 100
        print(f"{Fore.GREEN}Downloaded {
              index}/{total_urls} URLs, {percent_complete} % complete{Style.RESET_ALL}")


def load_url_list(url_file, nr_limit, search_term=None):
    """"_summary_

    Args:
        url_file (str): The file path of the CSV file containing the URLs.
        nr_limit (int): The maximum number of URLs to read from the CSV file.
        search_term (str, optional): The search term to filter the videos. Defaults to None.

    Returns:
        List[str]: A list of video URLs.
    """
    video_urls = []

    # Open the CSV file
    with open(url_file, 'r') as file:
        # Create a CSV reader
        reader = csv.reader(file)
        # Skip the header row
        next(reader)
        # Loop through each row in the CSV
        for index, row in enumerate(reader):
            # If we've already read 10 URLs, stop reading
            if index >= nr_limit:
                break

            title = row[0]  # The title is the first column in the CSV
            url = row[1]  # The URL is the second column in the CSV

            # If search_term is not None and it is in the title, add the URL to the list of video URLs
            if search_term is None or search_term.lower() in title.lower():
                video_urls.append(url)
    return video_urls


if __name__ == "__main__":

    # config
    url_file = './videolists/videolist_ThinkingBasketball_L120M.csv'
    nr_limit = 700
    search_term = None
    outlet_name = 'ThinkingBasketball'

    video_urls = []
    video_urls = load_url_list(url_file, nr_limit, search_term)

    download_videos_as_mp3(video_urls, outlet_name)
