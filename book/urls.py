from django.urls import path
from .views import (HomeView, AuthorsList, AuthorsDetail,
                    AuthorCreation, AuthorBooksEdit)

app_name = 'book'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('authors/', AuthorsList.as_view(), name='authors'),
    path('authors/<str:pk>', AuthorsDetail.as_view(), name='authors-detail'),
    path('authors/add/', AuthorCreation.as_view(), name='authors-add'),
    path('authors/<str:pk>/books/edit/', AuthorBooksEdit.as_view(), name='author-books-edit'),
]
