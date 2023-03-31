from django.urls import path, include
from . import views



urlpatterns = [ 

    path("",
        views.NoteListView.as_view(),
        name="note_list"),

    path("create_note",
         views.NoteCreateView.as_view(),
         name="create_note"),
    
    path("note/<int:pk>/",
         views.NoteDetailView.as_view(),
         name="note_detail"),

    path("note/<int:pk>/delete",
         views.NoteDeleteView.as_view(),
         name="delete_note"),

    path("note/<int:pk>/update",
         views.NoteUpdateView.as_view(),
         name="update_note"),

     path("signup",
          views.signup,
          name="signup"),
     
     path("accounts/", 
          include("django.contrib.auth.urls")),

]