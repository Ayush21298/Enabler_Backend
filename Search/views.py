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

@api_view(['GET'])
def all(request):
	if request.method == 'GET':

		return Response({})

