from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import ListView

from .serializers import CreateUserSerializer, UserSerializer, PostSerializer
from .mixins import LikedMixin
from .forms import UserForm
from .models import Post


class IndexView(ListView):
    template_name = 'blog.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by("-date")


def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Token.objects.create(user=new_user)
            return redirect('../login')
    else:
        user_form = UserForm()
    return render(request, 'registration_form.html', {'user_form': user_form})


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        self.serializer_class = CreateUserSerializer
        self.permission_classes = (AllowAny,)
        return super(UserViewSet, self).create(request, *args, **kwargs)


class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

