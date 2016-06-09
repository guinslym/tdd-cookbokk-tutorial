import pytest
#from django.test import RequestFactory
#from django.contrib.auth.models import AnonymousUser
#from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db

from .. import forms

class TestPostForm:
    def test_form(self):
        form = forms.PostForm(data={})
        assert form.is_valid() is False, 'Should be invalid if no data given'

        form = forms.PostForm(data={'body':'Hello'})
        assert form.is_valid() is False, 'Should be invalid if too short'
        assert 'body' in form.errors, 'Should include the word BODY in the error'

        form = forms.PostForm(data={'body':'Hello !!!!!!!!!!!!!!!!!!!'})
        assert form.is_valid() is True, 'Should be valid if long enough'
