from django.shortcuts import render
from .models import LottoTicket, LottoResult
import random

def buy_lotto(request):
    if request.method == "POST":
        user = request.POST.get("user")
        mode = request.POST.get("mode")

        if mode == "auto":
            nums = sorted(random.sample(range(1,46), 6))
        else:
            nums = request.POST.get("numbers").split(",")

        LottoTicket.objects.create(
            user_name=user,
            numbers=",".join(map(str, nums))
        )
    return render(request, "buy.html")

def check_result(request):
    tickets = LottoTicket.objects.all()
    result = LottoResult.objects.last()
    return render(request, "check.html", {"tickets": tickets, "result": result})

# 관리자 기능
def draw(request):
    nums = sorted(random.sample(range(1,46), 6))
    LottoResult.objects.create(winning_numbers=",".join(map(str, nums)))

    for t in LottoTicket.objects.all():
        if t.numbers == ",".join(map(str, nums)):
            t.is_winner = True
            t.save()

    return render(request, "draw.html", {"numbers": nums})

def stats(request):
    tickets = LottoTicket.objects.count()
    winners = LottoTicket.objects.filter(is_winner=True).count()
    return render(request, "stats.html", {"tickets": tickets, "winners": winners})

def index(request):
    return render(request, "index.html")