import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
from .forms import DataFileForm
from .models import DataFile

def upload_file(request):
    if request.method == 'POST':
        form = DataFileForm(request.POST, request.FILES)
        if form.is_valid():
            datafile = form.save()

            # Leitura do arquivo CSV com Pandas
            df = pd.read_csv(datafile.file.path)

            # Geração de um gráfico simples com Seaborn
            plt.figure(figsize=(10, 6))
            sns.histplot(df['coluna_interessante']) # Substitua 'coluna_interessante' por uma coluna real do seu CSV
            plt.title('Histograma da Coluna Interessante')
            plt.savefig('static/graph.png') # Salve o gráfico na pasta 'static'

            return render(request, 'result.html', {'datafile': datafile})
    else:
        form = DataFileForm()

    return render(request, 'upload.html', {'form': form})