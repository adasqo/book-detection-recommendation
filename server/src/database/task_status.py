from enum import Enum, auto


class TaskStatus(Enum):
    PROCESSING = "processing"
    FINISHED = "finished"
    FAILED = "failed"
