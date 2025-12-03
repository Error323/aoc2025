import requests
import datetime
import sys
import os

from pathlib import Path

now = datetime.datetime.now()

AOC_YEAR = now.year
DAY = now.day

def download_aoc_input(year, day, session_cookie, save_path):
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {
        "Cookie": f"session={session_cookie}",
        "User-Agent": "adventofcode-input-downloader"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        with open(save_path, 'w') as file:
            file.write(response.text)
    else:
        print(f"Failed to download input file. HTTP Status: {response.status_code}")
        print("Response:", response.text)

if __name__ == "__main__":
    path = Path(__file__).parent
    save_file_path = path / f"day{DAY}/input.txt"
    save_file_path.parent.mkdir(exist_ok=True)
    download_aoc_input(AOC_YEAR, DAY, os.getenv("AOC_COOKIE"), save_file_path)
    with open(save_file_path, "rt") as f:
        for i, line in enumerate(f):
            if i > 20:
                print("...")
                break
            print(line, end='')

