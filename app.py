from flask import Flask, jsonify, request
from flask_cors import CORS  # ✅ add this
import ipl
import jugad

app = Flask(__name__)
CORS(app)  # ✅ add this


@app.route('/')
def home():
    return "Hello World"


@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)


@app.route('/api/teamVteam')
def teamVteam():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = ipl.teamVteamAPI(team1, team2)
    print(response)
    return response


@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')
    response = jugad.teamAPI(team_name)
    return response  


@app.route('/api/batting-record')
def batting_record():
    batsman_name = request.args.get('batsman')  # ✅
    response = jugad.batsmanAPI(batsman_name)
    return response


@app.route('/api/bowling-record')
def bowling_record():
    bowler_name = request.args.get('bowler')  # ✅
    response = jugad.bowlerAPI(bowler_name)
    return response


app.run(debug=True)