from pyngrok import ngrok
from getpass import getpass
from threading import Thread
import time

token = getpass("Enter your ngrok auth token: ")
ngrok.set_auth_token(token)

def run_flask():
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False
    )

Thread(target=run_flask, daemon=True).start()

time.sleep(2)

public_url = ngrok.connect(5000).public_url

print("Your Loan Prediction Website:")
print(public_url)
