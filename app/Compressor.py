from PIL import Image
import os


class Compressor():
    def __init__(self, files: list, quality: int=100, dest: str=''):
        self.files = files
        self.quality = quality
        self.dest = dest

    def compressFiles(self):
        for file in self.files:
            try:
                Img = Image.open(file)

                fileName = os.path.basename(file)
                fileSize = os.path.getsize(file) / (1024 * 1024)
                # print('Compressing:', fileName, 'size:', fileSize)
                
                if self.dest:
                    newFile = os.path.join(self.dest, fileName)
                else:
                    newFile = file

                Img.save(newFile, optimize=True, quality=self.quality)

                newFileSize = os.path.getsize(newFile) / (1024 * 1024)
                print('Compressed:', fileName, 'size:', fileSize, '->', newFileSize)

            except Exception as e:
                print('Error:', e)
                continue


if __name__ == '__main__':
    pass
