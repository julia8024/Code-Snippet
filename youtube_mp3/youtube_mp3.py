import os
import shutil
from yt_dlp import YoutubeDL
from pydub import AudioSegment

def check_ffmpeg_installed():
    """FFmpeg가 설치되어 있는지 확인하는 함수"""
    if shutil.which("ffmpeg") is None:
        print("⚠ FFmpeg가 설치되지 않았습니다. 'pydub'을 사용하려면 FFmpeg가 필요합니다.")
        print("설치 방법:")
        print(" - Windows: https://ffmpeg.org/download.html 에서 다운로드 후 환경 변수 설정")
        print(" - macOS: brew install ffmpeg (Homebrew 필요)")
        print(" - Linux: sudo apt install ffmpeg 또는 sudo yum install ffmpeg")
        exit(1)

def download_audio(youtube_url, output_folder):
    """유튜브에서 오디오를 다운로드하고 MP3로 변환하는 함수"""

    # FFmpeg 설치 확인
    check_ffmpeg_installed()

    os.makedirs(output_folder, exist_ok=True)

    # yt-dlp 다운로드 옵션 설정
    ydl_opts = {
        'format': 'bestaudio/best',  # 가장 좋은 오디오 품질 선택
        'outtmpl': f"{output_folder}/%(title)s.%(ext)s",  # 파일명 지정
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    # yt-dlp 실행
    with YoutubeDL(ydl_opts) as ydl:
        print("🔽 유튜브 오디오 다운로드 중...")
        info = ydl.extract_info(youtube_url, download=True)
        filename = f"{output_folder}/{info['title']}.mp3"
    
    print(f"✅ MP3 파일이 저장되었습니다: {filename}")

# 예시 사용법
youtube_url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
output_folder = "./downloads"

# 유튜브 오디오 다운로드 및 MP3 변환 실행
download_audio(youtube_url, output_folder)
