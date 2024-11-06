import pandas as pd
import matplotlib.pyplot as plt
import os

# Carregar os dados
try:
    data = pd.read_csv('data/Estudos.csv', delimiter=';', encoding='latin1', on_bad_lines='skip', usecols=['Name', 'Type1', 'Totalstats'])
    print("Arquivo carregado com sucesso!")
    print(data.head())  # Verifique as primeiras 4 linhas

    # Limpar dados, se necessário
    data.dropna(axis=1, how='all', inplace=True)  # Remove colunas vazias
    print("Colunas após limpeza:", data.columns)

    # Verifique se as colunas 'Totalstats' e 'Type1' existem
    if 'Totalstats' not in data.columns:
        print("Erro: A coluna 'Totalstats' não existe no arquivo.")
    if 'Type1' not in data.columns:
        print("Erro: A coluna 'Type1' não existe no arquivo.")
    
    # Criar a pasta 'outputs' caso não exista
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
        print("Pasta 'outputs' criada.")

    # Gerar o histograma
    if 'Totalstats' in data.columns:
        plt.figure(figsize=(8, 6))
        data['Totalstats'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
        plt.title('Histograma de Totalstats')
        plt.xlabel('Totalstats')
        plt.ylabel('Frequência')
        plt.show()  # Exibe o gráfico para verificar se está correto
        plt.savefig('outputs/histograma.png')  # Salva o histograma
        print("Histograma salvo em 'outputs/histograma.png'")

    # Gerar o gráfico de dispersão
    if 'Totalstats' in data.columns and 'Type1' in data.columns:
        data['Type1_numeric'] = pd.factorize(data['Type1'])[0]
        plt.figure(figsize=(8, 6))
        plt.scatter(data['Type1_numeric'], data['Totalstats'], color='green', alpha=0.5)
        plt.title('Gráfico de Dispersão: Type1 vs Totalstats')
        plt.xlabel('Type1 (numérico)')
        plt.ylabel('Totalstats')
        plt.show()  # Exibe o gráfico para verificar se está correto
        plt.savefig('outputs/grafico_dispercao.png')  # Salva o gráfico de dispersão
        print("Gráfico de dispersão salvo em 'outputs/grafico_dispercao.png'")

except Exception as e:
    print("Erro ao carregar ou processar o arquivo:", e)
