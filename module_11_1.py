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


import numpy as np

# 1. Создание массивов
# Одномерный массив
array_1d = np.array([1, 2, 3, 4, 5])
print("Одномерный массив:", array_1d)

# Двумерный массив (матрица)
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Двумерный массив:\n", array_2d)

# Создание массива нулей и единиц
zeros_array = np.zeros((2, 3))  # Массив 2x3 заполненный нулями
ones_array = np.ones((2, 3))     # Массив 2x3 заполненный единицами
print("Массив нулей:\n", zeros_array)
print("Массив единиц:\n", ones_array)

# 2. Выполнение математических операций с массивами
# Математические операции
array_a = np.array([1, 2, 3])
array_b = np.array([4, 5, 6])

# Сложение массивов
sum_array = array_a + array_b
print("Сумма массивов:", sum_array)

# Умножение на скаляр
scaled_array = array_a * 2
print("Умножение на скаляр:", scaled_array)

# Скалярное произведение двух массивов
dot_product = np.dot(array_a, array_b)
print("Скалярное произведение:", dot_product)

# 3. Изменение формы массива
reshaped_array = array_2d.reshape(3, 2)  # Изменение формы массива на 3x2
print("Измененный массив:\n", reshaped_array)

# 4. Применение функций для анализа данных
# Генерация случайных чисел и вычисление статистики
random_numbers = np.random.rand(1000)  # Генерация массива из 1000 случайных чисел от 0 до 1

# Среднее значение
mean_value = np.mean(random_numbers)
print("Среднее значение:", mean_value)

# Стандартное отклонение
std_deviation = np.std(random_numbers)
print("Стандартное отклонение:", std_deviation)

# Максимальное и минимальное значение
max_value = np.max(random_numbers)
min_value = np.min(random_numbers)
print("Максимальное значение:", max_value)
print("Минимальное значение:", min_value)


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