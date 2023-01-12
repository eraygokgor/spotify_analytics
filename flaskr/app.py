from flask import Flask, redirect, make_response
from decouple import config

app = Flask(__name__)

@app.route("/")
def spotify_auth():
    return "<p>Hello, World!</p>"
 
@app.route('/login')
def authorize():
    client_id = config('client_id')
    redirect_uri = config('redirect_uri')
    scope = config('scope')

    # redirect user to Spotify authorization page
    authorize_url = 'https://accounts.spotify.com/en/authorize?'
    parameters = 'response_type=code&client_id=' + client_id + '&redirect_uri=' + redirect_uri + '&scope=' + scope
    response = make_response(redirect(authorize_url + parameters))

    print(response.response)

    return f"Hey, there it is the response: {response}"
