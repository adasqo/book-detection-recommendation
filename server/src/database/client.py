
from elasticsearch import Elasticsearch
from datetime import datetime
import logging
from src.database.task_status import TaskStatus

from src.api.config import ComponentConfig

class ElasticsearchClient:

    logger = logging.getLogger()

    def __init__(self) -> None:
        self.config = ComponentConfig.build()
        self.client = Elasticsearch(
            host=self.config.address,
            port=self.config.port,
            http_auth=(self.config.user, self.config.password),
            scheme=self.config.scheme,
        )
        self.index = "task_index"
        self.__create_index()
        self.time_format = "%d/%m/%Y %H:%M:%S"

    def __create_index(self):
        request_body = {
            "settings" : {
                "number_of_shards": 2,
                "number_of_replicas": 1
            }
        }
        try:
            if not self.client.indices.exists(index=self.index):
                self.client.indices.create(index=self.index, body=request_body)
        except Exception as e:
            ElasticsearchClient.logger.error(f"Error while creating index: {e}")

    def create_task(self, task_id: str):

        body = {
            "task_id": task_id,
            "details": {},
            "lastUpdateDate": datetime.now().strftime(self.time_format),
            "status": TaskStatus.PROCESSING.value
        }
        try:
            self.client.index(index=self.index, body=body, id=task_id)
        except Exception as e:
            ElasticsearchClient.logger.error(f"Error while creating task: {e}")

    def update_task(self, task_id: str, details: dict, status: str = TaskStatus.PROCESSING.value):
        body = {
            "task_id": task_id,
            "details": details,
            "lastUpdateDate": datetime.now().strftime(self.time_format),
            "status": status
        }
        try:
            self.client.update(index=self.index, id=task_id, body={"doc": body})
        except Exception as e:
            ElasticsearchClient.logger.error(f"Error while updating task: {e}")

    def get_task(self, task_id: str):

        try:
            response = self.client.search(index=self.index, body={"query": {"match": {"task_id": task_id}}}, size='10000')
            return response["hits"]["hits"][0]['_source']
        except Exception as e:
            ElasticsearchClient.logger.error(f"Error while getting task: {e}")
            return {}

    def update_task_status(self, task_id: str, status: str):
        try:
            task = self.get_task(task_id)
            task["status"] = status
            task["lastUpdateDate"] = datetime.now().strftime(self.time_format)
            self.update_task(task_id, task["details"], status)
        except Exception as e:
            ElasticsearchClient.logger.error(f"Error while updating task's status: {e}")

    def get_all_tasks(self):
        try:
            response = self.client.search(index=self.index, body={"query": {"match_all": {}}}, size='10000')
            return response["hits"]["hits"]
        except Exception as e:
            # ElasticsearchClient.logger.error(f"No tasks detected")
            return []

    def delete_task(self, task_id: str):
        try:
            self.client.delete(index=self.index, id=task_id)
        except Exception as e:
            ElasticsearchClient.logger.error(f"Error while deleting task: {e}")

    def close(self):
        self.client.close()
