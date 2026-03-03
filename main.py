import argparse

def upload(args):
    print(f"Uploading {args.files}, encrypt={args.encrypt} compress={args.compress}")

def download(args):
    print(f"Downloading {args.file} to {args.output}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="catboxer")

    subparsers = parser.add_subparsers(title="commands", dest="command", required=True)

    upload_parser = subparsers.add_parser("upload", help="Upload files")
    upload_parser.add_argument("files", nargs="+", help="Files to upload")
    upload_parser.add_argument("--encrypt", action="store_true", default=True, help="Encrypt files")
    upload_parser.add_argument("--compress", action="store_true", default=True, help="Compress files")
    upload_parser.set_defaults(func=upload)

    download_parser = subparsers.add_parser("download", help="Download files")
    download_parser.add_argument("file", help="URL of the file to download")
    download_parser.add_argument("--output", default=".", help="Output path")
    download_parser.set_defaults(func=download)

    args = parser.parse_args()
    args.func(args)