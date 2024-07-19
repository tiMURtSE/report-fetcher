from basic_decor_library.Workbook import Workbook

class QueryFile(Workbook):
    def __init__(self):
        super().__init__()

    def get_initial_queries(self):
        """Возвращает только запросы c начальной формой."""
        raw_data = self.get_data()
        queries = []

        for row in raw_data.iter_rows(min_row=2, min_col=1, max_col=1):
            query = row[0].value
            queries.append(query)

        return queries
    
    def _input_file_path(self, printed_value=None):
        printed_value = "Выберите файл с запросами: "
        return super()._input_file_path(printed_value)

