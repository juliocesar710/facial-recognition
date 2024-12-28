# Projeto: Classificação de Faces com Modelo Treinado



## Visão Geral

Este projeto utiliza um modelo de aprendizado profundo para classificação de imagens faciais em gêneros "Male" ou "Female". Ele combina um classificador de faces (Haar Cascade), um modelo treinado e um pipeline de pré-processamento para identificar e rotular faces em imagens carregadas pelo usuário. Embora funcional, o projeto ainda enfrenta dificuldades em reconhecer ambos os gêneros com alta precisão, indicando que melhorias nos dados e no treinamento seriam necessárias para resultados mais consistentes e robustos.


## 🗂️ Estrutura do Projeto

### 1. 📖 Dependências 
O projeto utiliza as seguintes bibliotecas:

- TensorFlow/Keras: Para carregar e inferir com o modelo.

- OpenCV: Para detecção de faces e manipulação de imagens.

- Pandas: Para manipulação do arquivo CSV com os atributos das imagens.

- Google Colab Utilities: Para upload e exibição de imagens no ambiente Colab.

### 📦 2. Dados Utilizados

- Modelo Treinado: Um modelo de reconhecimento facial treinado com dados de classificação de gêneros.

- CSV: Arquivo list_attr_celeba.csv, contendo atributos como IDs de imagem e valores binários indicando "Male" ou "Female".

- Imagens: Diretório de imagens faciais (CelebA).

### 🛠️3. Principais Componentes

a) Detecção de Faces
Função detect_faces(image) utiliza o Haar Cascade para identificar regiões faciais em uma imagem.

b) Pré-Processamento
Função preprocess_face(face):

- Redimensiona a imagem para (128x128).

- Normaliza os valores dos pixels.

- Adiciona uma dimensão para batching.

c) Classificação
Função classify_face(face) processa a face pré-processada no modelo e retorna a previsão de classe.

d) Visualização
Função visualize_results(image) exibe a imagem com rótulos e caixas delimitadoras para cada face detectada.


## ⚙️ Funcionalidades

### 🕵️‍♂️ 1. Detecção e Classificação
O sistema detecta faces em uma imagem e classifica-as como "Male" ou "Female". As informações são exibidas diretamente na imagem.


### ✅ 2. Upload de Imagem
Permite ao usuário carregar uma imagem para classificação. Utiliza o Google Colab para upload.


### 💻 3. Busca na Base de Dados
Scripts adicionais para analisar o CSV e determinar:

- Quantas imagens de cada gênero existem no dataset.

- O caminho da primeira imagem com a classe "Male", iniciando da última posição do CSV.


## 📈 Scripts Disponíveis [Aqui](./scripts)

### 1. Upload e Classificação de Imagem
Permite o upload de uma imagem para classificação. Após detectar e processar faces, o sistema exibe a imagem com as predições visíveis.

### 2. Contagem de Classes
Percorre o CSV e conta quantas imagens possuem o atributo "Male" ou "Female".

## 🔍 Instruções de Uso [Aqui](./notebooks/reconhecimento_facial_view.ipynb)

### 1. Carregar Arquivos:

- Modelo treinado (modelo_face_recognition.h5).

- Arquivo CSV (list_attr_celeba.csv).

- Diretório de imagens (por exemplo, img_align_celeba/).

### 2. Executar Scripts:

- Para classificação: upload_image().

- Para contagem de classes: count_classes().

[Scripts](./scripts)

### 3. Interpretação dos Resultados:

- As imagens são exibidas com rótulos e caixas delimitadoras.

- Saídas textuais indicam contagens e caminhos relevantes.


## 🎯 Melhorias Futuras

- Suporte a Várias Classes: Expandir o modelo para classificar outras características.

- Interface Gráfica: Criar uma interface para upload e visualização fora do Colab.

- Otimização de Detecção: Usar redes neurais como MTCNN para maior precisão.

- Pipeline Completo: Automatizar a integração entre detecção e classificação sem necessidade de preprocessamento manual.


## Autor e Colaboração

Este projeto foi desenvolvido com o objetivo de explorar aprendizado de máquina aplicado à classificação de imagens. Sugestões e colaborações são bem-vindas!
