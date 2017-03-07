import jwt
from utils import send_403_response


class TokenVerifierFilter:
    def __init__(self, app, app_secret, appId):
        self.app = app
        self.app_secret = app_secret
        self.appId = appId

    @staticmethod
    def decode_and_verify_request(environ, app_secret, appId):
        payload = jwt.decode(environ['HTTP_X_FLOCK_EVENT_TOKEN'], app_secret, algorithm='HS256')
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
        body = environ['wsgi.input'].read(request_body_size).decode("utf-8")
        if payload['appId'] == appId:
            environ['event_token_payload'] = payload
            environ['request_body'] = body
            return payload, body
        else:
            return None, None

    def __call__(self, environ, start_response):
        try:
            (event_token_payload, request_body) = TokenVerifierFilter.decode_and_verify_request(environ,
                                                                                                self.app_secret,
                                                                                                self.appId)
            if event_token_payload is None or request_body is None:
                send_403_response(start_response)
            else:
                return self.app(environ, start_response)
        except jwt.DecodeError:
            send_403_response(start_response)
