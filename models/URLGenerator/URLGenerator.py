import urllib.parse

class URLGenerator:
    BASE_URL = "https://webmaster.yandex.ru/site/https:basicdecor.ru:443/wordcraft/"

    def generate_url(self, query: str, stop_words: list[str]):
        """Генерирует URL, в котором добавлены параметры для стоп-слов."""
        params = {"device": "ALL_DEVICES", "userQueries": "SITES", "rivals": "GENERAL", "tab": "GENERAL", "regions": "1"}
        params["query"] = query
        params["excludedWords"] = stop_words

        encoded_params = "&".join(f"excludedWords={urllib.parse.quote(word)}" for word in params["excludedWords"])
        del params["excludedWords"]

        encoded_url = f"{self.BASE_URL}?{urllib.parse.urlencode(params)}&{encoded_params}"

        return encoded_url
