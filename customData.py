from os import remove
from sys import argv
from os.path import exists
from genericpath import isdir

'''
argv[1] = path to classes file
argv[2] = path to train validation split
'''

class DirNotFoundError(Exception):
	pass

SIZE = len(argv)
if SIZE != 3:
	raise ValueError(f"Expected 3 command line arguments, but got {SIZE}")

if exists(argv[1]) == False:
	raise FileNotFoundError(f"File {argv[1]} not found")

if isdir(argv[2]) == False:
	raise DirNotFoundError(f"The directory {argv[2]} does not exists")

if exists("yolov5\\data\\coco128.yaml"):
	remove("yolov5\\data\\coco128.yaml")

coco128_yaml = """train: [DIR]\\images\\train
val: [DIR]\\images\\val

nc: [VALUE]
names: ["""

cnt = 0
for ii in open(argv[1]).readlines():
	coco128_yaml += f"'{ii[:-1]}', "
	cnt += 1

coco128_yaml = coco128_yaml[:-2] + "]"
coco128_yaml = coco128_yaml.replace("[VALUE]", str(cnt))
coco128_yaml = coco128_yaml.replace("[DIR]", argv[2])
open("yolov5\\data\\coco128.yaml", "w").write(coco128_yaml)