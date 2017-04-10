# coding: utf-8

from __future__ import absolute_import
import requests
import json
import flockos


def call_api(resource_path, params=None):
    base_url = flockos.base_url
    url = base_url + resource_path
    response_data = requests.post(url, data=str(params))
    return json.loads(response_data.text)
