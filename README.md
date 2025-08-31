# Flipkart Price Tracker

This is a Python-based Flipkart Price Tracker that monitors the price of a product on Flipkart and sends an email and SMS alert when the price drops below a user-defined target price.

## Technologies Used
- Python for backend logic
- Streamlit for the user interface
- Requests and BeautifulSoup for web scraping
- SMTP for email notifications
- Twilio for SMS notifications

---

## Features
- Fetch and monitor prices of Flipkart products
- Set a target price for alerts
- Receive email and SMS notifications when the target price is reached
- User-friendly web interface built with Streamlit
- Track multiple products per user
- Secure authentication and credential management

---

## Prerequisites
1. Python 3.8 or higher
2. Git (optional, for version control)
3. A Gmail account for sending email notifications
4. Twilio account for SMS notifications

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/price-tracker.git
   cd price-tracker
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage
1. Configure email and SMS settings:
   - Create a file named `secrets.toml` in the project directory with the following content:
     ```toml
     email = "your_email@gmail.com"
     password = "your_app_password"
     # Twilio SMS credentials
     twilio_sid = "your_twilio_account_sid"
     twilio_token = "your_twilio_auth_token"
     twilio_number = "+1234567890"  # Your Twilio phone number
     user_phone = "+1987654321"    # Your mobile number to receive SMS
     ```
   - **SMS Notifications:**
     - Sign up at [Twilio](https://www.twilio.com/) and get your Account SID, Auth Token, and a Twilio phone number.
     - Add these credentials to your `secrets.toml` as shown above.
     - SMS notifications will be sent to `user_phone` when the price drops below your target.
   - **Important:** For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833?hl=en) instead of your regular account password. To generate an app password:
     1. Go to your Google Account > Security > Signing in to Google > App passwords.
     2. Select "Mail" as the app and "Windows Computer" as the device.
     3. Copy the generated password and use it in your `secrets.toml` file.
   - Never share your app password or commit `secrets.toml` to version control.
2. Run the app locally:
   ```bash
   streamlit run app.py
   ```
   - Open your browser and go to [http://localhost:8501](http://localhost:8501)
3. (Optional) Deploy to Streamlit Community Cloud:
   - Push your code to GitHub
   - Log in to [Streamlit Cloud](https://streamlit.io/cloud)
   - Deploy your app by linking your repository

---

## Project Structure
```
price-tracker/
├── app.py            # Streamlit app file
├── main.py           # Logic for fetching prices and sending email/SMS alerts
├── requirements.txt  # List of Python dependencies
├── secrets.toml      # Email/SMS credentials (not tracked by git)
├── .gitignore        # Git ignore file
├── db.py             # Database logic for users/products
├── sms.py            # SMS notification logic
```

---

## How It Works
1. **Price Monitoring**
   - Users provide the Flipkart product URL and their target price.
   - The app uses `requests` and `BeautifulSoup` to fetch and parse the product page.
2. **Email & SMS Notifications**
   - If the price is below the target price, the app sends an email and SMS alert.
3. **User Interface**
   - A simple and interactive UI built with Streamlit allows users to input details and view results.

---

## Example Workflow
1. Enter the Flipkart product URL and target price in the Streamlit app.
2. The app fetches the current price and displays it.
3. If the price is below the target, you will receive an email and SMS alert.

---

## Limitations
- Flipkart may block scraping attempts, especially if a large number of requests are sent.
- Requires a Gmail account for email alerts.
- Only monitors prices for a single product at a time.

---

## Future Improvements
- Add support for monitoring multiple products
- Integrate a database to save user preferences
- Use a headless browser (e.g., Selenium) to bypass CAPTCHAs
- Implement OAuth2 for secure email sending

---

## License
This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments
- [Streamlit Documentation](https://docs.streamlit.io/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/en/master/)
- [Twilio Documentation](https://www.twilio.com/docs/)

# Flipkart Price Tracker

This is a Python-based Flipkart Price Tracker that monitors the price of a product on Flipkart and sends an email alert when the price drops below a user-defined target price.

## Technologies Used

- Python for backend logic
- Streamlit for the user interface
- Requests and BeautifulSoup for web scraping
- SMTP for email notifications

---

## Features

- Fetch and monitor prices of Flipkart products
- Set a target price for alerts
- Receive email notifications when the target price is reached
- User-friendly web interface built with Streamlit

---

## Prerequisites

1. Python 3.8 or higher
2. Git (optional, for version control)
3. A Gmail account for sending email notifications

---

## Installation


1. Clone the repository (if not already downloaded):
   ```bash
   git clone https://github.com/your-username/price-tracker.git
   cd price-tracker
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---


## Usage

1. Configure email settings:
   - Create a file named `secrets.toml` in the project directory with the following content:
     ```toml
     email = "your_email@gmail.com"
     password = "your_password"
     ```

2. Run the app locally:
   ```bash
   streamlit run app.py
   ```
   - Open your browser and go to [http://localhost:8501](http://localhost:8501)

3. (Optional) Deploy to Streamlit Community Cloud:
   - Push your code to GitHub
   - Log in to [Streamlit Cloud](https://streamlit.io/cloud)
   - Deploy your app by linking your repository

---


## Project Structure

```
price-tracker/
├── app.py            # Streamlit app file
├── main.py           # Logic for fetching prices and sending email alerts
├── requirements.txt  # List of Python dependencies
├── secrets.toml      # Email credentials (not tracked by git)
├── .gitignore        # Git ignore file
```

---


## How It Works

1. **Price Monitoring**
   - Users provide the Flipkart product URL and their target price.
   - The app uses `requests` and `BeautifulSoup` to fetch and parse the product page.

2. **Email Notifications**
   - If the price is below the target price, the app sends an email alert using Gmail's SMTP server.

3. **User Interface**
   - A simple and interactive UI built with Streamlit allows users to input details and view results.

---


## Example Workflow

1. Enter the Flipkart product URL and target price in the Streamlit app.
2. The app fetches the current price and displays it.
3. If the price is below the target, you will receive an email alert.

---


## Limitations

- Flipkart may block scraping attempts, especially if a large number of requests are sent.
- Requires a Gmail account for email alerts.
- Only monitors prices for a single product at a time.

---


## Future Improvements

- Add support for monitoring multiple products
- Integrate a database to save user preferences
- Use a headless browser (e.g., Selenium) to bypass CAPTCHAs
- Implement OAuth2 for secure email sending

---


## License

This project is licensed under the [MIT License](LICENSE).

---


## Acknowledgments

- [Streamlit Documentation](https://docs.streamlit.io/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/en/master/)

