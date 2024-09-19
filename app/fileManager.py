import os
import re
import shutil
import sys
import pprint as pp


class FileManager:
    def __init__(self, folder: str, dest: str = ''):
        self.folder = folder
        self.dest = dest
        print('folder:', folder)
        if not self.dest:
            self.dest = self.folder

    def get_files(self) -> list:
        files_list = []
        if not os.path.isdir(self.folder):
            print('Error: folder does not exist')
            return files_list

        os.chdir(self.folder)
        current_dir = os.getcwd()
        for root, dirs, files in os.walk(current_dir):
            if not files:
                continue
            for file in files:
                current_file = os.path.join(root, file)
                files_list.append(current_file)

        pp.pprint(files_list)
        return files_list

    def create_directory(self, folder: str):
        if not folder:
            print('Error: folder name is empty')
            return
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f'Directory {folder} created')
        else:
            print(f'Directory {folder} already exists')


if __name__ == '__main__':
    pass