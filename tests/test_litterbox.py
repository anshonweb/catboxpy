import pytest
from catboxpy import LitterboxClient

@pytest.mark.asyncio
async def test_upload_file():
    client = LitterboxClient()
    url = await client.upload("tests/example.jpg", expire_time="1h")
    assert url.startswith("https://files.catbox.moe/")