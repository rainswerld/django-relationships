from django.db import models

class Loan(models.Model):
    due_date = models.DateField()

    def __str__(self):
        return self.due_date
