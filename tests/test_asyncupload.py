import pytest
from catboxpy import AsyncCatboxClient

@pytest.mark.asyncio
async def test_upload_url_async():
    client = AsyncCatboxClient()
    url = await client.upload("tests/example.jpg")
    assert url.startswith("https://files.catbox.moe/")
