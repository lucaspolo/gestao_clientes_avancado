from decouple import config


class MetaData():
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        return response

    def process_template_response(self, request, response):
        app_version = config('app_version', default=1)
