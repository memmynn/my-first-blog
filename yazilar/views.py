from django.shortcuts import render
from .models import Yazi


# Create your views here.
def yazi(request):
    yazilar = Yazi.objects.order_by("?").first()
    return render(request, 'yazilar/yazi.html', {'yazilar': yazilar})
