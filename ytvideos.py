from youtube_transcript_api import YouTubeTranscriptApi
from pytube import extract
def getVideoID(video_url):
    """
    Extracts the video ID from a YouTube video URL.
    """
    video_id = None
    if "youtube.com" in video_url or "youtu.be" in video_url:
        try:
            video_id = extract.video_id(video_url)
        except Exception as e:
            print(f"Error extracting video ID: {e}")
    return video_id
def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)

    return transcript
        
        