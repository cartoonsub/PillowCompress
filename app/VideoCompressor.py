import os
import subprocess
import json


class VideoCompressor:
    def __init__(
            self, files: list,
            dest: str = '',
            bitrateAudio: str = '',
            bitrateVideo: str = ''
    ) -> None:
        self.extensions = ('mp4', 'mkv', 'avi', 'flv', 'mov', 'wmv', 'mpg', 'mpeg', 'm4v', '3gp', '3g2', 'm2ts', 'mts', 'ts', 'webm')
        self.files = files
        self.dest = dest
        self.bitrateAudio = bitrateAudio
        self.bitrateVideo = bitrateVideo

    def run(self) -> None:
        self.filter_files()

    def compress_files(self):
        for file in self.files:
            try:
                img = Image.open(file)
                
                if self.max_sizes:
                    width, height = img.size
                    if not width or not height:
                        print(f'Error: size is empty {file}')
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
                print(f'Compressed: {file_name} size: {file_size:.2f} MB -> {new_file_size:.2f} MB')
            except Exception as e:
                print(f'Error: {e}')
                continue

    def filter_files(self) -> None:
        for file in self.files:
            file = str(file)
            if not file.lower().endswith(self.extensions):
                continue
            
            info = self.get_video_info(file)
            print('Compress:', file)
            # print('info:', info)

    def get_video_info(self, file: str) -> dict:
        cmd = 'ffprobe'
        args = [cmd, '-show_format', '-show_streams', '-of', 'json', file]

        print('args:', args)
        p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p.communicate()
        if p.returncode != 0:
            raise Exception(f'Error running ffprobe on {file}: {err.decode("utf-8")}')

        # print(out.decode('utf-8'))
        return json.loads(out.decode('utf-8'))

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
