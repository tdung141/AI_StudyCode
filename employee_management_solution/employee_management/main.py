from exceptions.employee_exceptions import (
    DuplicateEmployeeError,
    EmployeeException,
    EmployeeNotFoundError,
    InvalidAgeError,
    InvalidSalaryError,
    ProjectAllocationError,
)
from models.developer import Developer
from models.intern import Intern
from models.manager import Manager
from services.company import Company
from services.payroll import (
    average_projects_per_employee,
    count_by_role,
    salary_by_department,
    top_paid_employees,
    total_company_salary,
)
from utils.formatters import print_employee_table
from utils.validators import (
    read_float,
    read_int,
    validate_age,
    validate_email,
    validate_performance,
    validate_salary,
)


def pause():
    input("\nNhấn Enter để tiếp tục...")


def print_header(company):
    print("\n" + "=" * 70)
    print(f"{'HỆ THỐNG QUẢN LÝ NHÂN VIÊN ' + company.name:^70}")
    print("=" * 70)


def print_main_menu():
    print("1. Thêm nhân viên mới")
    print("2. Hiển thị danh sách nhân viên")
    print("3. Tìm kiếm nhân viên")
    print("4. Quản lý lương")
    print("5. Quản lý dự án")
    print("6. Đánh giá hiệu suất")
    print("7. Quản lý nhân sự")
    print("8. Thống kê báo cáo")
    print("9. Thoát")


def collect_common_info():
    employee_id = input("Mã nhân viên: ").strip()
    name = input("Họ tên: ").strip()

    while True:
        try:
            age = validate_age(read_int("Tuổi: "))
            break
        except InvalidAgeError as exc:
            print(exc)

    while True:
        try:
            email = validate_email(input("Email: ").strip())
            break
        except ValueError as exc:
            print(exc)

    department = input("Phòng ban: ").strip()

    while True:
        try:
            base_salary = validate_salary(read_float("Lương cơ bản: "))
            break
        except InvalidSalaryError as exc:
            print(exc)

    return employee_id, name, age, email, department, base_salary


def add_employee_menu(company):
    print("\n1. Thêm Manager\n2. Thêm Developer\n3. Thêm Intern")
    choice = input("Chọn loại: ").strip()
    try:
        common = collect_common_info()
        if choice == "1":
            team_size = read_int("Số lượng thành viên quản lý: ")
            employee = Manager(*common, team_size=team_size)
        elif choice == "2":
            languages = [lang.strip() for lang in input("Ngôn ngữ lập trình (cách nhau bởi dấu phẩy): ").split(",") if lang.strip()]
            employee = Developer(*common, programming_languages=languages)
        elif choice == "3":
            mentor_name = input("Tên mentor: ").strip()
            employee = Intern(*common, mentor_name=mentor_name)
        else:
            print("Lựa chọn không hợp lệ.")
            return

        try:
            company.add_employee(employee)
            print("Đã thêm nhân viên thành công.")
        except DuplicateEmployeeError:
            employee = company.add_employee_safe(employee)
            print(f"ID bị trùng. Hệ thống đã tự sinh ID mới: {employee.employee_id}")
    except EmployeeException as exc:
        print(f"Lỗi: {exc}")


def display_employee_menu(company):
    print("\n1. Tất cả nhân viên\n2. Theo loại\n3. Theo hiệu suất (cao đến thấp)")
    choice = input("Chọn: ").strip()
    employees = []
    if choice == "1":
        employees = company.get_all()
    elif choice == "2":
        role = input("Nhập loại (Manager/Developer/Intern): ")
        employees = company.get_by_role(role)
    elif choice == "3":
        employees = company.sort_by_performance()
    else:
        print("Lựa chọn không hợp lệ.")
        return

    if not employees:
        print("Chưa có dữ liệu.")
        return
    print_employee_table(employees)


def search_employee_menu(company):
    print("\n1. Theo ID\n2. Theo tên\n3. Theo ngôn ngữ lập trình")
    choice = input("Chọn: ").strip()
    try:
        if choice == "1":
            emp = company.find_by_id(input("Nhập ID: ").strip())
            print_employee_table([emp])
        elif choice == "2":
            items = company.find_by_name(input("Nhập tên: ").strip())
            if not items:
                print("Không tìm thấy kết quả.")
            else:
                print_employee_table(items)
        elif choice == "3":
            items = company.find_developer_by_language(input("Nhập ngôn ngữ: ").strip())
            if not items:
                print("Không tìm thấy developer phù hợp.")
            else:
                print_employee_table(items)
        else:
            print("Lựa chọn không hợp lệ.")
    except EmployeeNotFoundError as exc:
        print(exc)


def payroll_menu(company):
    employees = company.get_all()
    if not employees:
        print("Chưa có dữ liệu.")
        return
    print("\n1. Tính lương cho từng nhân viên\n2. Tính tổng lương công ty\n3. Top 3 nhân viên lương cao nhất")
    choice = input("Chọn: ").strip()
    if choice == "1":
        for emp in employees:
            print(f"{emp.employee_id} - {emp.name} - {emp.get_role()}: {emp.calculate_salary():,.0f} VND")
    elif choice == "2":
        print(f"Tổng lương công ty: {total_company_salary(employees):,.0f} VND")
    elif choice == "3":
        for idx, emp in enumerate(top_paid_employees(employees), start=1):
            print(f"Top {idx}: {emp.name} ({emp.get_role()}) - {emp.calculate_salary():,.0f} VND")
    else:
        print("Lựa chọn không hợp lệ.")


def project_menu(company):
    print("\n1. Phân công dự án\n2. Xóa nhân viên khỏi dự án\n3. Hiển thị dự án của 1 nhân viên")
    choice = input("Chọn: ").strip()
    try:
        employee_id = input("Nhập ID nhân viên: ").strip()
        if choice == "1":
            company.assign_project(employee_id, input("Tên dự án: ").strip())
            print("Phân công dự án thành công.")
        elif choice == "2":
            company.remove_project(employee_id, input("Tên dự án: ").strip())
            print("Đã xóa nhân viên khỏi dự án.")
        elif choice == "3":
            emp = company.find_by_id(employee_id)
            print(f"Danh sách dự án của {emp.name}: {', '.join(emp.projects) if emp.projects else 'Chưa có'}")
        else:
            print("Lựa chọn không hợp lệ.")
    except (EmployeeNotFoundError, ProjectAllocationError) as exc:
        print(exc)


def performance_menu(company):
    print("\n1. Cập nhật điểm hiệu suất\n2. Hiển thị nhân viên xuất sắc (>8)\n3. Hiển thị nhân viên cần cải thiện (<5)")
    choice = input("Chọn: ").strip()
    try:
        if choice == "1":
            employee_id = input("ID nhân viên: ").strip()
            score = validate_performance(read_float("Điểm hiệu suất: "))
            company.update_performance(employee_id, score)
            print("Cập nhật thành công.")
        elif choice == "2":
            items = company.excellent_employees()
            print_employee_table(items) if items else print("Không có nhân viên xuất sắc.")
        elif choice == "3":
            items = company.employees_need_improvement()
            print_employee_table(items) if items else print("Không có nhân viên cần cải thiện.")
        else:
            print("Lựa chọn không hợp lệ.")
    except (EmployeeNotFoundError, ValueError) as exc:
        print(exc)


def hr_menu(company):
    print("\n1. Xóa nhân viên\n2. Tăng lương cơ bản\n3. Thăng chức")
    choice = input("Chọn: ").strip()
    try:
        employee_id = input("ID nhân viên: ").strip()
        if choice == "1":
            removed = company.remove_employee(employee_id)
            print(f"Đã xóa nhân viên {removed.name}.")
        elif choice == "2":
            amount = validate_salary(read_float("Số tiền tăng thêm: "))
            updated = company.increase_base_salary(employee_id, amount)
            print(f"Lương cơ bản mới của {updated.name}: {updated.base_salary:,.0f} VND")
        elif choice == "3":
            promoted = company.promote_employee(employee_id)
            print(f"Đã thăng chức. Chức vụ mới: {promoted.get_role()}")
        else:
            print("Lựa chọn không hợp lệ.")
    except (EmployeeNotFoundError, ValueError, InvalidSalaryError) as exc:
        print(exc)


def report_menu(company):
    employees = company.get_all()
    if not employees:
        print("Chưa có dữ liệu.")
        return

    print("\n1. Số lượng nhân viên theo loại\n2. Tổng lương theo phòng ban\n3. Số dự án trung bình trên mỗi nhân viên")
    choice = input("Chọn: ").strip()
    if choice == "1":
        for role, count in count_by_role(employees).items():
            print(f"{role}: {count}")
    elif choice == "2":
        for dept, total in salary_by_department(employees).items():
            print(f"{dept}: {total:,.0f} VND")
    elif choice == "3":
        print(f"Số dự án trung bình/nhân viên: {average_projects_per_employee(employees):.2f}")
    else:
        print("Lựa chọn không hợp lệ.")


def main():
    company = Company("CÔNG TY ABC")
    company.seed_sample_data()

    while True:
        print_header(company)
        print_main_menu()
        choice = input("\nChọn chức năng (1-9): ").strip()

        if choice == "1":
            add_employee_menu(company)
        elif choice == "2":
            display_employee_menu(company)
        elif choice == "3":
            search_employee_menu(company)
        elif choice == "4":
            payroll_menu(company)
        elif choice == "5":
            project_menu(company)
        elif choice == "6":
            performance_menu(company)
        elif choice == "7":
            hr_menu(company)
        elif choice == "8":
            report_menu(company)
        elif choice == "9":
            print("Tạm biệt!")
            break
        else:
            print("Vui lòng chọn số từ 1 đến 9.")
        pause()


if __name__ == "__main__":
    main()
