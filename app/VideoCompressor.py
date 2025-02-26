import os
import subprocess
import json

from globals import check_gui_controls
from logsBridge import set_logs


class VideoCompressor:
    """
    A class to compress video files using ffmpeg.
    """

    def __init__(
            self, files: list,
            dest: str = '',
            bitrate_audio: str = '',
            bitrate_video: int = 0,
            max_sizes: dict = None
    ) -> None:
        self.ffmpeg = 'C:/ffmpeg/bin/ffmpeg.exe'
        self.extensions = (
            'mp4', 'mkv', 'avi', 'flv', 'mov', 'wmv', 'mpg', 'mpeg', 'm4v',
            '3gp', '3g2', 'm2ts', 'mts', 'ts', 'webm'
        )
        self.files = files
        self.dest = dest
        self.bitrate_audio = bitrate_audio
        self.bitrate_video = bitrate_video
        self.max_sizes = max_sizes if max_sizes else {}

    def run(self) -> None:
        self.filter_files()
        if not self.files:
            print('After filtering: files is empty')
            set_logs('error', 'After filtering video: files is empty')
            return
        self.compress_files()

    def filter_files(self) -> None:
        for index, file in enumerate(self.files):
            file = str(file)
            if not file.lower().endswith(self.extensions):
                continue

            info = self.get_video_info(file)
            if not info:
                print('Error: info is empty')
                set_logs('error', 'Error: info is empty for ' + file)
                continue

            format = info.get('format', {})
            if not format:
                print('Error: format is empty')
                set_logs('error', 'Error: format is empty for ' + file)
                continue

            flag = False
            format_name = format.get('format_name', '')
            formats = format_name.split(',')
            for fmt in formats:
                if fmt in self.extensions:
                    flag = True
                    break

            if not flag:
                print('Error: format is not supported', file)
                set_logs('error', 'Error: format is not supported ' + file)
                self.files.pop(index)

    def get_video_info(self, file: str) -> dict:
        cmd = 'ffprobe'
        args = [cmd, '-show_format', '-show_streams', '-of', 'json', file]

        popen = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = popen.communicate()
        if popen.returncode != 0:
            set_logs('error', f'Error running ffprobe on {file}: {err.decode("utf-8")}')
            raise Exception(f'Error running ffprobe on {file}: {err.decode("utf-8")}')

        return json.loads(out.decode('utf-8'))

    def compress_files(self) -> None:
        for file in self.files:
            if not check_gui_controls():
                return

            set_logs('processing', 'Compressing: ' + file)
            print('Compressing:', file)

            info = self.get_video_info(file)
            bitrate = self.get_video_bitrate(info)
            bitrate = str(bitrate) + 'k'

            bitrate_audio = self.get_audio_bitrate(info)
            bitrate_audio = str(bitrate_audio) + 'k'
            file_name = os.path.basename(file)
            file_size = os.path.getsize(file) / (1024 * 1024)
            if self.dest:
                new_file = os.path.join(self.dest, file_name)
            else:
                new_file = file

            path = '"' + file + '"'
            start_query = self.ffmpeg + ' -y -i ' + path

            codec = 'libx264'
            query = start_query + ' -c:v ' + codec + ' -b:v ' + bitrate + ' -pass 1 -f mp4 NULL'
            process = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode != 0:
                set_logs('error', f'Error during first pass: {stderr.decode()} for {file}')
                print(f'Error during first pass: {stderr.decode()}')
                return

            if not os.path.exists('NULL'):
                self.remove_garbage()
                print('Error: NULL file is not created')
                set_logs('error', 'Error: NULL file is not created for ' + file)
                return

            out_name = '"' + new_file + '"'
            query = start_query + ' -map 0:0'
            query += ' -c:v libx264 -b:v ' + bitrate + ' -pass 2 -c:a aac -b:a ' + bitrate_audio + ' -f mp4 -movflags +faststart -vsync 1 -async 1 ' + out_name

            process = subprocess.Popen(query, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode != 0:
                print(f'Error during second pass: {stderr.decode()}')
                set_logs('error', f'Error during second pass: {stderr.decode()} for {file}')
                return

            if not os.path.exists(new_file):
                print('Error: compressed file is not created')
                set_logs('error', 'Error: compressed file is not created for ' + file)
                self.remove_garbage()
                return

            new_file_size = os.path.getsize(new_file) / (1024 * 1024)
            print(f'Compressed: {file_name} size: {file_size:.2f} MB -> {new_file_size:.2f} MB')
            set_logs('done', f'Compressed: {file_name} size: {file_size:.2f} MB -> {new_file_size:.2f} MB')

            self.remove_garbage()

    def get_video_bitrate(self, info: dict) -> int:
        bitrate = 0
        if not info:
            return self.bitrate_video

        streams = info.get('streams', [])
        for stream in streams:
            if stream.get('codec_type', '') == 'video':
                bitrate = int(stream.get('bit_rate', 0))
                bitrate = int(bitrate / 1000)
                break

        if self.bitrate_video < bitrate:
            bitrate = self.bitrate_video

        return bitrate

    def get_audio_bitrate(self, info: dict) -> int:
        bitrate = 0
        if not info:
            return bitrate

        streams = info.get('streams', [])
        for stream in streams:
            if stream.get('codec_type', '') == 'audio':
                bitrate = int(stream.get('bit_rate', 0))
                bitrate = int(bitrate / 1000)
                break

        return bitrate

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

    def remove_garbage(self) -> None:
        if os.path.exists('NULL'):
            os.remove('NULL')

        files = os.listdir('.')
        for file in files:
            if file.endswith('.log'):
                os.remove(file)

            if file.endswith('.mbtree'):
                os.remove(file)

            if file.endswith('.temp'):
                os.remove(file)


if __name__ == '__main__':
    pass