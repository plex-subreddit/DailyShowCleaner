# Daily Show Cleaner

This script is written around the idea that there's no point in storing old shows that air daily like the daily show, stephen colbert or jimmy kimmel. Set this up and keep only the latest episodes.

### Install Directions
* Edit "ShowsListWithNumber with the path to your files
* Add a colon after the path with the number of shows you would like to keep
    * Ex: /path/to/TV/show name:10
* Add it to your crontab or windows task scheduler

### Quick Notes
* If the script finds more than the number of shows that is set in the ShowsWithNumbers file, it will only delete one at a time. It may need to run multiple times if it needs to catch up
* The script supports the file types: mkv, mp4 avi, wmv and mpeg. More support can be added if needed by finding the list of filetypes in the script
