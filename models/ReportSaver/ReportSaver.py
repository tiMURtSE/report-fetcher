import os
import sys
import datetime
from models.Query.Query import Query
from tkinter import filedialog
from basic_decor_library.Workbook import Workbook

class ReportSaver:
    def __init__(self):
        self._directory_path = self._input_directory_path()

    def save(self, query: Query):
        file_name = self._create_file_name(query=query)
        file_path = os.path.join(self._directory_path, file_name)

        if query.report_content:
            with open(file_path, 'wb') as file:
                file.write(query.report_content)

            print(f"Файл успешно сохранен по расположению \"{file_path}\"")

    def _create_file_name(self, query: Query):
        formatted_query = "_".join(query.title.split(" "))
        time = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")
        file_name = f"отчет_по_запросу_{formatted_query}_{time}.xlsx"

        return file_name
    
    def _input_directory_path(self):
        print("Выберите папку для вывода результатов: ")

        directory_path = filedialog.askdirectory()

        if not directory_path:
            print("Папка не была выбрана")
            sys.exit()
        else:
            print(os.path.basename(directory_path))
            return directory_path