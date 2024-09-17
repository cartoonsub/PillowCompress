import re
import os
import sys
import shutil

class FileManager():
    def __init__(self, folder: str, dest: str = ''):
        self.folder = folder
        self.dest = dest
        print('folder:', folder)
        if not self.dest:
            self.dest = self.folder

    def getFiles(self) -> list:
        filesList = []
        if (os.path.isdir(self.folder) == False):
            print('Error: folder is not exist')
            return filesList
        
        os.chdir(self.folder)
        curentDir = os.getcwd()
        for root, dirs, files in os.walk(curentDir):
            if not files:
                continue
            for file in files:
                currentFile = os.path.join(root, file)
                filesList.append(currentFile)

        return filesList

    def createDirectory(self, folder: str):
        if not os.path.exists(folder):
            os.makedirs(folder)
        
        return folder

    def Rename(self, file):
        pass
        # newFile = os.path.join(self.folder, newName)
        # self.names.append(matches['serie'])
        # print('Renamed:', file, 'to', newFile, end='\n\r \n\r')
        # if self.test == True:
        #     return

        # shutil.move(file, newFile)

if __name__ == '__main__':
    pass
