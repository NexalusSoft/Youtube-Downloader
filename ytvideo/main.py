class YoutubeDownloader:
    video_url: str
    save_path: str
    
    def __init__(self, video_url: str, save_path: str) -> None:
        self.video_url = video_url
        self.save_path = save_path
