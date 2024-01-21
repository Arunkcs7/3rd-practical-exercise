# myapp/views.py
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotModified
from django.http import HttpResponseBadRequest, HttpResponseForbidden, HttpResponseNotAllowed, HttpResponseGone
from django.http import HttpResponseServerError, HttpResponseNotFound, JsonResponse, StreamingHttpResponse, FileResponse
from django.conf import settings
import os
import time

def simple_response(request):
    return HttpResponse("This is a simple HTTP response.")

def redirect_example(request):
    return HttpResponseRedirect('/new_url/')

def permanent_redirect_example(request):
    return HttpResponsePermanentRedirect('/new_url/')

def not_modified_example(request):
    return HttpResponseNotModified()

def bad_request_example(request):
    return HttpResponseBadRequest("Bad request.")

def forbidden_example(request):
    return HttpResponseForbidden("Forbidden.")

def not_allowed_example(request):
    return HttpResponseNotAllowed(['GET', 'POST'])

def gone_example(request):
    return HttpResponseGone("Resource is gone.")

def server_error_example(request):
    return HttpResponseServerError("Internal Server Error.")

def not_found_example(request):
    return HttpResponseNotFound("Page not found.")

def json_response_example(request):
    data = {'key': 'value'}
    return JsonResponse(data)

def streaming_response(request):
    def stream_content():
        yield "Streaming "
        time.sleep(1)
        yield "response."

    return StreamingHttpResponse(stream_content())

def serve_file(request):
    file_path = os.path.join(settings.BASE_DIR, 'path/to/your/file.txt')
    return FileResponse(open(file_path, 'rb'))

