from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_upload_path_video(instance, filename):
	return 'static/video/{0}/{1}'.format(instance.timestamp, filename)

@csrf_exempt
def get_upload_path_image(instance, filename):
	return 'static/image/{0}/{1}'.format(instance.timestamp, filename)
