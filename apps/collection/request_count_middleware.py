from .models import *
class RequestCountMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Retrieve the request count from the database
        request_counter, created = RequestCounter.objects.get_or_create(pk=1)
        request_count = request_counter.count

        # Increment the request count
        request_count += 1
        request_counter.count = request_count
        request_counter.save()

        response = self.get_response(request)
        return response