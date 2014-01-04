__author__ = u'schmatz'
from subprocess import call
import os
import sys
#TODO: Upgrade this so it works on windows
#These scripts will be placed in coco/bin
current_directory = os.path.dirname(os.path.realpath(sys.argv[0]))
coco_path = os.getenv("COCO_DIR",os.path.join(current_directory,os.pardir))
nodemon_path = coco_path + os.sep + "node_modules" + os.sep + ".bin" + os.sep + "nodemon"

call(nodemon_path + " . --ext \".coffee|.js\" --watch server --watch app.js --watch server_config.js",shell=True,cwd=coco_path)

