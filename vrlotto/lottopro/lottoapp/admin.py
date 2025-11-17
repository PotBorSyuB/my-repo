from django.contrib import admin
from .models import LottoTicket, LottoResult

admin.site.register(LottoTicket)
admin.site.register(LottoResult)