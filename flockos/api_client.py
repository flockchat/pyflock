# coding: utf-8

from __future__ import absolute_import
from utils import to_camel_case
import requests
import json
import flockos


def call_api(resource_path, params=None):
    base_url = flockos.base_url
    url = base_url + resource_path
    response_data = requests.post(url, data=str({k:to_camel_case(v) for k,v in params.items()}))
    return json.loads(response_data.text)
