import sys
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
output_file = "cron-job"
job = "0 * * * * " + sys.executable + " " + dir_path + "/" + output_file + "2>&1\r\n"

with open(output_file, "w") as text_file:
    text_file.write(job)