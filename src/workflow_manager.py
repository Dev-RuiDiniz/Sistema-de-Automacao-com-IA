import psycopg2
from datetime import datetime

class WorkflowManager:
    def __init__(self, db_config):
        self.db_config = db_config
        self.conn = None