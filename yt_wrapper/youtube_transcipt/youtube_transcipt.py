from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

class YouTubeTranscriptAPIWrapper:
    def get_transcript(self, video_id, languages=['en']):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
            return transcript
        except (TranscriptsDisabled, NoTranscriptFound) as e:
            return str(e)

    def get_transcript_with_translation(self, video_id, target_language='en'):
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        translated_transcript = YouTubeTranscriptApi.translate_transcript(transcript, target_language)
        return translated_transcript
