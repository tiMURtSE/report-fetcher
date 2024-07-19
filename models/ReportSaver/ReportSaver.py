import os
import datetime
from models.Query.Query import Query

class ReportSaver:
    def save(self, query: Query):
        file_name = self._create_file_name(query=query)
        file_path = os.path.join("отчеты", file_name)

        if query.report_content:
            with open(file_path, 'wb') as file:
                file.write(query.report_content)

            print(f"Файл успешно сохранен по расположению \"{file_path}\"")

    def _create_file_name(self, query: Query):
        formatted_query = "_".join(query.title.split(" "))
        time = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M")
        file_name = f"отчет_по_запросу_{formatted_query}_{time}.xlsx"

        return file_name