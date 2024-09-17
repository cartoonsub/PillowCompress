import fileManager
import Compressor


def main():
    FM = fileManager.FileManager('C:/Users/tseri/YandexDisk/фото/mi11tt2024/Camera/volgograd')
    files = FM.getFiles()
    if not files:
        print('Error: files is empty')
        return
    
    newFolder = 'C:/Users/tseri/YandexDisk/фото/mi11tt2024/Camera/volgograd/compressed'
    FM.createDirectory(newFolder)
    CM = Compressor.Compressor(files, 90, newFolder)
    CM.compressFiles()
    # создать статистику по сжатию
    # к примеру размер папки до и после сжатия

if __name__ == "__main__":
    main()