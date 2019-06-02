from django.test import TestCase
from django.urls import resolve
from cv.views import cv
import json

# Create your tests here.


class CVPageTest(TestCase):

    def test_root_url_resolves_to_cv_fmu_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, cv)

    def test_cv_page_uses_cv_template(self):

        response = self.client.get("/")
        print(response.data)
        self.assertTemplateUsed(response, 'cv/cv.html')

    def test_cv_page_receives_data_dict(self):
        with open('cv/static/FMu.json', 'r') as file:
            json_dict = json.load(file)
        response = self.client.get("/")
        self.assertIn(response, json_dict)
