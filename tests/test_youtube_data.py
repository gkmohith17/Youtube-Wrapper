import pytest
from yt_wrapper.youtube_data.youtube_data import YouTubeDataAPI

api_key = 'AIzaSyCsxaHNDVyEi4dweqmXpbtIOSvhljfkE1c'

def test_get_video_details():
    api = YouTubeDataAPI(api_key=api_key)
    details = api.get_video_details('05dwAAGgw5o')  # Replace with a valid video ID
    assert 'title' in details['snippet']
    assert 'viewCount' in details['statistics']

def test_search_videos():
    api = YouTubeDataAPI(api_key=api_key)
    results = api.search_videos('Python Programming')
    assert len(results) > 0
    assert 'title' in results[0]['snippet']

def test_list_channel_videos():
    api = YouTubeDataAPI(api_key=api_key)
    videos = api.list_channel_videos('UCb4AW4DtF_iS4_eNuTgEgRA')  # Replace with a valid channel ID
    assert len(videos) > 0
    assert 'title' in videos[0]['snippet']
