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

    return res.text


if __name__ == '__main__':
    path = Path("text.txt")
    print(path.read_text())

    link = upload(path.name,path.read_bytes())
    print(link)