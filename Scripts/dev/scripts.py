import pyautogui
import time
import os
from PIL import Image

time.sleep(1)

file_path = 'screenshot.png'
pyautogui.screenshot(file_path)

if os.path.exists(file_path):
    print(f"Print tirado com sucesso e salvo como {file_path}")

    try:
        img = Image.open(file_path)
        img.show()  
        print("Imagem aberta com sucesso.")
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
else:
    print("Erro ao tirar o print.")
