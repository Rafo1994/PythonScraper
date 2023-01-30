import os
import sys

dirPath = os.path.dirname(os.path.realpath(__file__))
outputFile = "cron-job"

job = "* * * * * " + sys.executable + " " + dirPath + "/App.py \r\n"

with open(outputFile, "w") as text_file:
    text_file.write(job)
