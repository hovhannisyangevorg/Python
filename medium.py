#!/usr/bin/env python3

import os
import shutil

def organizeDirectories(directory):

	dict = {}

	for rootPath, dirsPath, filesPaths in os.walk(directory):

		for name in filesPaths:
			key 		= "for_" + os.path.splitext(name)[1][1:]
			absFilePath = os.path.join(rootPath, name)
			relPath 	= os.path.dirname(os.path.relpath(absFilePath, directory))
			genDirname 	= os.path.join(directory, os.path.join(key, relPath))
			dict[genDirname] = []

	for rootPath, dirsPath, filesPaths in os.walk(directory):
		
		for name in filesPaths:
			key 		= "for_" + os.path.splitext(name)[1][1:]
			absFilePath = os.path.join(rootPath, name)
			relPath 	= os.path.dirname(os.path.relpath(absFilePath, directory))
			genDirname 	= os.path.join(directory, os.path.join(key, relPath))
			dict[genDirname].append(absFilePath)

	for key, pathList in dict.items():
		os.makedirs(key)
		for filePath in pathList:
			if os.access(filePath, os.R_OK):
				shutil.move(filePath, key)
			else:
				raise PermissionError(f"{os.path.basename(name)} Has no read permission")

	for key, pathList in dict.items():
		for filePath in pathList:
			if directory !=  os.path.dirname(filePath):
				shutil.rmtree(os.path.dirname(filePath))
			
def organize(dirPath):

	if os.path.isdir(dirPath):
		organizeDirectories(dirPath)
	else:
		raise FileNotFoundError(f"The directory {dirPath} was not found.")

def main():
    try:
        organize(input("Directory Path: "))
    except FileNotFoundError as err:
        os.write(2, f"{err}\n".encode())
    except PermissionError as err:
        os.write(2, (f"{err}\n").encode())
    except OSError as OSerr:   
        os.write(2, (OSerr.strerror + "\n").encode())

if __name__ == "__main__":
	main()
