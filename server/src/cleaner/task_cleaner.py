from datetime import datetime
import logging
from threading import Thread
from time import sleep
import os

from src.database.client import ElasticsearchClient


class TaskCleaner(Thread):

    _logger = logging.getLogger(__name__)
    processing = False

    def __init__(self, client: ElasticsearchClient):
        super().__init__()
        self.processing = True
        self.client = client
        self.heartbeat = 500
        self.time_format = "%d/%m/%Y %H:%M:%S"

    def run(self):
        while self.processing:
            try:
                tasks = self.client.get_all_tasks()
                if tasks is None:
                    sleep(self.heartbeat)
                for i in range(len(tasks)):
                    task_id, task = tasks[i]["_id"], tasks[i]["_source"]
                    last_heartbeat_tick = (datetime.now() - datetime.strptime(task["lastUpdateDate"], self.time_format)).total_seconds()
                    if last_heartbeat_tick > self.heartbeat :
                        try:
                            self.client.delete_task(task_id)
                            self.cleanup(f"./server/images/{task_id}.jpg")
                            self._logger.info(f"Deleted task: {task_id}.")
                        except:
                            pass
            except Exception as exc:
                self._logger.warning(f'Unknown task heartbeat error: {exc}')
            sleep(self.heartbeat)
        self.client.close()

    def cleanup(self, image_path: str):
        os.remove(image_path)
