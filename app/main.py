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
        self.quality = params.get('quality', 90)
        self.new_folder = params.get('new_folder', '')
        self.skip_folders = params.get('skip_folders', [])
        self.max_sizes_image = params.get('max_sizes_image', {})
        self.bitrateVideo = params.get('max_bitrate_video', '') #5000k
        self.bitrateAudio = params.get('max_bitrate_audio', '') #192k
        self.max_sizes_video = params.get('max_sizes_video', {})

    def run(self) -> None:
        fm = fileManager.FileManager(self.folder, skip_folders=self.skip_folders)
        files = fm.get_files()
        if not files:
            print('Error: folder is empty')
            return
        
        if self.new_folder:
            fm.create_directory(self.new_folder)

        if 'image' in files:
            imgComp = ImageCompressor.ImageCompressor(files['image'], self.quality, self.new_folder, self.max_sizes_image)
            imgComp.compress_files()
        
        if 'video' in files:
            videoComp = VideoCompressor.VideoCompressor(files['video'], self.new_folder, self.bitrateAudio, self.bitrateVideo, self.max_sizes_video)
            videoComp.run()


def main():
    params = {
        # 'folder': 'C:/Users/tseri/YandexDisk/фото/mi11tt2024/Camera/asia/мыс промтеп',
        'folder': 'C:/Users/tseri/Videos/test',
        'skip_folders': [
            r'done',
        ],
        'quality': 90,
        'new_folder': 'C:/Users/tseri/OneDrive/Documents/temp',
        'max_sizes_image': {
            'width': 1920,
            'height': 1080
        },
        # 'max_bitrate_video': '5000k',
        # 'max_bitrate_audio': '192k',
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