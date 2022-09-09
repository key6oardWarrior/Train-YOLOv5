from os import getcwd
from os.path import join
from genericpath import isdir
from sys import argv

'''
argv[1] = percentage of images used for training between 0.0 - 1.0
argv[2] = images path
argv[3] = labels path
'''

class DirNotFoundError(Exception):
	pass

path = getcwd()

def createDirs() -> None:
	from os import mkdir

	global path
	path = join(path, "train_val_split")
	cnt = 1

	while isdir(path):
		path = path[:-1] + str(cnt)
		cnt += 1

	mkdir(path)

	imagesPath: str = join(path, "images")
	labelsPath: str = join(path, "labels")

	mkdir(imagesPath)
	mkdir(labelsPath)

	mkdir(join(imagesPath, "train"))
	mkdir(join(imagesPath, "val"))

	mkdir(join(labelsPath, "train"))
	mkdir(join(labelsPath, "val"))

def trainValSplit() -> None:
	from os import listdir
	from shutil import copy2

	trainingSize: float

	if argv[1].replace(".", "").isnumeric():
		trainingSize = float(argv[1])
	else:
		raise ValueError("argv[1] must be a float between 0.0 and 1.0")

	if((trainingSize > 1.0) or (trainingSize < 0.0)):
		raise ValueError("argv[1] must be a float between 0.0 and 1.0")

	images: list = listdir(argv[2])
	trainingSize: int = round(len(images) * trainingSize)

	if (isdir(argv[2]) == False):
		raise DirNotFoundError(f"The directory {argv[2]} does not exists")

	cnt = 0
	for file in images:
		if cnt < trainingSize:
			copy2(join(argv[2], file), join(path, join("images", "train")))
		else:
			copy2(join(argv[2], file), join(path, join("images", "val")))

		cnt += 1

	if (isdir(argv[3]) == False):
		raise DirNotFoundError(f"The directory {argv[3]} does not exists")

	cnt = 0
	for file in listdir(argv[3]):
		if cnt < trainingSize:
			copy2(join(argv[3], file), join(path, join("labels", "train")))
		else:
			copy2(join(argv[3], file), join(path, join("labels", "val")))

		cnt += 1

if __name__ == "__main__":
	ARGS_SIZE = 4
	SIZE = len(argv)

	if SIZE != ARGS_SIZE:
		raise ValueError(f"Expected {ARGS_SIZE}, but got {SIZE}")

	createDirs()
	trainValSplit()
