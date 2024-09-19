import fileManager
import Compressor
import pprint as pp


def main():
    folder = 'C:/Users/tseri/YandexDisk/фото/mi11tt2024/Camera/asia/DONE'
    skip_folders = [
        r'done',
    ]
    fm = fileManager.FileManager(folder, skip_folders=skip_folders)
    files = fm.get_files()
    if not files:
        print('Error: files is empty')
        return
    
    new_folder = ''
    fm.create_directory(new_folder)
    cm = Compressor.Compressor(files, 90, new_folder)
    cm.compress_files()

    # создать статистику по сжатию
    # к примеру размер папки до и после сжатия


if __name__ == "__main__":
    main()