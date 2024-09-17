import fileManager
import Compressor


def main():
    folder = 'C:/Users/tseri/OneDrive/Изображения/3d'
    FM = fileManager.FileManager(folder)
    files = FM.getFiles()
    if not files:
        print('Error: files is empty')
        return
    
    newFolder = ''
    FM.createDirectory(newFolder)
    CM = Compressor.Compressor(files, 90, newFolder)
    CM.compressFiles()
    # создать статистику по сжатию
    # к примеру размер папки до и после сжатия

if __name__ == "__main__":
    main()