from django.core import serializers
from django.http import JsonResponse
from django.forms.models import model_to_dict

import json

from api.models import Manifest, Transporter


def manifest(request, manifest_id=None):
    manifest = Manifest.objects.get(id=manifest_id)
    return JsonResponse(manifest.as_json())
