from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen


def downloadVideo(link, id,location):
    print(f"Downloading video {id} from: {link}")
    cookies = {
        '__cflb': '02DiuEcwseaiqqyPC5qqJA27ysjsZzMZ791tHv5SKBU7m',
        '_ga': 'GA1.2.1900161439.1678039828',
        '_gid': 'GA1.2.1483917536.1678039828',
        '__gads': 'ID=165aa62986d316d4-221e6331b4de00bf:T=1678039828:RT=1678039828:S=ALNI_Mbp8fzhQB0cFXCmvPwlTI0cpgYWig',
        '__gpi': 'UID=000009c941f8d3e5:T=1678039828:RT=1678039828:S=ALNI_MaU3LhlpTjkS4SKX2yqaiBFkLW3fw',
        '_gat_UA-3524196-6': '1',
        # Please get this data from the console network activity tool
        # This is explained in the video :)
    }

    headers = {
        'authority': 'ssstik.io',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'cookie': '__cflb=02DiuEcwseaiqqyPC5qqJA27ysjsZzMZ791tHv5SKBU7m; _ga=GA1.2.1900161439.1678039828; _gid=GA1.2.1483917536.1678039828; __gads=ID=165aa62986d316d4-221e6331b4de00bf:T=1678039828:RT=1678039828:S=ALNI_Mbp8fzhQB0cFXCmvPwlTI0cpgYWig; __gpi=UID=000009c941f8d3e5:T=1678039828:RT=1678039828:S=ALNI_MaU3LhlpTjkS4SKX2yqaiBFkLW3fw; _gat_UA-3524196-6=1',
        'hx-current-url': 'https://ssstik.io/en',
        'hx-request': 'true',
        'hx-target': 'target',
        'hx-trigger': '_gcaptcha_pt',
        'origin': 'https://ssstik.io',
        'referer': 'https://ssstik.io/en',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
        # Please get this data from the console network activity tool
        # This is explained in the video :)
    }

    params = {
        'url': 'dl',
    }

    data = {
        'id': link,
        'locale': 'en',
        'tt': 'SDVTQ1Fj',
        # NOTE: This value gets changed, please use the value that you get when you copy the curl command from the network console
    }

    print("STEP 4: Getting the download link")
    print("If this step fails, PLEASE read the steps above")
    try:
        response = requests.post('https://ssstik.io/abc', params=params, cookies=cookies, headers=headers, data=data)
        downloadSoup = BeautifulSoup(response.text, "html.parser")

        downloadLink = downloadSoup.a["href"]

        print("STEP 5: Saving the video :)")
        mp4File = urlopen(downloadLink)
        # Feel free to change the download directory
        with open(f"videos/{location}/{id}.mp4", "wb") as output:
            while True:
                data = mp4File.read(4096)
                if data:
                    output.write(data)
                else:
                    break
    except:
        print(f'downloading failed in video {id}')

def Scraping(location):
    print("STEP 1: Open Chrome browser")
    Website = f'https://www.tiktok.com/tag/{location}'
    Path = 'D:\Computational design\chromedriver_win32_new\chromedriver'
    driver = webdriver.Chrome(Path)
    # Change the tiktok link
    driver.get(Website)

    # IF YOU GET A TIKTOK CAPTCHA, CHANGE THE TIMEOUT HERE
    # to 60 seconds, just enough time for you to complete the captcha yourself.
    time.sleep(1)

    scroll_pause_time = 1
    screen_height = driver.execute_script("return window.screen.height;")
    i = 1

    print("STEP 2: Scrolling page")
    while i<10:
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        time.sleep(scroll_pause_time)
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        if (screen_height) * i > scroll_height:
            break

    soup = BeautifulSoup(driver.page_source, "html.parser")
    # this class may change, so make sure to inspect the page and find the correct class
    videos = soup.find_all("div", {"class": "tiktok-x6y88p-DivItemContainerV2 e19c29qe7"})

    print(f"STEP 3: Time to download {len(videos)} videos")
    for index, video in enumerate(videos):
        print(f"Downloading video: {index}")
        print(video.a["href"])
        downloadVideo(video.a["href"], index,location)
        time.sleep(7)

if __name__ == '__main__':
    locations =['bostoncommon','kowloonpark','luxembourggardens']
    for location in locations:
        Scraping(location)