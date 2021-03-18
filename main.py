from moviepy.editor import *



def convert(mp4_file, mp3_file):
    videoClip = VideoFileClip(mp4_file)
    audioClip = videoClip.audio
    audioClip.write_audiofile(mp3_file)
    audioClip.close()
    videoClip.close()


if __name__ == '__main__':
    convert("Your Video Directory.mp4", "Your Audio Directory.mp3")


