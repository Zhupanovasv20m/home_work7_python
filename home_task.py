# Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] 
# берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. 
# Далее счётчик файлов и расширение.


from pathlib import Path

# our_path = Path(r'C:\Users\leito\Desktop\ww\home_work_7')


def group_rename (new_name: str, ext_renamed: str, expansion_file: str = None,
                       saved_range: range = (3, 6)) -> int:
    if expansion_file is None: 
        expansion_file = ext_renamed
    # our_path= Path.cwd() if path is None else Path(path)
    our_path=Path(r'C:\Users\leito\Desktop\ww\home_work_7')
    count = 0
    for p in our_path.iterdir():
        if p.is_file() and p.suffix == ext_renamed:
            new_file_name = f"{p.stem[saved_range[0]:saved_range[1]]}{new_name}{count:03}{expansion_file}"
            p.rename(Path(p.parent,  new_file_name))
            count += 1
    return count


group_rename("exa", ".doc")