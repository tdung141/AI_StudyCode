# Employee Management System

Bài giải Python cho đề tài **Xây dựng Hệ thống quản lý nhân viên công ty**.

## Cấu trúc
- `main.py`: menu chương trình chính
- `models/`: các lớp `Employee`, `Manager`, `Developer`, `Intern`
- `services/`: xử lý nghiệp vụ công ty và bảng lương
- `utils/`: kiểm tra dữ liệu đầu vào, định dạng hiển thị
- `exceptions/`: custom exceptions

## Chức năng đã làm
- Thêm nhân viên theo 3 loại: Manager, Developer, Intern
- Hiển thị danh sách nhân viên, lọc theo loại, sắp xếp theo hiệu suất
- Tìm kiếm theo ID, tên, ngôn ngữ lập trình
- Tính lương từng nhân viên, tổng lương công ty, top lương cao
- Phân công/xóa dự án, giới hạn tối đa 5 dự án/nhân viên
- Cập nhật hiệu suất, lọc nhân viên xuất sắc và cần cải thiện
- Xóa nhân viên, tăng lương cơ bản, thăng chức
- Thống kê số lượng theo loại, tổng lương theo phòng ban, số dự án trung bình
- Xử lý ngoại lệ đúng theo mô tả đề

## Chạy chương trình
```bash
cd employee_management
python main.py
```

## Ghi chú
Chương trình đã có dữ liệu mẫu để test nhanh khi khởi động.
