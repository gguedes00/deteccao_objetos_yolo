import cv2
import os

# Configurações
IMAGES_DIR = "images"  # Pasta com suas imagens
LABELS_DIR = "labels"  # Pasta onde os arquivos .txt serão salvos
CLASSES = {'1': 'cat', '2': 'dog'}  # Teclas para seleção de classe

# Variáveis globais
current_class = 0  # 0 = cat, 1 = dog (índice YOLO)
points = []
drawing = False

# Criar pasta de labels se não existir
os.makedirs(LABELS_DIR, exist_ok=True)

# Função para capturar cliques do mouse
def click_event(event, x, y, flags, param):
    global points, drawing, img_display, img_original

    if event == cv2.EVENT_LBUTTONDOWN:
        points = [(x, y)]
        drawing = True

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        img_copy = img_display.copy()
        cv2.rectangle(img_copy, points[0], (x, y), (0, 255, 0), 2)
        cv2.imshow("Image", img_copy)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        points.append((x, y))
        cv2.rectangle(img_display, points[0], points[1], (0, 255, 0), 2)
        cv2.imshow("Image", img_display)

# Processar todas as imagens
for image_name in os.listdir(IMAGES_DIR):
    image_path = os.path.join(IMAGES_DIR, image_name)
    img_original = cv2.imread(image_path)
    h, w = img_original.shape[:2]  # Dimensões originais da imagem
    
    # Redimensionar para visualização (mantém aspect ratio)
    scale = min(800 / w, 600 / h)
    img_display = cv2.resize(img_original, (int(w * scale), int(h * scale)))
    
    # Configurar janela e mouse callback
    cv2.imshow("Image", img_display)
    cv2.setMouseCallback("Image", click_event)
    
    annotations = []  # Lista para guardar anotações da imagem
    
    while True:
        key = cv2.waitKey(1) & 0xFF

        # Tecla '1' para classe 'cat' (índice 0)
        if key == ord('1'):
            current_class = 0
            print("Classe selecionada: CAT (0)")

        # Tecla '2' para classe 'dog' (índice 1)
        elif key == ord('2'):
            current_class = 1
            print("Classe selecionada: DOG (1)")

        # Tecla 's' para salvar bounding box
        elif key == ord('s') and len(points) == 2:
            # Converter coordenadas para a imagem original
            x1 = int(points[0][0] / scale)
            y1 = int(points[0][1] / scale)
            x2 = int(points[1][0] / scale)
            y2 = int(points[1][1] / scale)
            
            # Calcular coordenadas YOLO (normalizadas)
            x_center = ((x1 + x2) / 2) / w
            y_center = ((y1 + y2) / 2) / h
            bbox_width = (x2 - x1) / w
            bbox_height = (y2 - y1) / h
            
            # Adicionar à lista de anotações
            annotations.append(f"{current_class} {x_center:.6f} {y_center:.6f} {bbox_width:.6f} {bbox_height:.6f}")
            print(f"Bounding box salvo: {CLASSES[str(current_class + 1)]}")
            points = []

        # Tecla 'n' para próxima imagem
        elif key == ord('n'):
            break

        # Tecla 'Esc' para sair
        elif key == 27:
            cv2.destroyAllWindows()
            exit()

    # Salvar anotações no arquivo .txt
    if annotations:
        label_name = os.path.splitext(image_name)[0] + ".txt"
        label_path = os.path.join(LABELS_DIR, label_name)
        with open(label_path, "w") as f:
            f.write("\n".join(annotations))
        print(f"Arquivo {label_name} salvo!")

cv2.destroyAllWindows()