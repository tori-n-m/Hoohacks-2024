from django.db import modules

class Quiz(modules.Module):
    title = modules.CharField(max_length=100)
    content = modules.TextField()
    # Add more fields as needed