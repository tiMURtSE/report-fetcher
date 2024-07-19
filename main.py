import time
from models.QueryFile.QueryFile import QueryFile
from models.StopWordsFile.StopWordsFile import StopWordsFile
from models.WordFormsGenerator.WordFormsGenerator import WordFormsGenerator
from models.RequestHandler.RequestHandler import RequestHandler
from models.Query.Query import Query
from models.ReportSaver.ReportSaver import ReportSaver
from basic_decor_library.SessionData import SessionData
from consts import SESSION_DATA_PATH

class Main:
    def __init__(self):
        self.query_file = QueryFile()
        self.stop_words_file = StopWordsFile()
        self.word_forms_generation = WordFormsGenerator()
        self.request_handler = RequestHandler()
        self.report_saver = ReportSaver()
        self.session_data = SessionData(SESSION_DATA_PATH)
        
    def run(self):
        # Этап №1
        initial_queries = self.query_file.get_initial_queries()
        stop_words = self.stop_words_file.get_stop_words()
        current_index = self.session_data.read_data()["value"]
        
        # Этап №2
        all_variations = []

        for query in initial_queries:
            variations = self.word_forms_generation.generate_variations(query)
            all_variations.extend(variations)
            
        all_variations.sort()

        # Этап №3
        queries = []
        start_pos = current_index + 1 if current_index else current_index
        print(f"Начальные индекс запроса: {start_pos}")
    
        for variation in all_variations[start_pos:]:
            query = Query(title=variation, stop_words=stop_words)
            queries.append(query)

        # Этап №4
        for index, query in enumerate(queries):
            print(f"\nТекущий индекс запроса: {start_pos + index}")

            if self.request_handler.check_results(query=query):
                print(f"У запроса \"{query.title}\" есть результаты")
                query.report_content = self.request_handler.get_report(query=query)
                self.report_saver.save(query=query)
            else:
                print(f"По запросу \"{query.title}\" нет результатов")

            self.session_data.write_data(value=start_pos + index)

        self.session_data.write_data(value=0)
                
app = Main()
app.run()