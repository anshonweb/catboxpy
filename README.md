# catboxpy

`catboxpy` is a Python wrapper for [Catbox](https://catbox.moe/), which allows you to easily upload files, manage albums, and interact with the Catbox service. This package supports both `synchronous` and `asynchronous usage`. 
## Installation

### From PyPI

You can easily install the stable version of `catboxpy` from PyPI using pip:

```bash
pip install catboxpy
```

### From GitHub Repository

Alternatively, if you wish to access the latest (potentially unstable) version directly from the GitHub repository, you can execute the following command:

```bash
pip install git+https://github.com/anshonweb/catboxpy.git
```

## Features

- Upload files to Catbox.
- Create and manage albums (synchronous and asynchronous support).
- Delete files from Catbox.
- Both synchronous and asynchronous methods for flexible usage.

## Installation

To install `catboxpy`, simply use pip:

```bash
pip install catboxpy
```

## Usage

### **Synchronous Usage**

The synchronous interface is simple to use for blocking operations. Here is how to use it:

#### 1. **Uploading a File**

```python
from catboxpy.catbox import CatboxClient

client = CatboxClient(userhash="your_userhash_here")
file_url = client.upload("path/to/your/file.jpg")
print(f"File uploaded to: {file_url}")
```

#### 2. **Uploading a URL**

You can upload files directly from a URL:

```python
url = client.upload('https://example.com/your_image.jpg')
print(f"URL uploaded to: {url}")
```

#### 3. **Creating an Album**

To create an album:

```python
album_url = client.album.create("My Album", "Album description", ["file1.jpg", "file2.jpg"])
print(f"Album created at: {album_url}")
```

#### 4. **Deleting a File**

To delete a file by its URL:

```python
client.delete_file("file_url")
```

---

### **Asynchronous Usage**

The asynchronous interface allows you to perform operations without blocking the execution of other tasks, making it ideal for applications that need to handle multiple requests concurrently.

#### 1. **Uploading a File Asynchronously**

```python
import asyncio
from catboxpy.catbox import AsyncCatboxClient

async def upload_file():
    client = AsyncCatboxClient(userhash="your_userhash_here")
    file_url = await client.upload("path/to/your/file.jpg")
    print(f"File uploaded to: {file_url}")

# Running the async function
asyncio.run(upload_file())
```

#### 2. **Uploading a URL Asynchronously**

```python
import asyncio
from catboxpy.catbox import AsyncCatboxClient

async def upload_url():
    client = AsyncCatboxClient(userhash="your_userhash_here")
    url = await client.upload('https://example.com/your_image.jpg')
    print(f"URL uploaded to: {url}")

# Running the async function
asyncio.run(upload_url())
```

#### 3. **Creating an Album Asynchronously**

```python
import asyncio
from catboxpy.catbox import AsyncCatboxClient

async def create_album():
    client = AsyncCatboxClient(userhash="your_userhash_here")
    album_url = await client.album.create("My Album", "Album description", ["file1.jpg", "file2.jpg"])
    print(f"Album created at: {album_url}")

# Running the async function
asyncio.run(create_album())
```

#### 4. **Deleting a File Asynchronously**

```python
import asyncio
from catboxpy.catbox import AsyncCatboxClient

async def delete_file():
    client = AsyncCatboxClient(userhash="your_userhash_here")
    await client.delete_file("file_url")

# Running the async function
asyncio.run(delete_file())
```

---

### **Litterbox Usage**
```python

from catboxpy import LitterboxClient

uploader = LitterboxClient()
try:
    url = uploader.upload_file("filepath", expire_time="1h")
    print(f"Uploaded to: {url}")
except Exception as e:
    print(f"Upload failed: {e}")

```

## Authentication

For most operations, such as uploading or managing albums, you need a valid **userhash**. You can obtain the `userhash` by logging in to Catbox and accessing your user settings.

- If you're performing **anonymous uploads**, you can omit the `userhash`. However, operations like creating and managing albums require a valid `userhash`.

---

## Notes

- **Album Limitations**: Catbox albums currently allow a maximum of 500 files. This limit may change in the future.
- **Anonymous Albums**: Anonymous albums cannot be edited or deleted, and they also cannot contain more than 500 files.

---


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
---

## Contact

For issues, bugs, or suggestions, please open an issue on the [GitHub repository](https://github.com/anshonweb/catboxpy/issues).

---

```
