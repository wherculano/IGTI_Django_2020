from django.shortcuts import render
from . import forms


# Create your views here.
def cadastro(request):
    form = forms.GeneroForm()
    if request.method == 'POST':
        form = forms.GeneroForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print('Erro')
    data_dict = {'form': form}
    return render(request, 'genero/genero.html', data_dict)
