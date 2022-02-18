import argparse
import urllib.request
import datetime
import csv
import re


def downloadData(url):
    """Downloads the data"""
    with urllib.request.urlopen(url) as response:
        web_data = response.read().decode('utf-8')

    return web_data


def main(url):
    print(f"Running main with URL = {url}...")
    data = downloadData(url)
    data_lines = data.split("\n")
    csvreader = csv.reader(data_lines) #use the csv reader object to read the csv file

    browser_count = {
        'FIREFOX': 0,
        'CHROME': 0,
        'MSIE': 0,
        'SAFARI': 0
    }

    row_count = 0
    image_counter = 0
    for row in csv.reader(data_lines):
        if len(row) == 0:
            continue
        row_count += 1
        url_hit, timestamp_str, browser, status_code, hit_size = row
        url_hit = url_hit.upper()
        if re.search("PNG|GIF|JPG|JPEG", url_hit.upper()):
            image_counter += 1

        if re.search(r'(?i)Firefox', str(row)):
            browser_count['FIREFOX'] += 1
        if re.search(r'(?i)msie', str(row)):
            browser_count['MSIE'] += 1
        if re.search(r'(?i)chrome', str(row)):
            browser_count['CHROME'] += 1
        if re.search(r'(?i)safari', str(row)):
            browser_count['SAFARI'] += 1

    #    timestamp = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
    #    print(row)
    percent = (int(image_counter) / int(row_count)) * 100

    print("Image requests account for {}% of all requests".format(percent))
    max_hits = max(browser_count, key=browser_count.get)
    print("The most popular browser is:", max_hits)
    print(browser_count)


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
