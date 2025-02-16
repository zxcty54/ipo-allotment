from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from flask_cors import CORS  

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS

def check_ipo_status(app_no):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")  # ✅ Headless mode for Render

    service = Service(GeckoDriverManager().install())  
    driver = webdriver.Firefox(service=service, options=options)

    try:
        driver.get("https://www.linkintime.co.in/IPO/public-issues.html")
        search_box = driver.find_element(By.NAME, "appNo")  
        search_box.send_keys(app_no)
        search_box.submit()

        driver.implicitly_wait(5)
        result = driver.find_element(By.CLASS_NAME, "result").text  

    except Exception as e:
        result = str(e)

    driver.quit()
    return result

@app.route('/check-ipo', methods=['GET'])
def check():
    app_no = request.args.get("app_no")
    if not app_no:
        return jsonify({"error": "Application number is required"}), 400
    status = check_ipo_status(app_no)
    return jsonify({"IPO Status": status})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
