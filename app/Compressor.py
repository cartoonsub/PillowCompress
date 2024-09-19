from PIL import Image
import os


class Compressor:
    def __init__(self, files: list, quality: int = 100, dest: str = ''):
        self.files = files
        self.quality = quality
        self.dest = dest

    def compress_files(self):
        for file in self.files:
            try:
                img = Image.open(file)

                file_name = os.path.basename(file)
                file_size = os.path.getsize(file) / (1024 * 1024)

                if self.dest:
                    new_file = os.path.join(self.dest, file_name)
                else:
                    new_file = file

                img.save(new_file, optimize=True, quality=self.quality)

                new_file_size = os.path.getsize(new_file) / (1024 * 1024)
                print(f'Compressed: {file_name} size: {file_size:.2f} MB -> {new_file_size:.2f} MB')
            except Exception as e:
                print(f'Error: {e}')
                continue


if __name__ == '__main__':
    pass
