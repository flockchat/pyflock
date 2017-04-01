import json
import jwt
from token_verifier_filter import TokenVerifierFilter
from utils import send_200_response, send_403_response, send_404_response


class Event(object):
    def __init__(self, dictionary):
        self.__dict__ = json.loads(dictionary)


class EventHandlerClient(object):
    def __init__(self, app_secret, app_id):
        self.app_secret = app_secret
        self.app_id = app_id
        self.on_app_install_handler = None
        self.on_app_uninstall_handler = None
        self.on_chat_generate_url_preview_handler = None
        self.on_chat_receive_message_handler = None
        self.on_client_flockml_action_handler = None
        self.on_client_open_attachment_widget_handler = None
        self.on_client_message_action_handler = None
        self.on_client_press_button_handler = None
        self.on_client_slash_command_handler = None
        self.on_client_widget_action_handler = None

    def on_app_install(self, f):
        self.on_app_install_handler = f

    def on_app_uninstall(self, f):
        self.on_app_uninstall_handler = f

    def on_chat_generate_url_preview(self, f):
        self.on_chat_generate_url_preview_handler = f

    def on_chat_receive_message(self, f):
        self.on_chat_receive_message_handler = f

    def on_client_flockml_action(self, f):
        self.on_client_flockml_action_handler = f

    def on_client_open_attachment_widget(self, f):
        self.on_client_open_attachment_widget_handler = f

    def on_client_message_action(self, f):
        self.on_client_message_action_handler = f

    def on_client_press_button(self, f):
        self.on_client_press_button_handler = f

    def on_client_slash_command(self, f):
        self.on_client_slash_command_handler = f

    def on_client_widget_action(self, f):
        self.on_client_widget_action_handler = f

    @staticmethod
    def send_response(handler, event, start_response):
        if handler is not None:
            try:
                body = handler(event)
                send_200_response(start_response)
                return body
            except:
                send_403_response(start_response)
                return {}
        else:
            send_404_response(start_response)
            return {}

    def handle(self, environ, start_response):
        if 'event_token_payload' not in environ:
            try:
                payload, event_json = TokenVerifierFilter.decode_and_verify_request(environ,
                                                                                    self.app_secret,
                                                                                    self.app_id)
                event = Event(event_json)
            except jwt.DecodeError:
                send_403_response(start_response)
                return {}
        else:
            payload, event = environ['event_token_payload'], Event(environ['request_body'])

        if event.name == "app.install":
            return EventHandlerClient.send_response(self.on_app_install_handler, event, start_response)
        elif event.name == "app.uninstall":
            return EventHandlerClient.send_response(self.on_app_uninstall_handler, event, start_response)
        elif event.name == "chat.generateUrlPreview":
            return EventHandlerClient.send_response(self.on_chat_generate_url_preview_handler, event, start_response)
        elif event.name == "chat.receiveMessage":
            return EventHandlerClient.send_response(self.on_chat_receive_message_handler, event, start_response)
        elif event.name == "client.flockmlAction":
            return EventHandlerClient.send_response(self.on_client_flockml_action_handler, event, start_response)
        elif event.name == "client.messageAction":
            return EventHandlerClient.send_response(self.on_client_message_action_handler, event, start_response)
        elif event.name == "client.openAttachmentWidget":
            return EventHandlerClient.send_response(self.on_client_open_attachment_widget_handler, event,
                                                    start_response)
        elif event.name == "client.pressButton":
            return EventHandlerClient.send_response(self.on_client_press_button_handler, event, start_response)
        elif event.name == "client.slashCommand":
            return EventHandlerClient.send_response(self.on_client_slash_command_handler, event, start_response)
        elif event.name == "client.widgetAction":
            return EventHandlerClient.send_response(self.on_client_widget_action_handler, event, start_response)
        else:
            raise Exception("Unknown event encountered" + event.name)
