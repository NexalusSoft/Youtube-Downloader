# Python Imports
import re

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

        self.video_id = self.extract_video_id(self.video_url)

        self.watch_url = f"https://youtube.com/watch?v={self.video_id}"
        self.embed_url = f"https://www.youtube.com/embed/{self.video_id}"

    def extract_video_id(self, url: str) -> str:
        """
        Extract video_id from url

        Args:
            url(str): url of the video

        Returns:
            video_id(str): id of the video
        """
        return re.search(r"((?<=(v|V)/)|(?<=be/)|(?<=(\?|\&)v=)|(?<=embed/))([\w-]+)", url).group(1)