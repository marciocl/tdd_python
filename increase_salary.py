def increase_salary(increase: float, salary: int) -> float:
    return increase * salary


assert 150 == increase_salary(0.15, 1000)
