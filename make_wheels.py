import sys
from pathlib import Path
import urllib.request


XVAL_PLATFORMS = {
    'x86_64-windows': 'win_amd64',
}

def write_xval_wheel(out_dir:Path, version:str, platform:str, binary:str):
    contents = {}
    with open("src/xval/__init__.py") as f: 
        contents['xval/__init__.py'] = f.read()

    with open("src/xval/xval.py") as f: 
        contents['xval/xval.py'] = f.read()

    print(contents['xval/__init__.py'])


def fetch_and_write_xval_wheels( xval_version: str ):
    folder_path = Path("dist") / xval_version
    folder_path.mkdir(exist_ok = True)

    for xval_platform, python_platform in XVAL_PLATFORMS.items():
        xval_url = f"https://www.xval.io/releases/{xval_version}/xval.exe"
        print(xval_url)
        with urllib.request.urlopen(xval_url) as request:
            xval_binary = request.read() 

        write_xval_wheel(
            out_dir = folder_path,
            version = xval_version,
            platform = python_platform,
            binary = xval_binary
        )


def main():
    if len(sys.argv) < 2: 
        print("Usage: make_wheels <version string>")
        return

    fetch_and_write_xval_wheels(
        xval_version = sys.argv[1]   
    )

if __name__ == '__main__':
    main()
