import os
from pytube import YouTube
from pydub import AudioSegment

def download_audio_from_youtube(youtube_url, output_folder):
    # 유튜브 영상 다운로드
    yt = YouTube(youtube_url)
    video_stream = yt.streams.filter(res="720p").first()
    
    if not video_stream:
        print("오디오 스트림을 찾을 수 없습니다.")
        return
    
    downloaded_file = video_stream.download(output_path=output_folder)
    
    # 다운로드된 파일의 확장자를 변경하여 파일명 가져오기
    base, ext = os.path.splitext(downloaded_file)
    new_file = base + '.mp3'
    
    # AudioSegment를 사용하여 mp4를 mp3로 변환
    audio = AudioSegment.from_file(downloaded_file)

    # 오디오의 길이가 원본 영상의 길이와 일치하는지 확인
    video_length = yt.length * 1000  # 비디오 길이를 밀리초로 변환
    audio = audio[:video_length]  # 비디오 길이만큼 오디오를 자름

    # mp3로 내보내기
    audio.export(new_file, format='mp3')
    
    # 원본 파일 삭제 (mp4)
    # os.remove(downloaded_file)
    
    print(f"MP3 파일이 다음 경로에 저장되었습니다: {new_file}")

# 예시 사용법
youtube_url = 'https://www.youtube.com/watch?v=YOUR_VIDEO_ID'

output_folder = './downloads'  # 저장할 폴더 경로
os.makedirs(output_folder, exist_ok=True)
download_audio_from_youtube(youtube_url, output_folder)


