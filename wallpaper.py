import datetime
import json
import os

import requests


def download_bing_img():
    # get image url
    response = requests.get("https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US")
    image_data = json.loads(response.text)

    image_url = image_data["images"][0]["url"]
    image_url = image_url.split("&")[0]
    full_image_url = "https://www.bing.com" + image_url

    # image's name
    image_name = datetime.date.today().strftime("%Y%m%d")
    image_extension = image_url.split(".")[-1]
    image_name = image_name + "." + image_extension

    # download and save image
    img_data = requests.get(full_image_url).content

    with open(f'/Users/israelwernik/play/scripts/wallpaper/imgs/{image_name}', 'wb') as handler:
        handler.write(img_data)
    
    return f'imgs/{image_name}'

def remove_all_files(directory):
    files_in_directory = os.listdir(directory)
    for file in files_in_directory:
        path_to_file = os.path.join(directory, file)
        os.remove(path_to_file)


remove_all_files("/Users/israelwernik/play/scripts/wallpaper/imgs")
bing_path = download_bing_img()

# if you have dual monitor use both command, if only one use just the first
command1 = f"osascript -e 'tell application \"System Events\" to set picture of current desktop to \"/Users/israelwernik/play/scripts/wallpaper/{bing_path}\"'"
command2 = f"osascript -e 'tell application \"System Events\" to set picture of second desktop to \"/Users/israelwernik/play/scripts/wallpaper/{bing_path}\"'"


os.system(command1)
os.system(command2)

# launchctl load ~/Library/LaunchAgents/play.scripts.wallpaper.plist
# launchctl unload ~/Library/LaunchAgents/play.scripts.wallpaper.plist
