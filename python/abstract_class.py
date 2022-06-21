from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Employee(ABC):
    name: str
    role: str

    @abstractmethod
    def pay(self) -> None:
        """Pay method abstracted from child class"""


@dataclass
class SalaryEmployee(Employee):
    monthly_salary: float = 5000

    def pay(self) -> None:
        print(f'Paying {self.name} monthly salary of ${self.monthly_salary}')


@dataclass
class WageEmployee(Employee):
    hourly_wage: float = 25
    hours_worked_daily: int = 8
    days_works_weekly: int = 4

    def pay(self):
        print(
            f'Paying {self.name} weekly pay of ${(self.hourly_wage * self.hours_worked_daily) * self.days_works_weekly}')


def main():
    employee_one = SalaryEmployee(name='John', role='President')
    employee_two = WageEmployee(name='Michael', role='Tradesmen')
    employee_one.pay()
    employee_two.pay()


main()
