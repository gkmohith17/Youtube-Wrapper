from .youtube_data.youtube_data import YouTubeDataAPI
from .youtube_transcript.youtube_transcript import YouTubeTranscriptAPIWrapper

class YouTubeAPIWrapper:
    def __init__(self, api_key):
        self.data_api = YouTubeDataAPI(api_key)
        self.transcript_api = YouTubeTranscriptAPIWrapper()

    def get_video_info_and_transcript(self, video_id, languages=['en']):
        video_details = self.data_api.get_video_details(video_id)
        transcript = self.transcript_api.get_transcript(video_id, languages)
        return {
            'video_details': video_details,
            'transcript': transcript
        }
