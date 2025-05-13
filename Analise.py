import pandas as pd

# Carrega o arquivo CSV
df = pd.read_csv("filmes.csv")

# Mostra os 3 primeiros registros
print("🎬 Primeiros filmes:")
print(df.head(3))
print()

# Média de duração dos filmes
# Média de duração dos filmes
media_duracao = df["Duração"].mean()
print(f"🕒 Duração média: {media_duracao:.1f} minutos")

# Filme com maior nota
filme_top = df.loc[df["Nota"].idxmax()]
print(f"\n🏆 Filme mais bem avaliado: {filme_top['Título']} ({filme_top['Nota']})")

# Quantidade de filmes por gênero
print("\n📊 Filmes por gênero:")
print(df["Genero"].value_counts())
