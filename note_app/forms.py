from django import forms
from .models import NoteModel

class NoteCreateForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ("note_name", "note_text")

class NoteUpdateForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = ("note_name", "note_text")

