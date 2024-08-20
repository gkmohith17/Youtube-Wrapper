import pytest
from yt_wrapper.youtube_transcript.youtube_transcript import YouTubeTranscriptAPIWrapper

def test_get_transcript():
    api = YouTubeTranscriptAPIWrapper()
    transcript = api.get_transcript('05dwAAGgw5o')  # Replace with a valid video ID that has a transcript
    assert len(transcript) > 0
    assert 'text' in transcript[0]

def test_get_transcript_with_translation():
    api = YouTubeTranscriptAPIWrapper()
    translated_transcript = api.get_transcript_with_translation('Ks-_Mh1QhMc', target_language='es')  # Spanish translation
    assert len(translated_transcript) > 0
    assert 'text' in translated_transcript[0]

def test_transcript_not_available():
    api = YouTubeTranscriptAPIWrapper()
    with pytest.raises(Exception):  # Expecting an exception for videos with no transcript
        api.get_transcript('Pk_gNYDAGIE')  # Replace with a video ID known to have no transcript
