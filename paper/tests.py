from django.test import TestCase


# Create your tests here.


class TestPaper(TestCase): # simple test for example
    def test_access(self):
        response = self.client.get('/')