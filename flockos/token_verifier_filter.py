import jwt
from utils import send_403_response
import json
from urlparse import parse_qs


class TokenVerifierFilter:
    EVENT_BODY = 'event_body'
    EVENT_TOKEN_PAYLOAD = 'event_token_payload'

    def __init__(self, app, app_secret, app_id):
        self.app = app
        self.app_secret = app_secret
        self.app_id = app_id

    @staticmethod
    def decode_and_verify_request(environ, app_secret, app_id):
        payload, body = TokenVerifierFilter.get_token_and_body(environ, app_secret)
        event = json.loads(body)
        if payload is not None and body is not None and payload.get('appId') == app_id and event.get(
                'userId') == payload.get('userId'):
            environ[TokenVerifierFilter.EVENT_TOKEN_PAYLOAD] = payload
            environ[TokenVerifierFilter.EVENT_BODY] = event

    @staticmethod
    def get_token_and_body(environ, app_secret):
        payload, body = None, None
        if environ['REQUEST_METHOD'] == 'GET':
            query_params = parse_qs(environ['QUERY_STRING'])
            token = query_params.get('flockEventToken')
            body = query_params.get('flockEvent')
        elif environ['REQUEST_METHOD'] == 'POST' and environ['CONTENT_TYPE'].startswith('application/json'):
            token = environ.get('HTTP_X_FLOCK_EVENT_TOKEN')
            request_body_size = int(environ.get('CONTENT_LENGTH', 0))
            body = environ.get('wsgi.input').read(request_body_size).decode("utf-8")
        payload = jwt.decode(token, app_secret, algorithm='HS256')
        return payload, body

    def __call__(self, environ, start_response):
        try:
            TokenVerifierFilter.decode_and_verify_request(environ,
                                                          self.app_secret,
                                                          self.app_id)
            if environ.get(TokenVerifierFilter.EVENT_TOKEN_PAYLOAD) is None:
                send_403_response(start_response)
            else:
                return self.app(environ, start_response)
        except jwt.DecodeError:
            send_403_response(start_response)
