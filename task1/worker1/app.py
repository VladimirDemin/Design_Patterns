import os

# Каталог с исходными данными
data_dir = "/var/data"
# Файл для записи результата
result_file = "/var/result/data.txt"

# Получаем список файлов в каталоге
files = os.listdir(data_dir)

# Открываем файл для записи результата
with open(result_file, "w") as f:
    for file in files:
        # Считаем количество символов в имени файла
        line = f"{len(file)}\n"
        f.write(line)

print(f"Результат записан в {result_file}")
