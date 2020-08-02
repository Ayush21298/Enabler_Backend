from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_upload_path_video(instance, filename):
	return 'video/{0}/{1}/{2}/{3}'.format(instance.timestamp, instance.username, instance.title, filename)
