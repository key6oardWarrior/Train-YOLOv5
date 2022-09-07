from os import system
from sys import platform

system("git clone https://github.com/ultralytics/yolov5")

if platform == "win32":
	system("py -m pip install -r yolov5/requirements.txt")
else:
	system("python -m pip install -r yolov5/requirements.txt")