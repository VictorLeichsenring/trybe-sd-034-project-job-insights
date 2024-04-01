from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        maiores_salarios = []
        for job in self.jobs_list:
            salario_string = job.get('max_salary')
            if salario_string and salario_string.isdigit():
                try:
                    maiores_salarios.append(int(salario_string))
                except ValueError:
                    continue
        maior_salario = max(maiores_salarios)
        return maior_salario

    def get_min_salary(self) -> int:
        pass

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
