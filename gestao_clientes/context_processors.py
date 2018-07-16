from decouple import config


def get_app_version(request):
    app_version = config('app_version', default=1)
    return {'APP_VERSION': app_version}
