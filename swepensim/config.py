from swepensim.salary_curve import LinearSalaryCurve
from dataclasses import dataclass

## Terminology
# TP: tjänstepension
# AP: Allmän pension
# PP: Privat pension


@dataclass
class SimulationConfig:
    """Configures the simulation"""

    ##### Non-optional configurations

    # Age
    current_age: int

    # Current saved pension
    current_tp: int
    current_ap: int
    current_pp: int 

    # Salary
    current_salary: int
    expected_max_salary: int # Non-inflation adjusted expected max salary in your life (What is the average salary at age ~55-60 in your profession?)

    # Savings rate
    tp_rate: float # TP rate, 0 <= tp_rate <= 1. 0.05 is 5% and noraml. 
    pp_rate: float # PP rate, 0 <= pp_rate

    # Return rates, yearly
    tp_return_rate: float # TP return rate
    pp_return_rate: float # PP return rate
    ap_return_rate: float # AP return rate

    ##### Optional configurations

    # Age configurations
    target_pension_age: int = 65

    # Financial configurations
    ap_cutoff_monthly_salary: int = 45000 # This is where your salary stops contribute to the AP
    inflation: float = 0.02
    salary_curve = LinearSalaryCurve
    target_pension_share_of_end_salary: float = 0.8 # What share/percentage of your max salary do you want to save for your pension?
    
