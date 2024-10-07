# Importando as bibliotecas necessárias
import pandas as pd

# 1. Leitura do dataset
file_path = 'C:\\Users\\reis1\\OneDrive\\Documentos\\Netflix\\netflix_titles.xlsx'
df = pd.read_excel(file_path)

# 2. Exibir as primeiras linhas e as colunas do dataset para entender a estrutura
print(df.head())  # Ver as primeiras linhas
print("Colunas presentes no dataset:")
print(df.columns)  # Exibir as colunas

# 3. Quantos filmes estão disponíveis na Netflix?
# Aqui eu Filtro a coluna 'type' para contar quantos títulos são filmes
total_filmes = df[df['type'] == 'Movie'].shape[0]
print(f"Total de filmes disponíveis na Netflix: {total_filmes}")

# 4. Quem são os 5 diretores com mais filmes e séries na plataforma?
# Aqui eu Utilizo a função 'value_counts()' para contar o número de produções de cada diretor
top_diretores = df['director'].value_counts().head(5)
print("Os 5 diretores com mais filmes e séries na Netflix são:")
print(top_diretores)

# 5. Quais diretores também atuaram como atores em suas próprias produções?
# Verifico se os diretores aparecem na coluna 'cast' (lista de atores)
df_non_null_cast = df.dropna(subset=['cast'])  # Remover valores nulos de 'cast'
diretores_atores = df_non_null_cast[df_non_null_cast['director'].isin(df_non_null_cast['cast'])]['director'].unique()
print("Diretores que também atuaram como atores:")
print(diretores_atores)

# 6. Insight adicional: Qual país tem mais títulos no catálogo?
# Uso 'value_counts()' para contar os títulos por país e pegamos o país com mais títulos
pais_com_mais_titulos = df['country'].value_counts().idxmax()
print(f"O país com mais títulos no catálogo da Netflix é: {pais_com_mais_titulos}")
