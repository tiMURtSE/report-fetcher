from basic_decor_library.Workbook import Workbook

class StopWordsFile(Workbook):
    def __init__(self):
        super().__init__()

    def get_stop_words(self):
        """Возвращает список стоп-слов."""
        raw_data = self.get_data()
        stop_words = []

        for row in raw_data.iter_rows(min_row=2, min_col=1, max_col=1):
            stop_word = str(row[0].value)
            stop_words.append(stop_word)

        return stop_words

    def _input_file_path(self, printed_value=None):
        printed_value = "Выберите файл со стоп-словами: "
        return super()._input_file_path(printed_value)