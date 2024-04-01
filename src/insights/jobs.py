import csv
from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            self.jobs_list = list(csv_reader)

    def get_unique_job_types(self) -> List[str]:
        job_types = set()
        for job in self.jobs_list:
            job_type = job.get('job_type')
            job_types.add(job_type)
        return list(job_types)

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
