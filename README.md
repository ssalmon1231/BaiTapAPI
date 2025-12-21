# 🐾 Pet Detection Engine

![Python](https://img.shields.io/badge/Python-3.10-yellow)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15.0-orange)
![Flask](https://img.shields.io/badge/Backend-Flask-green)

> **Hệ thống nhận diện thú cưng (Chó/Mèo) trên nền tảng Web.**

## 1. Giới thiệu (Introduction)

**Pet Detection Engine** là ứng dụng web sử dụng Deep Learning để tự động phát hiện, phân loại và khoanh vùng thú cưng trong hình ảnh. Dự án tích hợp mô hình CNN đã huấn luyện sẵn với Backend Flask để cung cấp giao diện người dùng trực quan, dễ sử dụng.

⚠️ **YÊU CẦU BẮT BUỘC:** Dự án này được thiết kế đặc biệt để chạy trên **Python 3.10**. Việc sử dụng các phiên bản Python mới hơn (3.12, 3.13) sẽ gây ra lỗi không tương thích với thư viện TensorFlow 2.15.

## 2. Tính năng (Features)

* **Giao diện Web:** Upload ảnh và xem kết quả trực quan trên trình duyệt.
* **AI Detection:** Tự động vẽ khung (Bounding Box) quanh vật thể.
* **Phân loại:** Xác định nhãn **Dog** (Chó) hoặc **Cat** (Mèo) kèm độ tin cậy.

## 3. Cấu trúc dự án (Project Structure)

```text
Pet-Detection-Engine/
├── templates/          # Giao diện HTML
│   ├── index.html      # Trang chủ (Upload file)
│   └── result.html     # Trang hiển thị kết quả
├── static/             # Chứa CSS, JS, ảnh upload
├── app.py              # File chạy Server (Flask)
├── model.h5            # File model AI (Pre-trained)
├── requirements.txt    # Danh sách thư viện (Strict version)
└── README.md           # Tài liệu hướng dẫn
```
# ⚙️ Hướng dẫn Cài đặt (Installation Instructions)

Vui lòng thực hiện tuần tự các bước sau để đảm bảo chương trình chạy ổn định.

### Bước 1: Clone dự án

```bash
git clone [https://github.com/khoidesu/Pet-Detection-Engine.git](https://github.com/khoidesu/Pet-Detection-Engine.git)
cd Pet-Detection-Engine
```
## Bước 2: Tạo môi trường ảo (Virtual Environment)

**Bắt buộc dùng Python 3.10**. Nếu máy bạn có nhiều phiên bản Python, hãy trỏ chính xác vào bản 3.10.

```bash
# Windows
py -3.10 -m venv venv
# Hoặc:
python -m venv venv

# Mac/Linux
python3.10 -m venv venv
```
## Bước 3: Kích hoạt môi trường

```bash
# Windows
.\venv\Scripts\activate

# MacOS/Linux
source venv/bin/activate
```
## Bước 4: Cài đặt thư viện

Chạy lệnh sau để cài đặt các gói phụ thuộc từ file cấu hình:

```bash
pip install -r requirements.txt
```
## 5. Hướng dẫn Sử dụng (Usage)

### Khởi chạy Server
Tại terminal (đảm bảo đang kích hoạt `venv`), chạy lệnh sau:

```bash
python app.py
Khi server chạy thành công, terminal sẽ hiện thông báo:
```text
Running on [http://127.0.0.1:5000](http://127.0.0.1:5000)
```
### Thao tác trên Web

1. Mở trình duyệt (Chrome/Edge) truy cập: [http://127.0.0.1:5000](http://127.0.0.1:5000)
2. Nhấn **Choose File** để chọn ảnh thú cưng từ máy tính.
3. Nhấn nút **Upload/Detect**.
4. Hệ thống sẽ trả về kết quả nhận diện.

## ❗ Khắc phục lỗi thường gặp (Troubleshooting)

Trong quá trình cài đặt, nếu bạn gặp lỗi, hãy kiểm tra các trường hợp sau:

### 1. Lỗi `No matching distribution found for tensorflow==2.15.0`
* **Nguyên nhân:** Bạn đang dùng Python 3.12 hoặc 3.13 (quá mới).
* **Khắc phục:** Hãy cài đặt **Python 3.10** và tạo lại `venv` như hướng dẫn ở Bước 2.

### 2. Lỗi `ValueError: Unrecognized keyword arguments passed to DepthwiseConv2D`
* **Nguyên nhân:** Bạn đã cài nhầm phiên bản Keras 3 (mới nhất) thay vì Keras 2.
* **Khắc phục:** Đảm bảo file `requirements.txt` của bạn chứa đúng các phiên bản gốc và chạy lại lệnh:
    ```bash
    pip install -r requirements.txt
    ```

### 3. Lỗi `ModuleNotFoundError: No module named 'flask'`
* **Nguyên nhân:** Bạn chưa kích hoạt môi trường ảo.
* **Khắc phục:** Chạy lại lệnh kích hoạt:
    ```bash
    .\venv\Scripts\activate
    ```
