import pytest
from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer

from .. import admin
from .. import models

#don't save it to the db
pytestmark = pytest.mark.django_db

class TestPostAdmin:
    def test_excerpt(self):
        site = AdminSite()
        post_admin = admin.PostAdmin(models.Post, Site)

        obj = mixer.blend('birdie.Post', body='Hello')
        result = post_admin.get_excerpt(obj)
        assert result == 'Hello', 'Should return first few characters'
