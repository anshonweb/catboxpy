import requests


class LitterboxClient:

    LITTERBOX_API = "https://litterbox.catbox.moe/resources/internals/api.php"
    VALID_TIMES = ["1h", "12h", "24h", "72h"]

    def __init__(self):
        pass

    def upload_file(self, filepath: str, expire_time: str = "24h") -> str:
        """
        Upload a file to Litterbox.
        
        :param filepath: Path to the file to upload
        :param expire_time: Time before the file expires ('1h', '12h', '24h', or '72h')
        :return: URL to the uploaded file
        :raises: ValueError if expire_time is invalid, or requests.exceptions.RequestException on network errors
        """

        if expire_time not in self.VALID_TIMES:
            raise ValueError(f"Invalid expire_time '{expire_time}'. Must be one of {self.VALID_TIMES}")
        
        with open(filepath, "rb") as f:
            files = {
                "fileToUpload": f
            }
            data = {
                "reqtype": "fileupload",
                "time": expire_time
            }

            response = requests.post(self.LITTERBOX_API, files=files, data=data)
            response.raise_for_status()

            if response.text.startswith("https://"):
                return response.text.strip()
            else:
                raise RuntimeError(f"Unexpected response from Litterbox: {response.text}")