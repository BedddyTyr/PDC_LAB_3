from concurrent.futures import ProcessPoolExecutor

# Deduction rates
SSS_RATE = 0.045
PHILHEALTH_RATE = 0.025
PAGIBIG_RATE = 0.02
TAX_RATE = 0.10

# Given employees
employees = [
    ("Alice", 25000),
    ("Bob", 32000),
    ("Charlie", 28000),
    ("Diana", 40000),
    ("Edward", 35000)
]

# Single payroll computation function (Data Parallelism)
def compute_payroll(employee):
    name, salary = employee

    # Individual deductions
    sss = salary * SSS_RATE
    philhealth = salary * PHILHEALTH_RATE
    pagibig = salary * PAGIBIG_RATE
    tax = salary * TAX_RATE

    # Total deduction
    total_deduction = sss + philhealth + pagibig + tax

    # Net salary
    net_salary = salary - total_deduction

    return name, salary, total_deduction, net_salary


# Main multiprocessing execution
if __name__ == "__main__":

    with ProcessPoolExecutor() as executor:

        results = executor.map(compute_payroll, employees)

        for name, gross, total_deduction, net in results:

            print(f"\nEmployee: {name}")
            print(f"Gross Salary: ₱{gross:,.2f}")
            print(f"Total Deduction: ₱{total_deduction:,.2f}")
            print(f"Net Salary: ₱{net:,.2f}")