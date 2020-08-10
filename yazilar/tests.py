from django.test import TestCase, Client
from django.urls import reverse
from . models import Yazi

# Create your tests here.

def yazi_yarat(sayaç):
    """
    Verilen 'yazi' ile bir Yazi nesnesi yarat.
    """
    for yazi in range(sayaç):
        return Yazi.objects.create()


class Yazi_randomview_sorgusu(TestCase):
    def test_Yazi_random(self):
        """
        Yazılar 100 kez test edilir. Bir listeden pk'ler verilir.
        """
        yazı_pk = []
        yazı = yazi_yarat(sayaç=100).pk.append(yazı_pk)
        client = Client()
        response = client.get(reverse('yazilar:yazi'))
        return yazı_pk


