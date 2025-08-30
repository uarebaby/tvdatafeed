import logging
import os
from tvDatafeed import TvDatafeed, Interval

# ชื่อไฟล์ token
TOKEN_FILE = 'tv_auth_token.json'

# เปิด logging เพื่อดูขั้นตอนการทำงาน
logging.basicConfig(level=logging.INFO)

try:
    # ใส่ username และ password ของคุณที่นี่
    tv = TvDatafeed(
        username='xxxx',
        password='xxxx',
        autologin=True
    )

    # ลองดึงข้อมูลเพื่อทดสอบการเชื่อมต่อ
    data = tv.get_hist(symbol='AAPL', exchange='NASDAQ',
interval=Interval.in_daily, n_bars=1)

    if data is not None and not data.empty:
        print("Login and data retrieval successful!")
        print(data)
    else:
        # หากดึงข้อมูลล้มเหลว, แสดงว่า token อาจจะหมดอายุ
        print("Failed to retrieve data. The saved auth_token might be invalid.")

        # ตรวจสอบว่ามีไฟล์ token ที่บันทึกไว้หรือไม่ และทำการลบ       
        if os.path.exists(TOKEN_FILE):
            os.remove(TOKEN_FILE)
            print(f"Removed invalid token file: {TOKEN_FILE}")        
            print("Please run the script again to log in and create a new token.")
        else:
            # กรณีที่ล้มเหลวตั้งแต่การล็อกอินครั้งแรก
            print("Could not log in. Please check your username and password.")
except Exception as e:
    print(f"An error occurred: {e}")