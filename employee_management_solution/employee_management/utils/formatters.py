def format_employee_row(employee):
    return (
        f"{employee.employee_id:<8} | {employee.name:<20} | {employee.get_role():<10} | "
        f"{employee.department:<12} | {employee.base_salary:>12,.0f} | "
        f"{employee.performance_score:^5.1f} | {len(employee.projects):^3}"
    )


def print_employee_table(employees):
    print("-" * 90)
    print(
        f"{'ID':<8} | {'Tên':<20} | {'Loại':<10} | {'Phòng ban':<12} | "
        f"{'Lương cơ bản':>12} | {'ĐG':^5} | {'DA':^3}"
    )
    print("-" * 90)
    for employee in employees:
        print(format_employee_row(employee))
    print("-" * 90)
