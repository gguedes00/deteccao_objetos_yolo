# YOLOv5 - Desafio BairesDev | DIO - Machine Learning Practitioner

Este repositório apresenta a solução desenvolvida para o desafio BairesDev - Machine Learning Practitioner na DIO (Digital Innovation One). O projeto consiste na implementação e treinamento de um modelo YOLOv5 para detecção de objetos em imagens, incluindo a visualização dos resultados e métricas do treinamento.

## 🖼️ Pré-processamento e Anotação

🖍️ Script de Anotação Manual (Python Customizado)

Objetivo:
Criar labels no formato YOLO para suas imagens quando ferramentas como LabelMe não estão disponíveis.

📂 Estrutura Necessária:

deteccao_objetos_yolo
└──annotate_yolo/
 imagens/  

## 🛠️ Como Usar:
Crie o arquivo annotate_yolo.py:

annotate_yolo.py

import cv2
import os

Execute o script:

python annotate_yolo.py

## 🕹️ Controles:

Tecla	Ação
1	Selecionar classe Gato
2	Selecionar classe Cachorro
Clique + Arraste	Desenhar Bounding Box
S	Salvar anotação
N	Próxima imagem
ESC	Sair do programa

## 🎯 Saída Gerada:

dataset/
├── images/  
└── labels/  # Labels no formato YOLO
    ├── 1.txt
    ├── 2.txt
    └── ...
Exemplo de arquivo 1.txt:

0 0.456 0.372 0.120 0.250  # Gato
1 0.743 0.611 0.150 0.300  # Cachorro

## 💡 Dicas:

Mantenha os nomes das imagens e labels idênticos (ex: img1.jpg ↔ img1.txt)

Para imagens sem objetos, crie um arquivo .txt vazio

Revise as anotações no Validate Data antes do treinamento

## 📌 Tecnologias Utilizadas

Python 3.11+

PyTorch

YOLOv5 (Ultralytics)

OpenCV

Matplotlib

NumPy

Pandas


📂 Estrutura do Repositório

📦 deteccao_objetos_yolo/
├── annotate_yolo/ 
│ ├── images/ 
│ ├── labels/ 
│ └── annotate_yolo.py 
├── yolov5/ # Repositório oficial YOLOv5 
├── myenv/ # Ambiente virtual
├── deteccao_objetos_yolo.py 
├── dataset.yaml 
├── yolov5s.pt 
└── README.md 

# 🚀 Instalação e Execução

## 1️⃣ Clonar o Repositório

git clone https://github.com/gguedes00/deteccao_objetos_yolo.git
cd deteccao_objetos_yolo

## 2️⃣ Criar e Ativar um Ambiente Virtual

python -m venv myenv
source myenv/bin/activate  # Linux/macOS
myenv\Scripts\activate     # Windows

## 3️⃣ Instalar Dependências

pip install -r requirements.txt

## 4️⃣ Baixar o YOLOv5

git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
cd ..

## 5️⃣ Executar o Treinamento e a Detecção

python deteccao_objetos_yolo.py

📊 Visualização dos Resultados

As métricas do treinamento, como perda e precisão, são salvas em yolov5/runs/train/expX/.

Para exibir o gráfico de desempenho do treinamento, o script renderiza automaticamente results.png.

As imagens com detecções são salvas em yolov5/runs/detect/expX/.

## 📌 Personalização

Para ajustar hiperparâmetros, modifique deteccao_objetos_yolo.py, alterando:

comando = [
    "python",
    "yolov5/train.py",
    "--img", "640",
    "--batch", "8",
    "--epochs", "10",  # Alterar para mais épocas
    "--data", "dataset.yaml",
    "--weights", "yolov5s.pt"
]

## 📄 Licença

Este projeto é de uso livre sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

Desenvolvido por Gabriel Guedes
