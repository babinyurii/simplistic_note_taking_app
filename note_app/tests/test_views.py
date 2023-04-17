from django.test import TestCase
from note_app.models import NoteModel
# Create your tests here.
from django.urls import reverse

class NoteListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        num_of_notes = 10
        for note_id in range(num_of_notes):
            NoteModel.objects.create(
                note_name=f'note name {note_id}',
                note_text=f'note text {note_id}'
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_url_name(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'note_list.html')
