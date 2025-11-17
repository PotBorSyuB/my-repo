from django.db import models
import random

class LottoTicket(models.Model):
    user_name = models.CharField(max_length=50)
    numbers = models.CharField(max_length=100)  # 예: "1,5,12,23,33,42"
    created_at = models.DateTimeField(auto_now_add=True)
    is_winner = models.BooleanField(default=False)

class LottoResult(models.Model):
    draw_date = models.DateTimeField(auto_now_add=True)
    winning_numbers = models.CharField(max_length=100)
