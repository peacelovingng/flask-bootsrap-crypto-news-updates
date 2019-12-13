from flask import Flask, render_template, url_for
import requests
import json

app = Flask(__name__)

api_requests = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
api = json.loads(api_requests.content)


@app.route('/')
def index():
    return render_template('index.html', api=api, title='Crypto News Update')


if __name__=='__main__':
    app.run(debug=True)


'''
<div>
    <p class = "aboutmetext">Let's Connect</p>
    <a href = "https://www.linkedin.com/mwlite/me"><img src="img/linkedin.svg" class="social"></a>
    <a href = "https://www.twitter.com/peacelovingng"><img src="img/twitter.svg" class="social"></a>
    <a href="https://www.facebook.com/alamuolawamiwale.ahmed"><img src="img/facebook.svg" class="social"></a>
    <a href = "https://www.github.com/peacelovingng"><img src="img/github.svg" class="social"></a>
    <a href="mailto:alamuolawale@gmail.com"><img src="img/github.svg" class="social"></a>
  </div>
'''
