__author__ = u'schmatz'
from subprocess import call
import subprocess
import os
import time
import sys
#TODO: Upgrade this so it works on windows
#These scripts will be placed in coco/bin
current_directory = os.path.dirname(os.path.realpath(sys.argv[0]))
coco_path = os.getenv("COCO_DIR",os.path.join(current_directory,os.pardir))
brunch_path = coco_path + os.sep + "node_modules" + os.sep + ".bin" + os.sep + "brunch"
subprocess.Popen("ulimit -n 10000",shell=True)
while True:
    call(brunch_path + " w --config " + coco_path + os.sep + "brunch.coffee",shell=True,cwd=coco_path)
    print("Brunch crashed. Press control+C within 1 second to quit.")
    time.sleep(1)