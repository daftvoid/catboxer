import argparse
import glob
from pathlib import Path

from catboxer.catbox import upload, download


def upload_file(args):
    files = []

    for file in args.files:
        matches = glob.glob(file)
        if matches:
            files.extend(matches)
        else:
            files.append(file)

    print(f"Uploading {files}, encrypt={args.encrypt} compress={args.compress}")

    for file in files:
        path = Path(file)
        if path.is_file():
            link = upload(path.name, path.read_bytes())
            print(link)

def download_file(args):
    print(f"Downloading {args.file} to {args.output}")

    download(args.file, Path(args.output))

def main():
    parser = argparse.ArgumentParser(prog="catboxer")

    subparsers = parser.add_subparsers(title="commands", dest="command", required=True)

    upload_parser = subparsers.add_parser("upload", help="Upload files")
    upload_parser.add_argument("files", nargs="+", help="Files to upload")
    upload_parser.add_argument("--encrypt", action="store_true", default=True, help="Encrypt files")
    upload_parser.add_argument("--compress", action="store_true", default=True, help="Compress files")
    upload_parser.set_defaults(func=upload_file)

    download_parser = subparsers.add_parser("download", help="Download files")
    download_parser.add_argument("file", help="URL of the file to download")
    download_parser.add_argument("--output", default=".", help="Output path")
    download_parser.set_defaults(func=download_file)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()