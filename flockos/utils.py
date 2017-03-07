from six import iteritems


def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + "".join(x.title() for x in components[1:])


def to_dict(model_dict):
    result = {}
    for attr, value in iteritems(model_dict):
        if value is None:
            continue
        attr = to_camel_case(attr[1:] if attr.startswith("_") else attr)
        if isinstance(value, list):
            result[attr] = list(map(
                lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                value
            ))
        elif hasattr(value, "to_dict"):
            result[attr] = value.to_dict()
        elif isinstance(value, dict):
            result[attr] = dict(map(
                lambda item: (item[0], item[1].to_dict())
                if hasattr(item[1], "to_dict") else item,
                value.items()
            ))
        else:
            result[attr] = value
    return result


def send_403_response(start_response):
    send_response('403 Forbidden', start_response)


def send_404_response(start_response):
    send_response('404 Not Found', start_response)


def send_200_response(start_response):
    send_response('200 OK', start_response)


def send_response(status, start_response):
    start_response(status, [('Content-Type', 'application/json')])
