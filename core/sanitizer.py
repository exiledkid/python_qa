SENSITIVE_KEYS = {'password', 'token', 'secret', 'authorization', 'api_key', 'access_token'}


def sanitize_data(data):
    if isinstance(data, list):
        return [sanitize_data(item) for item in data]
    
    if not isinstance(data, dict):
        return data

    sanitized = {}
    for key, value in data.items():
        if str(key).lower() in SENSITIVE_KEYS:
            sanitized[key] = '***MASKED***'
        elif isinstance(value, (dict, list)):
            sanitized[key] = sanitize_data(value)
        else:
            sanitized[key] = value

    return sanitized