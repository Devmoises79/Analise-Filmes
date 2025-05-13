## Análise de Filmes com Pandas 🐻👨🏾‍💻
Este projeto realiza a análise simples de uma lista de filmes utilizando a biblioteca Pandas, com operações básicas de leitura e manipulação de dados. Ele tem como objetivo apresentar como usar o Pandas para obter informações úteis e realizar cálculos rápidos.

## Funcionalidades
- Carrega uma tabela de filmes contendo informações como título, ano, gênero, duração e nota.

- Calcula a média de duração dos filmes.

- Exibe o filme mais bem avaliado.

- Realiza uma análise por gênero, mostrando quantos filmes existem em cada categoria.

## Como Funciona
O projeto utiliza um DataFrame do Pandas para armazenar e manipular dados sobre filmes. Ele segue os seguintes passos:

- Carregamento dos dados: Uma lista com informações sobre os filmes é convertida em um DataFrame do Pandas.

- Cálculos e análises:

- Duração média: Calcula a média da duração dos filmes.

- Filme mais bem avaliado: Identifica qual filme possui a maior nota.

- Análise de gênero: Conta quantos filmes existem em cada gênero.

## Exemplo de Saída
Ao executar o código, o seguinte resultado pode ser exibido:

```yaml

Primeiros filmes:
      Título   Ano    Genero  Duração  Nota
0  Inception  2010   Ficção      148    8.8
1    Titanic  1997  Romance      195    7.8
2     Avatar  2009   Ficção      162    7.9

Duração média: 171.5 minutos

Filme mais bem avaliado: Inception (8.8)

Filmes por gênero:
Genero
Ficção     2
Romance    1
Ação       1
Name: count, dtype: int64
```

## Tecnologias Utilizadas
- Python: A linguagem utilizada para o desenvolvimento do código.

- Pandas: Biblioteca fundamental para manipulação e análise de dados.

## Como Executar
Certifique-se de ter o Python instalado em sua máquina.

Instale a biblioteca pandas utilizando o comando:

```bash
pip install pandas
```

Execute o script:

```bash
python Analise.py
```


## Estrutura do Projeto
Analise.py: O script principal que contém a lógica para análise dos filmes.
