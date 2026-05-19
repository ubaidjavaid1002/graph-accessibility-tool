from django.db import models

class GraphUpload(models.Model):
    image = models.ImageField(upload_to='graphs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Graph {self.id}"