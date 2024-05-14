# Python Imports
import re

class YoutubeDownloader:
    """
    Class for downloading youtube videos

    Args:
        url(str): url of the video
        path(str): path to save the video
    """
    url: str
    path: str

    def __init__(self, url: str, path: str) -> None:
        self.video_url = url
        self.save_path = path

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