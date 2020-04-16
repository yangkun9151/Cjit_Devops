from django.db import models


class Servers(models.Model):
    server_name = models.CharField(max_length=30)
    server_ip = models.CharField(max_length=30)
    port = models.CharField(max_length=20)

    def __str__(self):
        return self.server_name

