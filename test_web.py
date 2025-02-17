from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Налаштовуємо WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 1️ Відкриваємо тестову сторінку логіна
    driver.get("https://practicetestautomation.com/practice-test-login/")
    
    # 2️ Очікуємо завантаження поля "Username"
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    
    # 3️ Заповнюємо логін і пароль
    username_input.send_keys("student")  # Тестовий логін
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("Password123")  # Тестовий пароль

    # 4️ Натискаємо кнопку "Submit"
    login_button = driver.find_element(By.ID, "submit")
    login_button.click()

    # 5️ Очікуємо перенаправлення на сторінку після успішного входу
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    ).text

    # 6️ Перевіряємо, що вхід виконано успішно
    assert "Logged In Successfully" in success_message, "Помилка: Вхід не виконано"

    print("✅ Тест успішний: Користувач успішно увійшов у систему!")

except Exception as e:
    print(f"❌ Помилка тестування: {e}")

finally:
    # Закриваємо браузер
    time.sleep(3)  # Додаємо затримку, щоб побачити результат перед закриттям
    driver.quit()
