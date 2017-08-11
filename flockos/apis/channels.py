# coding: utf-8



# python 2 and python 3 compatibility library
from six import iteritems
from ..api_client import call_api


def get_info(token, channel_id, **kwargs):
    """


    This method makes a synchronous HTTP request.
    :param str token:  (required)
    :param str channel_id:  (required)
    :return: response dict
    """

    params = locals()
    for key, val in iteritems(params['kwargs']):
        params[key] = val
    del params['kwargs']
    resource_path = '/channels.getInfo'.replace('{format}', 'json')
    response = call_api(resource_path, params=params)
    return response


def get_members(token, channel_id, show_public_profile, **kwargs):
    """


    This method makes a synchronous HTTP request.
    :param str token:  (required)
    :param str channel_id:  (required)
    :param bool show_public_profile:  (required)
    :return: response dict
    """

    params = locals()
    for key, val in iteritems(params['kwargs']):
        params[key] = val
    del params['kwargs']
    resource_path = '/channels.getMembers'.replace('{format}', 'json')
    response = call_api(resource_path, params=params)
    return response


def list(token, **kwargs):
    """


    This method makes a synchronous HTTP request.
    :param str token:  (required)
    :return: response dict
    """

    params = locals()
    for key, val in iteritems(params['kwargs']):
        params[key] = val
    del params['kwargs']
    resource_path = '/channels.list'.replace('{format}', 'json')
    response = call_api(resource_path, params=params)
    return response
