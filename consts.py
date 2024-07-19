SESSION_DATA_PATH = "./session_data.json"

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

# URL, на который идет запрос для получения ссылки на скачивание отчета
REPORT_URL = "https://webmaster.yandex.ru/gate/wordcraft/download/"

BASE_URL = "https://webmaster.yandex.ru/site/https:basicdecor.ru:443/wordcraft/"

# Параметры для генерации URL
PARAMS = {"device": "ALL_DEVICES", "userQueries": "SITES", "rivals": "GENERAL", "tab": "GENERAL", "regions": "1"}

COOKIES = "yandexuid=2368105821693897235; yuidss=2368105821693897235; ymex=2009257237.yrts.1693897237; gdpr=0; _ym_uid=1693897237239904244; yandex_login=t.tsedzhinov@basicdecor.ru; yashr=8571936461697812291; L=c19ceEFUWQFHe1Z5QHBKD0JmdQ1ZVAUGABdEKQ0sHiFeCjofDywlARw6UC8yF0ZpMww=.1697812837.15501.380414.23c30b81cdb6a67f8574eafd7639f5a1; font_loaded=YSv1; amcuid=721451111703743824; receive-cookie-deprecation=1; yandex_gid=213; my=YysEgNWERjgrAA==; gpb=yandex_gid.213#ygo.1094%3A213#ygu.0; _ym_d=1716531228; yp=1735607048.szm.1:1920x1080:1920x953; yabs-vdrf=BHt1cPm0L-HW10; i=a+ui0jLDAydydGYy339vIzsFA+JB/+q9pG7ACN37J74OvoJOcxDRDw5h+zUy58z/PJYEfxqe6sXuJUuB0pQbgxClBLA=; Session_id=3:1721289131.5.0.1697812837381:bqWsVQ:59.1.2:1|1130000064888744.0.2.3:1697812837|3:10291671.990721.wy1idHSPhydQD3Zi09BEipSUvuA; sessar=1.1192.CiBGFIdV6OW66IQ6v4IJpBLkwme9MDUbw0fUwD9rwQ6DCw.a3_qeJ-kXD_VR20cbFyOPIML1ABiyZ1Gfdd1oEdRwAI; sessionid2=3:1721289131.5.0.1697812837381:bqWsVQ:59.1.2:1|1130000064888744.0.2.3:1697812837|3:10291671.990721.fakesign0000000000000000000; _ym_isad=2; is_gdpr=0; is_gdpr_b=CO6pNRChiAIoAg==; cycada=1HudQT3igBBxu3E75rPKxSahdzxQIbGvZxSV8KE9cYU=; _yasc=Zk9+nkape+chrxWBkkCsg1XmOGHMDfyK+FeE/iFKc7q/K53AHeJn+B3AHuhlmVViv+vlB5xkVg/FaGg4g1NCcv3eSsCyI+M=; _ym_visorc=b; bh=EkAiTm90L0EpQnJhbmQiO3Y9IjgiLCAiQ2hyb21pdW0iO3Y9IjEyNiIsICJHb29nbGUgQ2hyb21lIjt2PSIxMjYiGgUieDg2IiIQIjEyNC4wLjYzNjcuMjA3IioCPzAyAiIiOgkiV2luZG93cyJCCCIxMC4wLjAiSgQiNjQiUl0iQ2hyb21pdW0iO3Y9IjEyNC4wLjYzNjcuMjA3IiwgIkdvb2dsZSBDaHJvbWUiO3Y9IjEyNC4wLjYzNjcuMjA3IiwgIk5vdC1BLkJyYW5kIjt2PSI5OS4wLjAuMCJaAj8wYKS+6LQG"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": COOKIES,
    "Host": "webmaster.yandex.ru",
    "Referer": "https://webmaster.yandex.ru/site/https:basicdecor.ru:443/tools/microtest/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "sec-ch-ua": '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

REQUEST_DATA = {
    "params[balancerParentRequestId]": "1720533590804796-17903470026661820058",
    "params[hostId]": "https:basicdecor.ru:443",
    "params[exportFormat]": "excel",
    "params[filters][device]": "ALL_DEVICES",
    "params[filters][regions][]": "1",
    "params[filters][userQueries]": "SITES",
    "params[filters][rivals]": "GENERAL",
    "crc": "df207d8e275de381b7073c7548f4b8ea5e1d4b75:1721376505142",
}
