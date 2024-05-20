# Python Imports
import re
import requests

class YoutubeDownloader:
    """
    Class for downloading youtube videos

    Args:
        url(str): url of the video
        path(str): path to save the video
    """
    url: str
    path: str
    _html_content: bytes

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
    
    @property
    def html_content(self) -> bytes:
        """
        Get the html content of the video

        Returns:
            html_content(bytes): html content of the video
        """
        if self._html_content is None:
            self._html_content = requests.get(self.watch_url).content
        return self._html_content
    
    @property
    def video_title(self) -> str:
        """
        Get the title of the video

        Returns:
            title(str): title of the video
        """
        return re.search(r"\<title\>(.*)\<\/title\>", str(self.html_content)).group(1)
        
    @property
    def video_thumbnail(self) -> str:
        """
        Get the thumbnail of the video

        Returns:
            thumbnail(str): thumbnail of the video
        """
        return re.search(r"src=\"(.*)\"", str(self.html_content)).group(1)

    @property
    def video_info(self) -> dict:
        """
        Get the info of the video

        Returns:
            info(dict): info of the video
        """
        return {
            "title": self.video_title,
            "thumbnail": self.video_thumbnail
        }