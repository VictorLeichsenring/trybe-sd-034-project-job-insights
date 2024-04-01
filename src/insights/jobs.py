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

    def job_key_verify(self, job, criteria):
        for key, value in criteria.items():
            if job.get(key) != value:
                return False
        return True

    def filter_by_multiple_criteria(self, jobs, filter_criteria) -> List[dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("filter_criteria must be a dictionary")

        filtered_jobs = []
        for job in jobs:
            if self.job_key_verify(job, filter_criteria):
                filtered_jobs.append(job)
        return filtered_jobs
