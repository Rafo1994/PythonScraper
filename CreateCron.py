import os
import sys

dirPath = os.path.dirname(os.path.realpath(__file__))
outputFile = "/etc/cron.d/crontab"
shellName = "cron-script.sh"

job = "* * * * * /bin/sh /app/" + shellName + "\n"

with open(outputFile, "w") as text_file:
    text_file.write(job)

cronScript = "#!/bin/bash\n" + sys.executable + " " + dirPath + "/App.py\n"

with open("/app/" + shellName, "w") as text_file:
    text_file.write(cronScript)
