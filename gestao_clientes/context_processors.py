from decouple import config


def get_app_version(request):
    app_version = config('HEROKU_RELEASE_VERSION', default=1)
    return {'APP_VERSION': app_version}
