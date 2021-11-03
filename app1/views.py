from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth.models import Group, ContentType, Permission
from django.contrib.auth.mixins import PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Books
from django.views.generic import ListView, UpdateView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.contenttypes.models import ContentType

class HomePageView(TemplateView):
    template_name = 'home.html'


class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Books
    template_name = 'booknew.html'
    # context_object_name = 'bookcreate'
    fields = ['title', 'author_name', 'pageno']
    # if using PermissionRequiredMixin
    permission_required = "app1.add_books"


class BooksDetails(PermissionRequiredMixin, ListView):
    model = Books
    template_name = 'booklist.html'
    context_object_name = 'booklists'
    # if using PermissionRequiredMixin
    permission_required = "app1.view_books"


class BookIndiviView(PermissionRequiredMixin, DetailView):
    model = Books
    template_name = 'bookdetails.html'
    context_object_name = 'bookdetails'
    # if using PermissionRequiredMixin
    permission_required = "app1.view_books"


class BookUpdateView(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Books
    template_name = 'book_edit.html'
    # context_object_name = 'book-edit'
    # if using PermissionRequiredMixin
    # fields = ['title']
    # fields = ['title', 'author_name', 'pageno']
    def test_func(self):  # new
        obj = self.get_object()
        return obj.author_name == self.request.user

    permission_required = "app1.canedittitle"

    if permission_required:
        fields = ['title', 'author_name', 'pageno']

    # permission_required2 = "app1.change_books"
    # if permission_required and not permission_required2:
    #     fields = ['title']

    # elif permission_required and permission_required2:
    #     fields = ['title', 'author_name']


# related to permissions
# @permission_required('app1.change_books')
# def BookUpdateView(request, pk):
#     cc = ContentType.objects.get_for_model(Books)
#     # if request.user.Permission.objects.filter(codename='canedittitle', content_type=cc) !=None:
    
#     # user M2M permission
#     # Permission <-----> User


#     # per = Permission.objects.filter(codename='canedittitle', content_type=cc)
#     # if per:
#     # if request.user.permission.filter(codename="app1.canedttitile_books", contentype=ct).exists():

#     if request.user.has_perm('app1.canedittitle'):
#         booklists = Books.objects.all()
#         return render(request, "book_edit.html", {"booklists": booklists})
#     else:
#         return HttpResponse("Not allowed")






# related to permissions
# @permission_required('app1.view_books')
# def BooksDetails(request):
#     # ct = ContentType.objects.get_for_model(PremiumProduct)
#     # if request.user.permissions.filter(codename = "view_premiumproducts" , contentype = ct).exists():

#     if request.user.has_perm('app1.view_books'):
#         booklists = Books.objects.all()
#         return render(request, "booklist.html", {"booklists": booklists})
#     else:
#         return HttpResponse("Not allowed")


class AboutPageView(TemplateView):
    template_name = 'about.html'


#from django.contrib.auth.models import Group, ContentType, Permission
# ct = ContentType.objects.get_for_model(PremiumProduct)
# permission = Permission.objects.create(codename="can_do_this", contentype = ct)

# ----------------------------------
# cc = ContentType.objects.get_for_model(Books)
# Permission.objects.get(codename='canedittitle', content_type=cc)
