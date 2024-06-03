from django.shortcuts import render
import random
import requests
from .models import Youtube_videos


def Novabase_home(request):
    image_url = {
        "Youtube video": {"image": "youtube_4494485.png", "url": "ytv"},
        "Youtube channel": {"image": "youtube_4494485.png", "url": "None"},

        "instagram post": {"image": "instagram_2111463.png", "url": "None"},
        "instagram id": {"image": "instagram_2111463.png", "url": "None"},

        "facebook post": {"image": "facebook_2496095.png", "url": "None"},
        "facebook id": {"image": "facebook_2496095.png", "url": "None"},

         "linkdin post": {"image": "linkedin_2673871.png", "url": "None"},
         "linkdin id": {"image": "linkedin_2673871.png", "url": "None"},
    }

    context = {
        "image_url": image_url,
    }

    return render(request, 'index.html', context)



def Youtube_videos_page(request):
    videos = Youtube_videos.objects.all()

    random_id = random.choice(videos)

    context = {
        'random_id': random_id,
    }
    return render(request, 'youtube\\youtube_video\\youtube_videos.html', context)


def check_video_availability(video_id):
    url = f"https://www.googleapis.com/youtube/v3/videos?id={
        video_id}&key=AIzaSyDv3zp1x-ip0wi3rXUWsM1-uiA0t-n_RaI&part=status"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("items") and data["items"][0]["status"]["uploadStatus"] == "processed":
            return True  # Video is available
        else:
            return False  # Video is unavailable
    else:
        return False  # Failed to fetch video data


def Upload_youtube_videos(request):
    if request.method == "POST":
        vid = request.POST.get("vid")  # Accessing POST data safely
        if len(vid) == 11 and not Youtube_videos.objects.filter(video_id=vid).exists():
            if check_video_availability(vid):
                # If the video is available, save the video ID
                video = Youtube_videos(video_id=vid)
                video.save()
                return render(request, 'youtube/youtube_video/upload_youtube_video.html', {'message': 'Video ID uploaded successfully!'})
            else:
                return render(request, 'youtube/youtube_video/upload_youtube_video.html', {'message': 'YouTube video is unavailable!'})
        else:
            if len(vid) != 11:
                return render(request, 'youtube/youtube_video/upload_youtube_video.html', {'message': 'Invalid video ID!'})
            else:
                return render(request, 'youtube/youtube_video/upload_youtube_video.html', {'message': 'Video already exists in the database!'})

    return render(request, 'youtube/youtube_video/upload_youtube_video.html')
