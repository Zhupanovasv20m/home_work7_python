import os

def rename_files(desired_name, number_length, extension):
    # Проверяем, что количество цифр в порядковом номере больше 0
    if number_length <= 0:
        print("Количество цифр в порядковом номере должно быть больше 0")
        return

    # Получаем список всех файлов в текущем каталоге
    files = os.listdir()

    # Проходим по каждому файлу в списке
    for i, file in enumerate(files):
        # Проверяем, является ли файл нужного расширения
        if file.endswith(extension):
            # Генерируем порядковый номер с нужным количеством цифр
            number = str(i + 1).zfill(number_length)
            # Формируем новое имя файла
            new_name = f"{desired_name}_{number}.{extension}"
            # Переименовываем файл
            os.rename(file, new_name)

rename_files("rtr.txt", 3, "txt")