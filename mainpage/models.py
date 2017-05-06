from django.db import models


class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    form_message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
