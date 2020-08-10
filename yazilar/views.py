from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import Yazı
from .forms import YazıForm
import random


# Create your views here.

class YazıView(TemplateView):
    template_name = 'yazilar/yazi.html'

    def get(self, request):
        yazılarım = Yazı.objects.all()
        yazı_listem = list(yazılarım)
        yazilar = random.choice(yazı_listem)
        return render(request, self.template_name, {'yazilar':yazilar})


def yazdır(request):
    if request.method == 'POST':
        form = YazıForm(request.POST)
        form.save()
        return redirect('http://karyadanyazilar.com')
    else:
        form = YazıForm()
    return render(request,
                  'yazilar/yaz.html',
                  {'form': form}
                  )
