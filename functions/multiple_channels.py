from functions.config import youtube


def search_channel_ids(youtube, channel_names):
    channel_ids = []
    for channel_name in channel_names:
        request = youtube.search().list(
            q=channel_name,
            type='channel',
            part='id,snippet',
            maxResults=1  
        )
        response = request.execute()
        

        if response['items']:
            channel_id = response['items'][0]['id']['channelId']
            channel_ids.append(channel_id)
        else:
            channel_ids.append(None)

    return channel_ids

def get_multiple_channel_stats(youtube, channel_ids):
    all_data = []
    request = youtube.channels().list(
        part='snippet,contentDetails,statistics',
        id=','.join(filter(None, channel_ids))  
    )
    response = request.execute()

    for i in range(len(response['items'])):
        data = dict(
            channel_name=response['items'][i]['snippet']['title'],
            subscribers=response['items'][i]['statistics']['subscriberCount'],
            views=response['items'][i]['statistics']['viewCount'],
            total_videos=response['items'][i]['statistics']['videoCount'],
            likes=int(response['items'][i]['statistics'].get('likeCount', 0)),  # Fixed
            comments=int(response['items'][i]['statistics'].get('commentCount', 0)),  # Fixed
            playlist_id=response['items'][i]['contentDetails']['relatedPlaylists']['uploads']
        )
        all_data.append(data)

    return all_data
