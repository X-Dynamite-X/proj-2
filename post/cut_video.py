from moviepy.editor import VideoFileClip

def get_video_duration(video_file):
    # استخدم MoviePy للحصول على مدة الفيديو
    clip = VideoFileClip(video_file.temporary_file_path())
    duration = clip.duration
    clip.close()
    return duration

def trim_video(video_file, start_time, end_time):
    # استخدم MoviePy لقص الفيديو بين الأوقات المحددة
    clip = VideoFileClip(video_file.temporary_file_path()).subclip(start_time, end_time)
    trimmed_video_file = clip.write_videofile(video_file.temporary_file_path(), codec="libx264")
    clip.close()
    return trimmed_video_file


def get_media_type(file):
    # احتسب نوع الملف (فيديو أو صورة) استنادًا إلى امتداد الملف
    file_extension = file.name.split('.')[-1].lower()
    if file_extension in ['mp4', 'avi', 'mov', 'mkv']:
        return 'video'
    elif file_extension in ['jpg', 'jpeg', 'png', 'gif']:
        return 'image'
    else:
        return 'unknown'

