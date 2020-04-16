from django.shortcuts import render, redirect
from .models import Servers
from .forms import ServerForm
from django.http import HttpResponse


def server_list(request):
    servers = Servers.objects.all()
    context = {'servers': servers}
    return render(request, 'servers/list.html', context)


def add_server(request):
    if request.method == "POST":
        Server_forms = ServerForm(data=request.POST)
        if Server_forms.is_valid():
            new_server = Server_forms.save(commit=False)
            serverip = Servers.objects.filter(server_ip=request.POST['server_ip'])
            if serverip.count() == 0:
                new_server.save()
                return redirect("server:server_list")
            else:
                return HttpResponse("服务器已存在，不用添加了")
    else:
        Server_forms = ServerForm()
        context = {'Server_forms': Server_forms}
        return render(request, 'servers/add.html', context)


def delete_server(request):
    if request.method == "POST":
        servername = Servers.objects.get(id=request.POST.get('server_id'))
        servername.delete()
        return redirect('index:index')
    else:
        return HttpResponse("请使用POST请求")


def edit_server(request, id):
    servername = Servers.objects.get(id=id)
    if request.method == "POST":
        Server_forms = ServerForm(data=request.POST)
        if Server_forms.is_valid():
            servername.server_name = request.POST['server_name']
            servername.server_ip = request.POST['server_ip']
            servername.port = request.POST['port']
            servername.save()
            return redirect('server:server_list')
    else:
        Server_forms = ServerForm()
        context = {'Server_forms': Server_forms,'servername': servername}
        return render(request, 'servers/edit.html', context)
