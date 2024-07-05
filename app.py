import requests
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def home():
    api_url = 'https://api.api-ninjas.com/v1/jokes?'
    response = requests.get(api_url, headers={'X-Api-Key': 'IoKQnEWgzSlEyHC5LdtCPQ==ERhflfFGbWafwQN8'})
    if response.status_code == requests.codes.ok:
        joke = response.json()
        joke = joke[0]['joke']
    else:
        print("Error:", response.status_code, response.text)

    return render_template('index.html', joke = joke)


if __name__ == '__main__':
    app.run(debug=True)