import time
import requests
from requests import Response
from models.Query.Query import Query
from consts import REPORT_URL, HEADERS, REQUEST_DATA

# Поменять название класса
class RequestHandler:
    def __init__(self):
        pass

    def check_results(self, query: Query):
        """Проверяет на сайта webmaster.yandex.ru, есть ли выдача результатов при получаемом запросе. Определяет, следует ли скачивать отчет по такому запросу."""
        response = requests.get(url=query.generated_url, headers=HEADERS)

        if response.status_code == 200:
            return self._has_results_in_markup(response=response)
        else:
            raise Exception(f"Произошла ошибка при запросе результатов отчета. Статус-код: {response.status_code}")

    def get_report(self, query: Query):
        """Возвращает отчет в виде содержимого для файла (в байтах)."""
        retries = 5
        attempt = 0

        while attempt < retries:
            download_info = self._get_download_info(query=query)
            status = download_info["downloadStatus"]

            if status == "DONE":
                print(f"Статус загрузки: {status}")
                report_url = self._extract_report_url(download_info)
                return self._download_report(report_url=report_url)
            
            attempt += 1
            time.sleep(5)
            print(f"Статус загрузки: {status}")

    def _download_report(self, report_url: str):
        file_response = requests.get(report_url)
        
        if file_response.status_code == 200:
            return file_response.content
        else:
            raise Exception(f"Ошибка при скачивании файла: {file_response.status_code}")

    def _get_download_info(self, query: Query):
        request_data = self._extend_request_data(query=query)
        response = requests.post(url=REPORT_URL, headers=HEADERS, data=request_data)

        if response.status_code != 200:
            raise Exception(f"Ответ от сервера при отправки запроса на получения ссылки отчета: {response.status_code}")

        download_info = response.json().get("response")["downloadInfo"]
        
        return download_info
    
    def _extend_request_data(self, query: Query):
        request_data = REQUEST_DATA
        request_data["params[parentUrl]"] = query.generated_url
        request_data["params[filters][query]"] = query.title

        for word in query.stop_words:
            request_data[f"params[filters][excludedWords][]"] = word

        return request_data
    
    def _has_results_in_markup(self, response: Response):
        return (
            "clicks" in str(response.content) and
            "demand" in str(response.content) and
            "competitiveness" in str(response.content)
        )
    
    def _extract_report_url(self, download_info: dict):
        report_url = download_info["publicUrlMds"]
        return report_url