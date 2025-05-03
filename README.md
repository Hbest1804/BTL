# 🏠 Bất Động Sản Quảng Bình Crawler

**BDS Crawler** là một công cụ thu thập dữ liệu nhà đất từ trang [alonhadat.com.vn](https://alonhadat.com.vn), tập trung vào khu vực **thành phố Đồng Hới, tỉnh Quảng Bình**. Dữ liệu được lưu dưới dạng file Excel (.xlsx) và chương trình được lập lịch chạy tự động mỗi ngày lúc **06:00 sáng**.

---

## 📌 Tính năng

- 🔍 Tự động duyệt nhiều trang bất động sản.
- 📝 Thu thập thông tin: tiêu đề, mô tả, diện tích, giá bán, địa chỉ.
- 📁 Xuất dữ liệu ra file Excel `bds.xlsx`.
- ⏰ Lên lịch tự động thu thập mỗi ngày lúc 06:00 sáng.
- ✅ Dễ mở rộng, dễ sử dụng và tùy chỉnh.

---

## ⚙️ Yêu cầu hệ thống

- Python 3.12 trở lên
- Google Chrome

---

## 📥 Cài đặt

1. **Clone dự án về máy:**

   ```bash
   git clone https://github.com/Hbest1804/BTL
   
Tải và cài Google Chrome (nếu chưa có):

Tải tại: https://www.google.com/chrome/

Cài đặt như phần mềm thông thường.

2.Thư viện:

pip install -r requirements.txt

3.Chạy chương trình:

python bds.py

📂 Kết quả:

Dữ liệu thu thập được sẽ được lưu vào file Excel bds.xlsx.

📂 Cấu trúc thư mục:



BTL/
├── bds.py               
├── bds.xlsx            
├── README.md            
└── requirements.txt     
