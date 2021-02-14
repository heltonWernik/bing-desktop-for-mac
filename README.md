# bing-desktop-for-mac
This is bing Wallpaper created for MAC

Bing Wallpaper includes a collection of beautiful images from around the world that have been featured on the Bing homepage. Not only will you see a new image on your desktop each day, but you can also browse images and learn where they're from.

## How to use
1. Download this script
2. On line 25,37,41,42 edit for your path
3. Test it locally and install all dependencies 
4. It works... Great, lets do it automatically 
5. Go to `~/Library/LaunchAgents` and paste the file `play.scripts.wallpaper.plist`
6. Edit `play.scripts.wallpaper.plist` and put the path for the `wallpaper.py` script on "line 10"
7. Run `launchctl load ~/Library/LaunchAgents/play.scripts.wallpaper.plist`

## Options
- Its works for one desktop or for two, just check inside the script 

Thats it