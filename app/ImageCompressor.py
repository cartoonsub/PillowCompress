from globals import check_gui_controls
from PIL import Image
import os
import time
from logsBridge import set_logs


class ImageCompressor:
    def __init__(
            self, files: list,
            quality: int = 100,
            dest: str = '',
            max_sizes: dict = {}
    ) -> None:
        self.files = files
        self.quality = quality
        self.dest = dest
        self.max_sizes = max_sizes

    def compress_files(self):
        for file in self.files:
            if not check_gui_controls():
                return

            try:
                img = Image.open(file)
                
                if self.max_sizes:
                    width, height = img.size
                    if not width or not height:
                        print(f'Error: size is empty {file}')
                        set_logs('error', f'size is empty {file}')
                        continue

                    newWidth, newHeight = self.get_new_size(width, height)
                    img = img.resize((newWidth, newHeight))

                file_name = os.path.basename(file)
                file_size = os.path.getsize(file) / (1024 * 1024)

                if self.dest:
                    new_file = os.path.join(self.dest, file_name)
                else:
                    new_file = file

                img.save(new_file, optimize=True, quality=self.quality)

                new_file_size = os.path.getsize(new_file) / (1024 * 1024)
                print(f'Compressed: {file_name} size: {file_size:.2f} MB -> {new_file_size:.2f} MB quality: {self.quality}')
                set_logs('done', f'Compressed: {file_name} size: {file_size:.2f} MB -> {new_file_size:.2f} MB quality: {self.quality}')
            except Exception as e:
                print(f'Error: {e}')
                continue

    def get_new_size(self, width: int, height: int) -> tuple:
        max_width = self.max_sizes.get('width', 1920)
        max_height = self.max_sizes.get('height', 1080)

        if (
            (width <= max_width and height <= max_height) or
            (width <= max_height and height <= max_width)
        ):
            return width, height

        new_width = width
        new_height = height

        reverse = False
        if width < height:
            reverse = True
            width, height = height, width

        aspect_ratio = width / height

        if (width / max_width) > (height / max_height):
            new_width = max_width
            new_height = int(max_width / aspect_ratio)
        else:
            new_height = max_height
            new_width = int(max_height * aspect_ratio)

        if reverse:
            new_width, new_height = new_height, new_width

        return new_width, new_height


if __name__ == '__main__':
    pass
