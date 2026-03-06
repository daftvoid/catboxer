from pathlib import Path

import requests


def upload(filename: str, data: bytes):
    res = requests.post("https://catbox.moe/user/api.php",
        headers={},
        data={
            "userhash": "",
            "reqtype": "fileupload"
        },
        files={
            "fileToUpload": (
                filename,
                data,
                "application/octet-stream"
            )
        }
    )
    res.raise_for_status()

    return res.text.strip()

def download_to_file(url: str, filepath: Path):
    content = download(url)

    if not filepath.is_file():
        filepath = filepath / url.split("/")[-1]

    with open(filepath, "wb") as f:
        f.write(content)

def download(url:str) -> bytes:
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    res.raise_for_status()

    return res.content