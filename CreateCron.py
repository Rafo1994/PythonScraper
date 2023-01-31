import os
import sys

dirPath = os.path.dirname(os.path.realpath(__file__))
outputFile = "/etc/cron.d/crontab"

job = "* * * * * " + sys.executable + " " + dirPath + "/App.py\n"

with open(outputFile, "w") as text_file:
    text_file.write(job)
