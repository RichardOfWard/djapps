import sys


class AppLoader(object):

    package = "".join(__name__.split(".")[:-1])

    def __init__(self):
        self.__apps = None

    def register(self):
        sys.meta_path.append(self)

    def find_module(self, fullname, path):
        if fullname == 'djapps.django':
            return
        elif fullname.startswith('djapps.'):
            return self

    def load_module(self, fullname):
        split_path = fullname.split(".")
        app_name = split_path[1]
        extra_path = split_path[2:]
        app_path = self.get_app_path(app_name)
        import_path = '.'.join([app_path] + extra_path)
        __import__(import_path)
        sys.modules[fullname] = sys.modules[import_path]
        return sys.modules[import_path]

    def get_app_path(self, name):
        if self.__apps is None:
            from django.conf import settings
            self.__apps = {}
            for app_path in settings.INSTALLED_APPS:
                app_name = app_path.split('.')[-1]
                self.__apps[app_name] = app_path
        try:
            return self.__apps[name]
        except KeyError:
            raise ImportError(
                'No app named ' + name + ' in INSTALLED_APPS'
            )
