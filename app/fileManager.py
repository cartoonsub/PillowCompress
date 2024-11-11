import os
import re
import re
import mimetypes

class FileManager:
    def __init__(self, folder: str, dest: str = '', skip_folders: list = []):
        self.folder = folder
        self.dest = dest
        self.skip_folders = skip_folders
        print('folder:', folder)
        if not self.dest:
            self.dest = self.folder

        self.image_types = [
            'image/jpeg',
            'image/png',
            'image/webp',
        ]

        self.video_types = [
            'video/mp4',
            'video/quicktime',
            'video/mpeg',
        ]

    def get_files(self) -> dict:
        files_list = {}
        if not os.path.isdir(self.folder):
            print('Error: folder does not exist')
            return files_list

        os.chdir(self.folder)
        current_dir = os.getcwd()
        for root, dirs, files in os.walk(current_dir):
            if not self.is_allowed_folder(root):
                print('Skip:', root)
                continue

            if not files:
                continue
            for file in files:
                current_file = os.path.join(root, file)
                file_type = self.get_file_type(current_file)
                if file_type in files_list:
                    files_list[file_type].append(current_file)
                else:
                    files_list[file_type] = [current_file]

        return files_list
    
    def is_allowed_folder(self, folder: str) -> bool:
        result = True
        folderName = os.path.basename(folder)
        for skip_folder in self.skip_folders:
            if re.search(skip_folder, folderName, re.IGNORECASE):
                print('Skip:', folder)
                result = False
                break
                
        return result

    def get_file_type(self, file: str) -> str:
        if not os.path.isfile(file):
            return ''

        mime_type, encoding = mimetypes.guess_type(file)
        if mime_type in self.image_types:
            file_type = 'image'
        elif mime_type in self.video_types:
            file_type = 'video'
        else:
            file_type = 'other'

        return file_type

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
