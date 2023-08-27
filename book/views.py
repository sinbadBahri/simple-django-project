from typing import Any

from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import (TemplateView, ListView,
                                  DetailView, CreateView, FormView)

from .models import Author

from .forms import AuthorBooksFormset


class HomeView(TemplateView):
    template_name = 'book/home.html'


class AuthorsList(ListView):
    model = Author


class AuthorsDetail(DetailView):
    queryset = Author.objects.prefetch_related('books').all()
    fields = ['name']


class AuthorCreation(CreateView):
    model = Author
    fields = ['name']
    success_url = reverse_lazy('book:authors')


class AuthorBooksEdit(SingleObjectMixin, FormView):
    model = Author
    template_name = 'book/author_books_edit.html'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object(queryset=Author.objects.prefetch_related('books').all())
        return super().get(request, *args, **kwargs)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        self.object = self.get_object(queryset=Author.objects.prefetch_related('books').all())
        return super().post(request, *args, **kwargs)

    def get_form(self, form_class=None) -> Any:
        return AuthorBooksFormset(**self.get_form_kwargs(), instance=self.object)

    def form_valid(self, form) -> HttpResponseRedirect:
        form.save()
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Changes were saved !',
        )

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self) -> str:
        return reverse(viewname='book:authors-detail', args=[self.object.pk])
