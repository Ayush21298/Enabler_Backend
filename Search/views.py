from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse
from django.urls import reverse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from rest_framework import status
from rest_framework.decorators import api_view, parser_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser

import json
import requests
import datetime
import base64
import hashlib

from serializers import *
from utils import *

from urllib.parse import unquote

CLIENT_ID = "mqvXuOXfn3YUjqZNdpPp5zyQXcUnA1GtG8e16zqG"
CLIENT_SECRET = "7QQfo5YIOPTmUwOtbSeiyrg9UpxYlt4M8Wv1qccxPQRwh947xdFtW2oaI7BavLDRfD1ItEE6FgPa8xQ5sZM6iC9nBl4KwjuuUXTfxZSFwJvRo2g39WZOp7ZCMkxC9hGw"
AUTHORIZATION_HEADER = "Basic bXF2WHVPWGZuM1lVanFaTmRwUHA1enlRWGNVbkExR3RHOGUxNnpxRzo3UVFmbzVZSU9QVG1Vd090YlNlaXlyZzlVcHhZbHQ0TThXdjFxY2N4UFFSd2g5NDd4ZEZ0VzJvYUk3QmF2TERSZkQxSXRFRTZGZ1BhOHhRNXNaTTZpQzluQmw0S3dqdXVVWFRmeFpTRndKdlJvMmczOVdaT3A3WkNNa3hDOWhHdw=="

BASE_URL = "https://www.udemy.com"

# https://www.udemy.com/developers/affiliate/methods/get-courses-list/

@api_view(['GET'])
def udemy(request):
	# http://127.0.0.1:8000/search/udemy/?search=introduction%20to%20computer%20science
	# http://127.0.0.1:8000/search/udemy/?search=introduction to computer science
	if request.method == 'GET':

		URL = BASE_URL + "/api-2.0/courses/"

		headers = {}
		headers["Accept"] = "application/json, text/plain, */*"
		headers["Authorization"] = "Basic bXF2WHVPWGZuM1lVanFaTmRwUHA1enlRWGNVbkExR3RHOGUxNnpxRzo3UVFmbzVZSU9QVG1Vd090YlNlaXlyZzlVcHhZbHQ0TThXdjFxY2N4UFFSd2g5NDd4ZEZ0VzJvYUk3QmF2TERSZkQxSXRFRTZGZ1BhOHhRNXNaTTZpQzluQmw0S3dqdXVVWFRmeFpTRndKdlJvMmczOVdaT3A3WkNNa3hDOWhHdw=="
		headers["Content-Type"] = "application/json;charset=utf-8"

		params = {}
		params["price"] = "price-free"
		params["ordering"] = "highest-rated"
		params["search"] = request.GET["search"]
		print(request.GET)

		r=requests.get(URL, headers=headers, params=params)
		print(r.url)

		return Response(json.loads(r.content))

@api_view(['GET'])
def coursera(request):
	# http://127.0.0.1:8000/search/udemy/?search=introduction%20to%20computer%20science
	# http://127.0.0.1:8000/search/udemy/?search=introduction to computer science
	if request.method == 'GET':

		URL = "https://api.coursera.org/api/courses.v1"

		params = {
					'q': 'search',
					'query': request.GET["search"],
					'start': 0,
					'limit': 10,
					'fields': ','.join(['name', 'description', 'partnerIds', 
								'slug', 'primaryLanguages', 'domainTypes', 'photoUrl']),
             }
		print(request.GET)

		r=requests.get(URL, params=params)
		print(r.url)

		return Response(json.loads(r.content))

@api_view(['GET'])
def edx(request):
	# http://127.0.0.1:8000/search/udemy/?search=introduction%20to%20computer%20science
	# http://127.0.0.1:8000/search/udemy/?search=introduction to computer science
	if request.method == 'GET':

		URL = "https://www.edx.org/api/v1/catalog/search"

		params = {'selected_facets[]': 'transcript_languages_exact:English',
				'query': request.GET["search"],
				'partner': 'edx',
				'content_type[]': 'courserun',
				'page': 1,
				'page_size': 10}

		print(request.GET)

		r=requests.get(URL, params=params)
		print(r.url)

		return Response(json.loads(r.content))

@api_view(['GET'])
def coursera_old(request):
	# http://127.0.0.1:8000/search/udemy/?search=introduction%20to%20computer%20science
	# http://127.0.0.1:8000/search/udemy/?search=introduction to computer science
	if request.method == 'GET':

		URL = "dump/coursera.dump"

		search = request.GET["search"]

		with open(URL, 'r') as f:
			lines = f.readlines()
			temp = json.loads(lines[0])
			print(len(temp))
			# print(json.loads(lines[0]))

			return Response(temp[:10])

@api_view(['GET'])
def edx_old(request):
	# http://127.0.0.1:8000/search/udemy/?search=introduction%20to%20computer%20science
	# http://127.0.0.1:8000/search/udemy/?search=introduction to computer science
	if request.method == 'GET':

		URL = "dump/edx.dump"

		search = request.GET["search"]

		with open(URL, 'r') as f:
			lines = f.readlines()
			temp = json.loads(lines[0])
			print(len(temp))
			# print(json.loads(lines[0]))

			return Response(temp[:10])

