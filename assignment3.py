import argparse
import urllib.request
import datetime
import csv
import re


def downloadData(url):
    response = urllib.request.urlopen(url)
    data = response.read().decode('utf-8')
    return data


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

    hour_count = {
        'Hour 01': 0,
        'Hour 02': 0,
        'Hour 03': 0,
        'Hour 04': 0,
        'Hour 05': 0,
        'Hour 06': 0,
        'Hour 07': 0,
        'Hour 08': 0,
        'Hour 09': 0,
        'Hour 10': 0,
        'Hour 11': 0,
        'Hour 12': 0,
        }

    row_count = 0
    image_counter = 0
    for row in csv.reader(data_lines):
    #    print(row)
        if len(row) == 0:
            continue
        row_count += 1
        url_hit, timestamp_str, browser, status_code, hit_size = row
    #    print(timestamp_str)
        hour = str(timestamp_str[11:13])
        #print(hour)
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


        if hour == "01":
            hour_count["Hour 01"] += 1
        elif hour == "02":
            hour_count["Hour 02"] += 1
        elif hour == "03":
            hour_count["Hour 03"] += 1
        elif hour == "04":
            hour_count["Hour 04"] += 1
        elif hour == "05":
            hour_count["Hour 05"] += 1
        elif hour == "06":
            hour_count["Hour 06"] += 1
        elif hour == "07":
            hour_count["Hour 07"] += 1
        elif hour == "08":
            hour_count["Hour 08"] += 1
        elif hour == "09":
            hour_count["Hour 09"] += 1
        elif hour == "10":
            hour_count["Hour 10"] += 1
        elif hour == "11":
            hour_count["Hour 11"] += 1
        elif hour == "12":
            hour_count["Hour 12"] += 1


    percent = (int(image_counter) / int(row_count)) * 100
    print("Image requests account for {}% of all requests".format(percent))

    max_hits = max(browser_count, key=browser_count.get)
    print("The most popular browser is:", max_hits)
    print(browser_count)

    print("Hour 01 has {} hits".format(hour_count["Hour 01"]))
    print("Hour 02 has {} hits".format(hour_count["Hour 02"]))
    print("Hour 03 has {} hits".format(hour_count["Hour 03"]))
    print("Hour 04 has {} hits".format(hour_count["Hour 04"]))
    print("Hour 05 has {} hits".format(hour_count["Hour 05"]))
    print("Hour 06 has {} hits".format(hour_count["Hour 06"]))
    print("Hour 07 has {} hits".format(hour_count["Hour 07"]))
    print("Hour 08 has {} hits".format(hour_count["Hour 08"]))
    print("Hour 09 has {} hits".format(hour_count["Hour 09"]))
    print("Hour 10 has {} hits".format(hour_count["Hour 10"]))
    print("Hour 11 has {} hits".format(hour_count["Hour 11"]))
    print("Hour 12 has {} hits".format(hour_count["Hour 12"]))

if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    args = parser.parse_args()
    main(args.url)
