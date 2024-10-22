
from functions.config import youtube


# using channel name to get channel id
def search_channel_id(youtube, channel_name):
    request = youtube.search().list(
        q=channel_name,
        type='channel',
        part='id,snippet',
        maxResults=1  
    )
    response = request.execute()
    
    # Extract the channel ID from the response
    if response['items']:
        channel_id = response['items'][0]['id']['channelId']
        return channel_id
    else:
        return None  
    

# basic channel statistics
def get_channel_info(youtube,channel_id):
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id = channel_id
    )
    response = request.execute()

    
    data = dict(channel_name=response['items'][0]['snippet']['title'],
                    views=response['items'][0]['statistics']['viewCount'],
                    subscribers=response['items'][0]['statistics']['subscriberCount'],
                    total_videos=response['items'][0]['statistics']['videoCount'],
                    playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
        )
    

    return data

