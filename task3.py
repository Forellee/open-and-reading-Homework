def merge_files(file_list, output_file):
    files_data = []

    # Считываем данные из файлов
    for file_name in file_list:
        with open(file_name, encoding='utf-8') as f:
            lines = f.readlines()
            files_data.append((file_name, len(lines), lines))

    # Сортируем по количеству строк
    files_data.sort(key=lambda x: x[1])

    # Записываем в итоговый файл
    with open(output_file, 'w', encoding='utf-8') as result:
        for file_name, line_count, lines in files_data:
            result.write(f"{file_name}\n")
            result.write(f"{line_count}\n")
            result.writelines(lines)
            result.write("\n")  # добавим пустую строку между блоками (по желанию)

if __name__ == '__main__':
    input_files = ['1.txt', '2.txt', '3.txt']  # здесь укажи нужные файлы
    merge_files(input_files, 'result.txt')
