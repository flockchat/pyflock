# coding: utf-8


# python 2 and python 3 compatibility library
from six import iteritems
from ..api_client import call_api


def fetch_messages(token, chat, uids, **kwargs):
    """
    
    
    This method makes a synchronous HTTP request.
    :param str token:  (required)
    :param str chat:  (required)
    :param list[str] uids:  (required)
    :return: response dict
    """

    params = locals()
    for key, val in iteritems(params['kwargs']):
        params[key] = val
    del params['kwargs']
    resource_path = '/chat.fetchMessages'.replace('{format}', 'json')
    response = call_api(resource_path, params=params)
    return response


def send_message(token, to, text, **kwargs):
    """
    
    
    This method makes a synchronous HTTP request.
    :param str token:  (required)
    :param str to:  (required)
    :param str text:  (required)
    :param str flockml: 
    :param str notification: 
    :param list[str] mentions: 
    :param SendAs send_as: 
    :param list[Attachment] attachments: 
    :return: response dict
    """

    params = locals()
    for key, val in iteritems(params['kwargs']):
        params[key] = val
    del params['kwargs']
    resource_path = '/chat.sendMessage'.replace('{format}', 'json')
    response = call_api(resource_path, params=params)
    return response

