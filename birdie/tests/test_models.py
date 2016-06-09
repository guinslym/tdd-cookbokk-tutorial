import pytest
from mixer.backend.django import mixer

#Don't try to write in the database
pytestmark = pytest.mark.django_db

class TestPost:
    def test_init(self):
        obj=mixer.blend('birdie.Post')
        assert obj.pk == 1, 'Should save an isntance'

    def test_get_excerpt(self):
        obj = mixer.blend('birdie.Post', body='Hello World!')
        result = obj.get_excerpt(5)
        assert result == 'Hello', 'Should return first 5 characters'
