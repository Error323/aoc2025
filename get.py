import requests
import datetime
import sys

from pathlib import Path

now = datetime.datetime.now()

AOC_YEAR = now.year
DAY = now.day
SESSION_COOKIE = "53616c7465645f5f03eeeacba6c44355d905edbcae34a27bd05d5873c3c38f4616f96f7e320c21523a7819a1cec5fce876726c8bd535d0bdc63e53e0853d8bc6"

def download_aoc_input(year, day, session_cookie, save_path):
    """
    Download the Advent of Code input file for a given day using the session cookie.
    
    :param year: The year of the Advent of Code event.
    :param day: The day of the challenge.
    :param session_cookie: Your session cookie for adventofcode.com.
    :param save_path: Path to save the downloaded input file.
    """
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
    download_aoc_input(AOC_YEAR, DAY, SESSION_COOKIE, save_file_path)
    with open(save_file_path, "rt") as f:
        for i, line in enumerate(f):
            if i > 20:
                print("...")
                break
            print(line, end='')

