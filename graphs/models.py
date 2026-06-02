from django.db import models

class Graph(models.Model):

    image = models.ImageField(
        upload_to='graphs/'
    )

    extracted_text = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Graph {self.id}"