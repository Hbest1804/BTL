from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import schedule

def crawl_data():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome()

    data = []

    driver.get("https://alonhadat.com.vn/")
    time.sleep(2)

    province_select = Select(driver.find_element(By.CSS_SELECTOR, "select.demand"))
    province_select.select_by_visible_text("Cần bán")

    province_select = Select(driver.find_element(By.CSS_SELECTOR, "select.property-type"))
    province_select.select_by_visible_text("Nhà")

    province_select = Select(driver.find_element(By.CSS_SELECTOR, "select.province"))
    province_select.select_by_visible_text("Quảng Bình")
    time .sleep(2)
    district_select = Select(driver.find_element(By.CSS_SELECTOR, "select.district"))
    district_select.select_by_visible_text("Thành phố Đồng Hới")
   
    
    driver.find_element(By.CLASS_NAME, "btnsearch").click()
    
    while True:
        
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

      
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, "a.page-next")
            next_button.click()
            time.sleep(2)
        except Exception:
            print("Không tìm thấy nút 'Next', dừng lại.")
        break


    driver.quit()
   
    df = pd.DataFrame(data)
    df.to_excel("bds.xlsx", index=False)
    print(" Đã lưu file thành công!")

def job():
    print("Đang chạy job định kỳ...")
    crawl_data()

schedule.every().day.at("15:40").do(job)

print("Đang chờ tới giờ chạy...")

while True:
    schedule.run_pending()
    time.sleep(20)
