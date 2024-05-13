class YoutubeDownloader:
    """
    Class for downloading youtube videos

    Args:
        video_url(str): url of the video
        save_path(str): path to save the video
    """
    video_url: str
    save_path: str

    def __init__(self, video_url: str, save_path: str) -> None:
        self.video_url = video_url
        self.save_path = save_path
