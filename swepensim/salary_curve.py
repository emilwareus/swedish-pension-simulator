from abc import ABC, abstractmethod


class SalaryCurve(ABC):
    """
    This class is used to calculate the salary curve.
    """

    def __intit__(self, current_age, target_pension_age, current_salary, expected_max_salary, inflation):
        self.current_age = current_age
        self.target_pension_age = target_pension_age
        self.current_salary = current_salary
        self.expected_max_salary = expected_max_salary
        self.inflation = inflation

        if self.current_age > self.target_pension_age:
            raise ValueError("Current age is greater than target pension age")
        
        if self.inflation < 0 or self.inflation > 1:
            raise ValueError("Inflation must be between 0 and 1")
        
        if self.current_salary < 0:
            raise ValueError("Current salary must be greater than 0")
        
        if self.expected_max_salary < 0:
            raise ValueError("Expected max salary must be greater than 0")
        

    @abstractmethod
    def get_salary_curve(self) -> list[int]:
        raise NotImplementedError


class LinearSalaryCurve(SalaryCurve):
    """
    Implements a linear salary curve (same increase each year), and adjusts the curve for inflation. 
    """

    def __intit__(self, current_age, target_pension_age, current_salary, expected_max_salary, inflation):
        super().__init__(current_age, target_pension_age, current_salary, expected_max_salary, inflation)

    def get_salary_curve(self) -> list[int]:
        salary_diff = self.expected_max_salary - self.current_salary
        yearly_increase = salary_diff / (self.target_pension_age - self.current_age)
        infl = self.inflation + 1
        salary_curve = [(self.current_salary + yearly_increase * i) * (infl**i) for i in range(self.target_pension_age - self.current_age)]

        return salary_curve    