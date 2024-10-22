from functions.config import youtube


# getting video_ids using playlist_id
def get_video_id(youtube,playlist_id):
   

    request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=50
    )

    response=request.execute()

    video_ids=[]

    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])

    
    next_page_token = response.get('nextPageToken')
    more_pages=True
     
    while more_pages:
        if next_page_token is None:
            more_pages=False
        else:
            request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
            )
            response=request.execute()

            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])

            next_page_token = response.get('nextPageToken')




       
    return video_ids


def get_video_details(youtube, video_ids):
    all_video_stats = []

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part='snippet,statistics,contentDetails',
            id=','.join(video_ids[i:i + 50])
        )
        response = request.execute()

        for video in response['items']:
            video_stats = dict(
                Title=video['snippet']['title'],
                published_date=video['snippet']['publishedAt'],
                views=int(video['statistics']['viewCount']),
                likes=int(video['statistics'].get('likeCount', 0)),
                dislikes=int(video['statistics'].get('dislikeCount', 0)),
                comments=int(video['statistics'].get('commentCount', 0)),
                thumbnail_url=video['snippet']['thumbnails']['high']['url'],
                duration=video['contentDetails']['duration']  
            )

            all_video_stats.append(video_stats)

    return all_video_stats