import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os
from scipy.stats import zscore

# Carregar os dados
try:
    data = pd.read_csv('data/Estudos.csv', delimiter=';', encoding='latin1', on_bad_lines='skip', usecols=['Name', 'Type1', 'Totalstats'])
    print("Arquivo carregado com sucesso!")
    print(data.head())  # Verifique as primeiras 4 linhas

    # Limpar dados, se necessário
    data.dropna(axis=1, how='all', inplace=True)  # Remove colunas vazias
    print("Colunas após limpeza:", data.columns)
    
    data.duplicated(['Name', 'Type1', 'Totalstats'])
    data.duplicated().sum()
    data.drop_duplicates()
    print("Valores duplicados de colunas excluido com sucesso")
    
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
        
        # Criando um Boxplot para anlise de outliers 
        
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=data, x='Totalstats')
        plt.title("Boxplot para identificação de outliers")
        plt.show()
        

        # Calculando o Z-score
        data['Z-Score'] = zscore(data['Totalstats'])

        # Filtrando os dados com base no Z-score 
        data_no_outliers_z = data[data['Z-Score'].abs() <= 3]

        # Exibindo os dados sem outliers
        print("Dados sem valores atípicos (Z-score):\n", data_no_outliers_z[['Totalstats']])

        # Plotando o boxplot após a remoção dos outliers
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=data_no_outliers_z, x='Totalstats')
        plt.title("Boxplot sem Outliers (Z-score)")
        plt.show()
 
        print("Quantidade total de dados:", len(data))
        print("Quantidade de dados após remoção de outliers pelo Z-score:", len(data_no_outliers_z))

        # # Calculando o IQR para remover os outliers que são os valores fora do padrão
        
        # Q1 = data['Totalstats'].quantile(0.25)
        # Q3 = data['Totalstats'].quantile(0.75)
        # IQR = Q3 - Q1
        
        # # Definindo os limites para identificar os outliers (valores abaixo do lower ou em cima do upper são outliers)
        
        # lower_bound = Q1 - 1.5 * IQR
        # upper_bound = Q3 + 1.5 * IQR
        
        # # filtrando para apenas pegar os valores que não são outliers
        
        # naosao_outliers = data[(data['Totalstats'] >= lower_bound) & (data['Totalstats'] <= upper_bound)]
        
        # print("Dados sem valores atípicos:\n", naosao_outliers)
        
        # # Plotando o boxplot após a remoção dos outliers
        # plt.figure(figsize=(8, 5))
        # sns.boxplot(data=naosao_outliers, x='Totalstats')
        # plt.title("Boxplot sem Outliers")
        # plt.show()


except Exception as e:
    print("Erro ao carregar ou processar o arquivo:", e)
