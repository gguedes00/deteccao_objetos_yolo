import torch
import subprocess
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def treinar_modelo():
    comando = [
        "python", 
        "yolov5/train.py", 
        "--img", "640", 
        "--batch", "8", 
        "--epochs", "10", 
        "--data", "dataset.yaml", 
        "--weights", "yolov5s.pt"
    ]
    
    resultado = subprocess.run(comando, capture_output=True, text=True)
    
    if resultado.returncode == 0:
        print("✅ Treinamento concluído!")
        return True
    else:
        print("❌ Erro no treinamento:", resultado.stderr)
        return False

def get_latest_experiment(dir_path="yolov5/runs/train"):
    """
    Busca automaticamente o diretório de experimento mais recente.
    Considera que os diretórios seguem o padrão 'exp', 'exp1', 'exp2', etc.
    """
    exp_dirs = [d for d in Path(dir_path).iterdir() if d.is_dir() and d.name.startswith("exp")]
    if not exp_dirs:
        raise FileNotFoundError(f"Nenhum diretório de experimento encontrado em {dir_path}")
    
    exp_dirs.sort(key=lambda d: int(d.name.replace("exp", "")) if d.name.replace("exp", "").isdigit() else 0)
    return exp_dirs[-1]

def detectar_objetos():
    latest_exp = get_latest_experiment("yolov5/runs/train")
    weights_dir = latest_exp / "weights"
    
    best_path = weights_dir / "best.pt"
    last_path = weights_dir / "last.pt"
    
    if best_path.exists():
        modelo_path = best_path
    elif last_path.exists():
        modelo_path = last_path
    else:
        raise FileNotFoundError("Modelo não encontrado! Treine primeiro.")
    
    print("Usando modelo:", modelo_path)
    model = torch.hub.load('ultralytics/yolov5', 'custom', path=str(modelo_path))
    
    img_path = "yolov5/dataset/imagem_test.jpg" 
    results = model(img_path)
    results.show()

def exibir_grafico_treinamento():
    """
    Exibe o gráfico de desempenho do treinamento.
    """
    latest_exp = get_latest_experiment("yolov5/runs/train")
    results_path = latest_exp / "results.png"
    
    if results_path.exists():
        img = Image.open(results_path)
        plt.figure(figsize=(10, 5))
        plt.imshow(img)
        plt.axis("off")
        plt.title("Gráfico de Treinamento do YOLOv5")
        plt.show()
    else:
        print("Gráfico não encontrado.")

if __name__ == "__main__":
    if treinar_modelo():
        detectar_objetos()
        exibir_grafico_treinamento()
