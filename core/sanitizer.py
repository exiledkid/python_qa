SENSITIVE_KEYS = ('password', 'token', 'authorization', 'secret', 'x-api-key', 'cookie', 'set-cookie', 'session_id')

def sanitize_data(data):
    if isinstance(data, list):
        return [sanitize_data(item) for item in data]
    if not isinstance(data, dict):
        return data

    sanitized = {}    
    for key, value in data.items():
        is_sensitive = False

        for word in SENSITIVE_KEYS:
            if word in str(key).lower():
                is_sensitive = True
                break

        if is_sensitive:
            sanitized[key] = '***MASKED***'
        elif isinstance(value, (list, dict)):
            sanitized[key] = sanitize_data(value)
        else:
            sanitized[key] = value

    return sanitized

if __name__ == '__main__':
    test_dict = {
        'title': 'test title',
        'body': 'test body',
        'user_password': '1337',
        'name': {
            'surname': 'alexandrov',
            'super_mega_password': 'lord1312'
        },
        'alex': [{'user': 'alex'}, {'hidden_token': '13123123123'}],
        'test': [1, 2, 3],
        'Authorization': 'Bearer',
        'api_token': 'taieiq0tiosd12'
    }

    filtered_dict = sanitize_data(test_dict)
    print(filtered_dict)