from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.
def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):
    perfil = Perfil()

    if perfil_id == 1:
        perfil = Perfil('Maria Alves', 'maria.alves@ifb.edu.br', '112233445', 'IFB')
    
    if perfil_id == 2:
        perfil = Perfil('Elon Musk', 'elon.musk@tesla.com', '333333', 'Tesla') 
    
    return render(request, 'perfil.html', {'perfil' : perfil})