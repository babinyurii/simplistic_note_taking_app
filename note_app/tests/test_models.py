from django.test import TestCase
from note_app.models import NoteModel
# Create your tests here.


class NoteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        NoteModel.objects.create(note_name="test_name",
                                 note_text="test_text")
        
    def test_note_name_label(self):
        note = NoteModel.objects.get(id=1)
        field_label = note._meta.get_field('note_name').verbose_name
        self.assertEqual(field_label, 'note name')
    
    def test_note_text_lable(self):
        note = NoteModel.objects.get(id=1)
        text_label = note._meta.get_field('note_text').verbose_name
        self.assertEqual(text_label, 'note text')

    def test_note_name_max_length(self):
        note = NoteModel.objects.get(id=1)
        max_len = note._meta.get_field('note_name').max_length
        self.assertEqual(max_len, 50)

    def test_note_text_max_length(self):
        note = NoteModel.objects.get(id=1)
        max_len = note._meta.get_field('note_text').max_length
        self.assertEqual(max_len, 500)

    def test_object_name_is_note_name(self):
        note = NoteModel.objects.get(id=1)
        expected_note_name = f'{note.note_name}'
        self.assertEqual(str(note), expected_note_name)

    
        

    