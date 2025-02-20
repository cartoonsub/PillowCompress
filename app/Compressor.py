import fileManager
import ImageCompressor
import VideoCompressor


class Compressor:
    def __init__(self, params: dict) -> None:
        if not params:
            raise ValueError('Error: params is empty')
        
        if 'folder' not in params:
            raise ValueError('Error: folder is required')

        self.folder = params['folder']
        self.skip_folders = params.get('skip_folders', [])
        self.new_folder = params.get('new_folder', '')
        
        img_params = params.get('img_params', {})
        self.quality = img_params.get('quality', 90)
        self.max_sizes_image = {
            'width': img_params.get('maxwidth', 1920),
            'height': img_params.get('maxheight', 1080)
        }
        
        video_params = params.get('video_params', {})
        self.bitrateVideo = video_params.get('bitrate', 5000)
        self.bitrateAudio = video_params.get('audio_bitrate', 192)
        self.max_sizes_video = {
            'width': video_params.get('maxwidth', 1920),
            'height': video_params.get('maxheight', 1080)
        }

    def run(self) -> bool:
        fm = fileManager.FileManager(self.folder, skip_folders=self.skip_folders)
        files = fm.get_files()
        if not files:
            print('Error: folder is empty')
            return False
        
        if self.new_folder:
            fm.create_directory(self.new_folder)

        if 'image' in files:
            imgComp = ImageCompressor.ImageCompressor(files['image'], self.quality, self.new_folder, self.max_sizes_image)
            imgComp.compress_files()
        
        if 'video' in files:
            videoComp = VideoCompressor.VideoCompressor(files['video'], self.new_folder, self.bitrateAudio, self.bitrateVideo, self.max_sizes_video)
            videoComp.run()

        print('Compression is done')
        return True


def main():
    params = {
        'folder': 'C:/Users/tseri/YandexDisk/фото/mi11tt2024/Camera/asia/море пхукет',
        # 'folder': 'C:/Users/tseri/Videos/test',
        'skip_folders': [
            r'done',
        ],
        'quality': 90,
        'new_folder': 'C:/Users/tseri/YandexDisk/фото/mi11tt2024/Camera/asia/море пхукет/converted',
        'max_sizes_image': {
            'width': 1920,
            'height': 1080
        },
        'max_bitrate_video': 5000,
        # 'max_bitrate_audio': '192',
        # 'max_sizes_video': {
        #     'width': 1920,
        #     'height': 1080
        # }
    }

    Compressor(params).run()

    # создать статистику по сжатию
    # к примеру размер папки до и после сжатия


if __name__ == "__main__":
    main()