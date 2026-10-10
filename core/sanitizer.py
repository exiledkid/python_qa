# Файл: core/sanitizer.py
SENSITIVE_KEYS = ('password', 'token', 'authorization', 'secret', 'x-api-key', 'cookie', 'session_id')

def sanitize_data(data):
    if isinstance(data, list):
        return [sanitize_data(item) for item in data]
    if not isinstance(data, dict):
        return data

    sanitized = {}
    for key, value in data.items():
        if str(key).lower() in SENSITIVE_KEYS:
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
        'password': 'super_secret_123',
        'name': {
            'surname': 'alexandrov',
            'name': 'anton'
        },
        'test': [1, 2, 3]
    }

    filtered_dict = sanitize_data(test_dict)
    print(filtered_dict)


# --- БЛОК ДЛЯ САМОПРОВЕРКИ ---
# Если файл запущен напрямую (if __name__ == '__main__'):
# 1. Создай тестовый словарь, в котором есть обычные поля, 
#    секретное поле на верхнем уровне, список словарей и вложенный словарь с секретами.
# 2. Прогони этот словарь через функцию.
# 3. Распечатай результат и убедись, что все пароли скрыты, а структура не сломалась.