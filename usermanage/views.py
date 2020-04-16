from django.shortcuts import render
from django.contrib.auth.models import User


def user_list(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'usermanage/user_list.html', context)
