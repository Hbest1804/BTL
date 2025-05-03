from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd
import time
import schedule

def crawl_data():
    options = webdriver.ChromeOptions()

    driver = webdriver.Chrome()

    data = []
    page = 1    

    while True:
        url = f"https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/quang-binh/543/thanh-pho-dong-hoi/trang--{page}.html"
        print(f"Đang truy cập trang {page}")
        driver.get(url)
        time.sleep(2)  

        items = driver.find_elements(By.CLASS_NAME, "content-item")

        if not items:
            print("Không còn dữ liệu, dừng lại.")
            break

        for item in items:
            try:
                title = item.find_element(By.CLASS_NAME, "ct_title").text.strip()
            except:
                title = ""

            try:
                description = item.find_element(By.CLASS_NAME, "ct_brief").text.strip()
            except:
                description = ""

            try:
                area = item.find_element(By.CLASS_NAME, "ct_dt").text.strip()
            except:
                area = ""

            try:
                price = item.find_element(By.CLASS_NAME, "ct_price").text.strip()
            except:
                price = ""

            try:
                address = item.find_element(By.CLASS_NAME, "ct_dis").text.strip()
            except:
                address = ""

            data.append({
                "Tiêu đề": title,
                "Mô tả": description,
                "Diện tích": area,
                "Giá": price,
                "Địa chỉ": address,
            })

        page += 1

    driver.quit()

    # Lưu ra file
    df = pd.DataFrame(data)
    df.to_excel("bds.xlsx", index=False)
    print("✅ Đã lưu file thành công!")

def job():
    print("Đang chạy job định kỳ...")
    crawl_data()


schedule.every().day.at("06:00").do(job)

print("Đang chờ tới giờ chạy...")

while True:
    schedule.run_pending()
    time.sleep(60)