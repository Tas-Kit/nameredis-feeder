import os
from py2neo import Database, NodeMatcher
from src import Feeder


class FeedTaskname(Feeder):

    @staticmethod
    def build_connector():
        params = {
            'host': os.getenv('TASK_DB_HOST', 'taskdb'),
            'port': int(os.getenv('TASK_DB_PORT', 7687)),
            'user': os.getenv('TASK_DB_USER', 'neo4j'),
            'password': os.getenv('TASK_DB_PASSWORD', 'neo4jpass'),
            'scheme': os.getenv('TASK_DB_SCHEME', 'bolt')
        }
        try:
            db = Database(**params)
            graph = db.default_graph
            matcher = NodeMatcher(graph)
            return matcher
        except Exception as e:
            print('Unable to connect to task db.', str(e))

    @staticmethod
    def get_data(conn):
        data = {}
        try:
            result = conn.match('StepInst')
            for item in result:
                data[item['sid']] = item['name']
            result = conn.match('TaskInst')
            for item in result:
                data[item['tid']] = item['name']
        except Exception as e:
            print(e.pgerror)
        return data
