import requests
from .album import AlbumManager

CATBOX_API = 'https://catbox.moe/user/api.php'


class CatboxClient:

    def __init__(self, userhash: str | None = None):

        self.userhash = userhash
        self.album = AlbumManager(userhash=self.userhash) 
        

    def upload(self,file_or_url: str) ->str:
        '''Upload an File to Catbox
            by uploading a file or by using an Url.'''
        
        if file_or_url.startswith('https://') or file_or_url.startswith('http://'):
            return self.url_upload(file_or_url)
        
        else:
            return self.file_upload(file_or_url)
    
    def file_upload(self, file_path: str):
        data={
            'reqtype':'fileupload',
            }  
        if self.userhash:
            data["userhash"] = self.userhash
        with open(file_path, 'rb') as f:
            files = {'fileToUpload' : f}
            response = requests.post(CATBOX_API, data=data, files=files)
        
        if response.status_code==200:
            return response.text.strip()
        else:
            raise Exception(f'Failed to Upload File: {response.status_code} {response.text}')
        


    def url_upload(self, file_url: str) -> str:
        data = {
            "reqtype": "urlupload",
            "url": file_url,
        }
        if self.userhash:
            data["userhash"] = self.userhash

        response = requests.post(CATBOX_API, data=data)
        if response.status_code == 200:
            return response.text.strip()
        else:
            raise Exception(f"URL upload failed: {response.status_code} {response.text}")

        

    def delete_file(self, filename: str) -> str:
        if not self.userhash:
            raise ValueError("Userhash is required to delete files")

        data = {
            "reqtype": "deletefiles",
            "userhash": self.userhash,
            "files": filename  
        }
        res = requests.post(CATBOX_API, data=data)
        return res.text.strip()

