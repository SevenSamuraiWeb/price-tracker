# Amazon Price Tracker 🌐✨

This project is a Python-based **Amazon Price Tracker** that monitors the price of an item on Amazon and sends an email alert when the price drops below a user-defined target price. The project is implemented with the following technologies: 🔧✨⭐

- **Python** for backend logic
- **Streamlit** for the user interface
- **Requests** and **BeautifulSoup** for web scraping
- **SMTP** for email notifications

---

## Features 🌟🔔⭐

- Fetch and monitor prices of Amazon products
- Set a target price for alerts
- Receive email notifications when the target price is reached
- User-friendly web interface built with Streamlit

---

## Prerequisites 🔧📊✨

1. **Python 3.8+** installed on your system.
2. **Git** for version control.
3. A **Gmail account** for sending email notifications.

---

## Installation 🛠️⭐⚡

### 1. Clone the Repository 📂🌐

```bash
git clone https://github.com/your-username/price-tracker.git
cd price-tracker
```

### 2. Create a Virtual Environment (Optional but Recommended) 🌐⚡

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies 🛠️🔔

```bash
pip install -r requirements.txt
```

---

## Usage 🔧🌟⚡

### 1. Configure Email Settings 📧⚡

Set up your Gmail credentials in the `secrets.toml` file for local testing: 🌐🔐

```toml
email = "your_email@gmail.com"
password = "your_password"
```

Alternatively, use Streamlit's **Secrets Management** feature for deployment.

### 2. Run the App Locally 📺🌟

```bash
streamlit run app.py
```

Access the app in your browser at: [http://localhost:8501](http://localhost:8501)

### 3. Deploy to Streamlit Community Cloud 🌐✨

1. Push your code to GitHub.
2. Log in to [Streamlit Cloud](https://streamlit.io/cloud).
3. Deploy your app by linking your repository.

---

## Project Structure 🌐🔧✨

```
price-tracker/
├── app.py                 # Streamlit app file
├── requirements.txt       # List of Python dependencies
├── secrets.toml           # (Optional) Email credentials for local testing
├── utils/                 # Utility functions (e.g., scraping, email sending)
    ├── scraper.py         # Logic for fetching Amazon prices
    ├── emailer.py         # Logic for sending email notifications
```

---

## How It Works 🌟🔧⚡

1. **Price Monitoring**: 🌐✨

   - Users provide the Amazon product URL and their target price.
   - The app uses `requests` and `BeautifulSoup` to fetch and parse the product page.

2. **Email Notifications**: 📧⭐

   - If the price is below the target price, the app sends an email alert using Gmail's SMTP server.

3. **User Interface**: 🔔🌟

   - A simple and interactive UI built with Streamlit allows users to input details and view results.

---

## Example Workflow 🔧🌐🔔

1. Enter the Amazon product URL and target price in the Streamlit app.
2. The app fetches the current price and displays it.
3. If the price is below the target, you will receive an email alert.

---

## Limitations 🌐🔧⭐

- Amazon may block scraping attempts, especially if CAPTCHAs are encountered frequently.
- Requires a Gmail account for email alerts.
- Only monitors prices for a single product at a time.

---

## Future Improvements 🔄✨🌟

- Add support for monitoring multiple products.
- Integrate a database to save user preferences.
- Use a headless browser (e.g., Selenium) to bypass CAPTCHAs.
- Implement OAuth2 for secure email sending.

---

## License 🔒⭐⚡

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments 🔧🔔✨

- [Streamlit Documentation](https://docs.streamlit.io/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/en/master/)

