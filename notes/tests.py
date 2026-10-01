from django.test import TestCase
from rest_framework.test import APIClient

from .models import Note


class NoteAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_notes(self):
        response = self.client.get("/api/notes/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_create_note(self):
        data = {
            "title": "Docker",
            "content": "Learn Docker Compose",
        }

        response = self.client.post("/api/notes/", data, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["title"], "Docker")
        self.assertEqual(response.json()["content"], "Learn Docker Compose")

        self.assertEqual(Note.objects.count(), 1)
