import os
import json
import argparse
from time import sleep
from urllib.request import (Request, urlopen, urlretrieve)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--sub', '-s')
    parser.add_argument('--count', '-c')
    args = parser.parse_args()
    count = args.count
    sub = args.sub
    imgs_folder = 'imgs_' + sub
    imgs_url = 'https://www.reddit.com/r/' + sub + '/.json' + '?count='+count
    req = Request(imgs_url)
    req.add_header('User-agent', 'Stylesheet images downloader Py3 v1')
    imgs_json = json.loads(urlopen(req).read())

    imgs = []
    for i in range(1, int(count)+1):
        # print(imgs_json["data"]["children"][i]["data"]["url"])
        imgs.append(imgs_json["data"]["children"][i]["data"]["url"])

    # imgs = [i for i in imgs_json['data']['images']]

    def fetch_images(total, count):
        if not os.path.exists(imgs_folder):
            os.makedirs(imgs_folder)
        os.chdir(imgs_folder)

        for i in imgs:
            url = i

            ext = url.split('/')[-1]
            if '?' in ext:
                # urllink="http://url.something.com/bla.html?querystring=stuff"
                ext = ext.split('?')[0]
                print(ext)
            # print(ext)
            name = i
            urlretrieve(url, ext)
            print('Downloading ' + str(count) +
                  ' of ' + str(total) + ' - ' + ext)
            count += 1
            # sleep(1)

    if imgs:
        # print(imgs)
        total = len(imgs)
        fetch_images(total, count=1)
    else:
        print("No images found")


if __name__ == "__main__":
    main()
