from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from requests_html import HTMLSession
from time import sleep
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# Tetapan untuk Chrome
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')

# Satu User-Agent sahaja
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/91.0.4472.124 Safari/537.36"

def open_url(url):
    # Mulakan sesi HTML
    session = HTMLSession()

    # Tetapkan User-Agent
    headers = {
        'User-Agent': user_agent
    }

    # Ambil halaman web dengan header yang ditetapkan
    response = session.get(url, headers=headers)

    # Tunggu beberapa saat untuk mensimulasikan tindakan manusia melihat iklan
    sleep(4)  # Tunggu 4 saat

    # Cetak kod status untuk memastikan halaman dimuat dengan betul
    print(f"Opened {url} with status code {response.status_code}")

    # Buka Chrome dengan Selenium untuk simulasi klik
    driver = webdriver.Chrome(service=Service('/usr/local/bin/chromedriver'), options=chrome_options)
    driver.get(url)

    # Tunggu sehingga elemen klik dapat dilihat
    sleep(6)  # Simulasikan menunggu

    try:
        # Klik butang "Click Here To Your Link Destination"
        button = driver.find_element(By.XPATH, '//*[@id="makingdifferenttimer"]')
        button.click()
        print("Clicked the button")
    except Exception as e:
        print(f"Failed to click the button: {e}")
    finally:
        driver.quit()

    # Tunggu lagi untuk simulasi manusia melihat iklan
    sleep(1)

def main():
    # Minta URL dari pengguna
    url = input("Masukkan URL: ")
    count = 5000000  # Bilangan kali untuk membuka URL
    urls = [url] * count  # Buat senarai URL untuk diulang

    # Kurangkan bilangan pekerja serentak kepada 10
    with ThreadPoolExecutor(max_workers=10) as executor:
        while urls:
            futures = [executor.submit(open_url, urls.pop()) for _ in range(min(10, len(urls)))]
            for future in as_completed(futures):
                future.result()  # Dapatkan hasil tugas (ini akan memaparkan sebarang pengecualian)

    print("All URLs have been opened.")

# Jalankan fungsi utama
if __name__ == "__main__":
    main()
