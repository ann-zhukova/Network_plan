class TunnelingMethodMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and 'method' in request.POST:
            if request.POST['method'] == 'DELETE':
                request.method = 'DELETE'
            elif request.POST['method'] == 'PUT':
                request.method = 'PUT'
        return self.get_response(request)

