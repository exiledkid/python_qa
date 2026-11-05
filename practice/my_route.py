def my_route(handler):
    caught_request = 'GET /api/v1/fruits'
    handler(caught_request)

def log_request(request):
    print(f'Поймал: {request}')

my_route(log_request)
