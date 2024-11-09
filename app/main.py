import fileManager
import Compressor as ImageCompressor
import pprint as pp


class Compressor:
    def __init__(self, params: dict) -> None:
        #  folder : str, new_folder : str = '', skip_folders : list = [], quality : int = 90
        if not params:
            raise ValueError('Error: params is empty')
        
        if 'folder' not in params:
            raise ValueError('Error: folder is required')
        
        self.folder = params['folder']
        self.quality = params.get('quality', 90)
        self.new_folder = params.get('new_folder', '')
        self.skip_folders = params.get('skip_folders', [])
        self.max_sizes = params.get('max_sizes', {})

    def run(self) -> None:
        fm = fileManager.FileManager(self.folder, skip_folders=self.skip_folders)
        files = fm.get_files()
        if not files:
            print('Error: folder is empty')
            return
        
        if self.new_folder:
            fm.create_directory(self.new_folder)

        cm = ImageCompressor.Compressor(files, self.quality, self.new_folder)
        cm.compress_files()


def main():
    params = {
        'folder': 'C:/Users/tseri/YandexDisk/фото/mi11tt2024/Camera/asia/DONE/острова PhiPhi/noneed',
        
        'skip_folders': [
            r'done',
        ],
        'quality': 90,
        # 'new_folder': 'C:/Users/tseri/OneDrive/Documents/temp',
        # 'max_sizes': {
        #     'width': 1920,
        #     'height': 1080
        # }
    }

    Compressor(params).run()

    # создать статистику по сжатию
    # к примеру размер папки до и после сжатия


if __name__ == "__main__":
    main()