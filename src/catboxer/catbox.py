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

def download(url: str, filepath: Path):
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    res.raise_for_status()

    if not filepath.is_file():
        filepath = filepath / url.split("/")[-1]

    with open(filepath, "wb") as f:
        f.write(res.content)


if __name__ == '__main__':
    url = upload("testfile.txt", b"this is a test file!")
    print(url)

    download(url, "testfile.txt")