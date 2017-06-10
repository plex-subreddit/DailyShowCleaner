#!/usr/bin/python

import os
import datetime
import shutil

showCleanerHome = '/opt/scripts/showCleaner'
showList = []

# Reads list of shows to clean
with open(os.path.join(showCleanerHome, "showsListWithNumbers.txt")) as file:
    dirList = file.read().splitlines()
    for line in dirList:
        newLine = line.split(':')
        showList.append(newLine)

# Walks the directory in the list, finding all video files, splitting them
# and then it turns them into a list of tupples.
for showPath in showList:
    shows = []
    listOfSeasons = []
    num = int(showPath[1])
    for (showPath[0], dirs, files) in os.walk(showPath[0]):

        # Gets a list of full paths to all season dirs and removes any empty ones  
        for seasonDir in dirs:
            if seasonDir != None:
                if os.listdir(os.path.join(showPath[0], seasonDir)) == []:
                    shutil.rmtree(os.path.join(showPath[0], seasonDir))
                else:
                    listOfSeasons.append(os.path.join(showPath[0], seasonDir))
            
        for item in files:
            if item.endswith(('.mkv', '.mp4', '.avi', '.wmv', '.mpeg')):
                newItem = tuple(item.split(" - "))
                shows.append(newItem)

    # Try Catch block for files with dates vs sXXeXX
    try:
        # Sorting based on date
        newShowList = sorted(shows, key=lambda x: datetime.datetime.strptime(x[1], '%Y-%m-%d'), reverse=True)
        try:
            # If it exists, deletes the next file after the amount specified in the config
            os.remove(os.path.join(showPath[0], newShowList[num][0] + " - " + newShowList[num][1] + " - " + newShowList[num][2]))
            print "removed {0}".format(os.path.join(showPath[0], newShowList[num][0] + " - " + newShowList[num][1] + " - " + newShowList[num][2]))
        except IndexError as e1:
            pass
    except ValueError as VE1:
        # Sorts based on sXXeXX naming scheme
        newShowList = sorted(shows, key=lambda x: x[1], reverse=True)
        try:
            # If it exists, deletes the next file after the amount specified in the config
            os.remove(os.path.join(showPath[0], newShowList[num][0] + " - " + newShowList[num][1] + " - " + newShowList[num][2]))
            print "removed {0}".format(os.path.join(showPath[0], newShowList[num][0] + " - " + newShowList[num][1] + " - " + newShowList[num][2]))
        except IndexError as e2:
            pass

    # Checks season folders for video files and removes them if none are left
    for seasonSpecific in listOfSeasons:
        count = 0
        for files in os.listdir(seasonSpecific):
            if files.endswith(('.mkv', '.mp4', '.avi', '.wmv', '.mpeg')):
                count += 1
        if count == 0:
            shutil.rmtree(seasonSpecific)