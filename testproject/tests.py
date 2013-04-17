import os
import sys
from unittest import TestCase as BaseTestCase
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testproject.settings")


class TestCase(BaseTestCase):
    def assertIs(self, a, b):
        if sys.version_info[:2] == (2, 6):
            return self.assertTrue(a is b)
        else:
            return super(TestCase, self).assertIs(a, b)


class DjangoLoading(TestCase):

    def test_0010_import_djapps(self):
        import djapps
        assert(djapps)

    def test_0020_import_normal(self):
        import testproject.apps.app1 as m1
        assert(m1)

    def test_0030_import_app_module(self):
        import testproject.apps.app1 as m1
        import djapps.app1 as m2
        self.assertIs(m1, m2)

    def test_0040_import_app_models(self):
        import testproject.apps.app1.models as m1
        import djapps.app1.models as m2
        self.assertIs(m1, m2)

    def test_0050_import_app_models_from(self):
        import testproject.apps.app1.models as m1
        from djapps.app1 import models as m2
        self.assertIs(m1, m2)

    def test_0060_import_app_model(self):
        from testproject.apps.app1.models import TestModel as m1
        from djapps.app1.models import TestModel as m2
        self.assertIs(m1, m2)

    def test_0070_import_app_model(self):
        import djapps.app1.models
        djapps.app1.models
        self.assertIs(
            sys.modules['djapps.app1.models'],
            sys.modules['testproject.apps.app1.models'],
        )
