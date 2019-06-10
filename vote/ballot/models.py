from django.db import models


class VotingProject(models.Model):
    option=models.CharField(max_length=100)

