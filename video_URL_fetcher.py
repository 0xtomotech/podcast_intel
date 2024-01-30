
from googleapiclient.discovery import build
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
import csv
import os

# Load environment variables
load_dotenv()

# Initialize YouTube API Client
# api_key = 'AIzaSyCZ-z-0xbKsKfaqfBNw2v5vvQYG47nUZCs'
api_key = os.getenv('YOUTUBE_API_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

channel_id = {
    'ThinkingBasketball': 'UC3HPbvB6f58X_7SMIp6OPYw',
}

# channel_id = {
#     'TheRinger': 'UCT83YP07yVuaH9J19YABhlw',
#     'BillSimmons': 'UCP032AGFh2KzzIUGylB9BjA',
#     'JJRedick': 'UCbPY1Efha9VPRBYW2x1M16A',
#     'ThinkingBasketball': 'UC3HPbvB6f58X_7SMIp6OPYw',
# }

# Function to get the upload playlist ID of a channel for a given number of months dating back


# Function to get the ID of the 'uploads' playlist from a YouTube channel
def get_upload_playlist_id(channel_id):
    # Make a request to the YouTube API to get the channel details
    request = youtube.channels().list(part='contentDetails', id=channel_id)
    # Execute the request and get the response
    response = request.execute()
    # Return the ID of the 'uploads' playlist
    return response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# Function to get videos from a playlist


def get_videos_from_playlist(playlist_id, date_limit):
    """
    Fetches videos from a YouTube playlist based on the provided playlist ID and date limit.

    Args:
        playlist_id (str): The ID of the YouTube playlist.
        date_limit (datetime.datetime): The date limit to filter the videos.

    Returns:
        list: A list of dictionaries containing the title, URL, and published date of the videos.
    """
    # Initialize an empty list to store the videos
    videos = []
    # Initialize the next_page_token to None
    next_page_token = None

    # Loop until all pages of the playlist have been fetched
    while True:
        # Make a request to the YouTube API to get the playlist items
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        # Execute the request and get the response
        response = request.execute()

        # Loop through each item in the response
        for item in response['items']:
            # Get the video ID, title, and published date
            video_id = item['snippet']['resourceId']['videoId']
            title = item['snippet']['title']
            published_at = item['snippet']['publishedAt']
            # Convert the published date to a datetime object
            published_at_datetime = datetime.strptime(
                published_at, '%Y-%m-%dT%H:%M:%SZ')
            # Format the published date as a string in the format 'YYYYMMDD'
            published_at_formatted = published_at_datetime.strftime('%Y%m%d')
            # If the video was published after the date limit, add it to the list of videos
            if published_at_datetime >= date_limit:
                videos.append(
                    {'title': title,
                     'url': f'https://www.youtube.com/watch?v={video_id}',
                     'published_at': published_at_formatted})

        # Get the token for the next page of the playlist
        next_page_token = response.get('nextPageToken')
        # If there is no next page, break the loop
        if not next_page_token:
            break

    # Return the list of videos
    return videos


# Main script execution
if __name__ == "__main__":
    for channel in channel_id:
        upload_playlist_id = get_upload_playlist_id(channel_id[channel])
        months_back = 120
        date_limit = datetime.now() - relativedelta(months=months_back)
        videos = get_videos_from_playlist(upload_playlist_id, date_limit)
        print(f"finished getting videos for {channel}")

        # Ensure the directory exists
        os.makedirs('videolists', exist_ok=True)
        with open(f'videolists/videolist_{channel}_L{months_back}M.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Title', 'URL', 'PublishDate'])

            for video in videos:
                writer.writerow(
                    [video['title'], video['url'], video['published_at']])

        print(f"Video list saved for {channel}.csv")
