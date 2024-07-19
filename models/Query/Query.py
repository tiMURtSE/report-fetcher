import urllib.parse
from consts import BASE_URL, PARAMS

class Query:
    def __init__(self, title: str, stop_words: list[str]):
        self.title = title
        self.stop_words = stop_words
        self.generated_url = self._generate_url()
        self.file_url = None
        self.report_content = None
        self.has_results = None

    def _generate_url(self):
        """Генерирует URL, в котором добавлены параметры для стоп-слов."""
        params = PARAMS
        params["query"] = self.title
        params["excludedWords"] = self.stop_words

        encoded_params = "&".join(f"excludedWords={urllib.parse.quote(word)}" for word in params["excludedWords"])
        del params["excludedWords"]

        encoded_url = f"{BASE_URL}?{urllib.parse.urlencode(params)}&{encoded_params}"

        return encoded_url
    