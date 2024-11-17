import requests

# Отправка GET-запроса
response = requests.get('https://api.github.com')

# Проверка статуса ответа
if response.status_code == 200:
    print("Данные успешно получены:")
    print(response.json())  # Вывод данных в формате JSON
else:
    print(f"Ошибка: {response.status_code}")




import matplotlib.pyplot as plt

# Пример данных
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Построение линейного графика
plt.plot(x, y, marker='o')
plt.title('Пример линейного графика')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.show()



from PIL import Image, ImageFilter

# 1. Открытие изображения
image_path = 'example.jpg'  # Укажите путь к вашему изображению
img = Image.open(image_path)
print(f"Открыто изображение: {img.format}, размер: {img.size}, режим: {img.mode}")

# 2. Изменение размера изображения
new_size = (200, 200)  # Новый размер (ширина, высота)
resized_img = img.resize(new_size)
resized_img.show()  # Отображаем измененное изображение

# 3. Применение фильтра (размытие)
blurred_img = img.filter(ImageFilter.BLUR)
blurred_img.show()  # Отображаем размазанное изображение

# 4. Сохранение изображения в другом формате
output_path = 'output_image.png'
blurred_img.save(output_path)
print(f"Изображение сохранено как: {output_path}")