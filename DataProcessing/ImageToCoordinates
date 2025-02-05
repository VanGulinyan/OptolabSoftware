import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def load_image(image_path):
    # Загрузка изображения
    img = Image.open(image_path).convert('L')  # Конвертирование в оттенки серого
    img_array = np.array(img)
    
    # Конвертирование в бинарное представление: 0 для черных пикселей, 1 для белых
    binary_img = (img_array < 128).astype(int)  # Черные пиксели имеют значения меньше 128
    
    return binary_img

def extract_coordinates(binary_img):
    coords = []
    for y in range(binary_img.shape[0]):
        for x in range(binary_img.shape[1]):
            if binary_img[y][x] == 1:  # Черный пиксель
                coords.append((y, x))
    return coords

def plot_path(coords):
    plt.figure(figsize=(10, 10))
    if len(coords) > 0:
        path_x, path_y = zip(*coords)
        plt.plot(path_y, path_x, color='red', marker='o', linestyle='none')
    plt.gca().invert_yaxis()  # Инвертируем ось Y для соответствия координатам изображения
    plt.title("Path of Black Pixels")
    plt.xlabel("X coordinate")
    plt.ylabel("Y coordinate")
    plt.show()

if __name__ == "__main__":
    # Путь к изображению
    image_path = 'C:\images.png'
    
    # Загрузка изображения
    binary_img = load_image(image_path)
    
    # Извлечение координат черных пикселей
    coords = extract_coordinates(binary_img)
    
    if len(coords) == 0:
        print("Нет черных пикселей найдено в изображении.")
    else:
        # Вывод пути на графике
        plot_path(coords)
