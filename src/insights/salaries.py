from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


def is_valid_number(value) -> bool:
    if isinstance(value, (int, str)):
        try:
            int(value)
            return True
        except ValueError:
            return False
    return False


def validate_salary_range(min_salary, max_salary):
    min_salary = int(min_salary)
    max_salary = int(max_salary)
    if min_salary > max_salary:
        raise ValueError("min_salary não pode ser maior que max_salary.")
    return min_salary, max_salary


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
        menores_salarios = []
        for job in self.jobs_list:
            salario_string = job.get('min_salary')
            if salario_string and salario_string.isdigit():
                try:
                    menores_salarios.append(int(salario_string))
                except ValueError:
                    continue
        menor_salario = min(menores_salarios)
        return menor_salario

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if 'min_salary' not in job or 'max_salary' not in job:
            raise ValueError("min_salary e max_salary são obrigatórios.")

        min_salary = job['min_salary']
        max_salary = job['max_salary']

        if job['min_salary'] is None or job['max_salary'] is None:
            raise ValueError('min_salary e max_salary não podem ser none')

        if not is_valid_number(min_salary) or not is_valid_number(max_salary):
            raise ValueError("min_salary e max_salary devem ser números.")

        min_salary, max_salary = validate_salary_range(min_salary, max_salary)
        if not is_valid_number(salary):
            raise ValueError("salary deve ser um número.")
        salary = int(salary)
        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
