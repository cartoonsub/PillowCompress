import fileManager
import Compressor


def main():
    folder = 'C:/Users/tseri/OneDrive/Изображения/3d'
    fm = fileManager.FileManager(folder)
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