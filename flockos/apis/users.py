# coding: utf-8


# python 2 and python 3 compatibility library
from six import iteritems
from ..api_client import call_api


def get_info(token, **kwargs):
    """
    
    
    This method makes a synchronous HTTP request.
    :param str token:  (required)
    :return: response dict
    """

    params = locals()
    for key, val in iteritems(params['kwargs']):
        params[key] = val
    del params['kwargs']
    resource_path = '/users.getInfo'.replace('{format}', 'json')
    response = call_api(resource_path, params=params)
    return response

