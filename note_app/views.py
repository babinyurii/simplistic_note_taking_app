from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import NoteModel
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
# Create your views here.

class NoteListView(ListView):
    model = NoteModel
    queryset = NoteModel.objects.all().order_by("-date_created")
    paginate_by = 12
    template_name = "note_list.html"


class NoteCreateView(CreateView):
    model = NoteModel
    fields = ["note_name", "note_text"]
    template_name = "create_note.html"
    success_url = reverse_lazy("note_list")
    #def get_success_url(self):
    #    return reverse_lazy("note_list")
    
class NoteDetailView(DetailView):
    template_name = "note_detail.html"
    model = NoteModel

class NoteDeleteView(DeleteView):
    model = NoteModel
    template_name = "delete_note.html"
    success_url = reverse_lazy("note_list")

class NoteUpdateView(UpdateView):
    model = NoteModel
    fields = ["note_name", "note_text"]
    template_name = "update_note.html"
    
    def get_success_url(self):
        return reverse_lazy("note_detail", 
                            kwargs={"pk": self.object.id})


def signup(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST) # don't forget this arg
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = UserCreationForm()

    return render(request, 
                  "registration/signup.html",
                  context={"form": form})

    
    

