from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        unicas = set()

        for job in self.jobs_list:
            industria = job.get('industry')
            if industria:
                unicas.add(industria)

        return list(unicas)
