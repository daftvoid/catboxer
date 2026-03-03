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