#!/usr/bin/env python3 

from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect

app = Flask(__name__)

@app.route('/')
def start():
    return render_template("champFinder.html")

@app.route('/found/<champName>')
def found(champName):
    vikings = ['berserker', 'raider', 'highlander', 'shaman', 'warlord', 'valkyrie', 'jormungandr']
    knights = ['warden', 'conquerer', 'lawbringer', 'peacekeeper', 'centurion', 'gladiator', 'black prior', 'warmonger', 'gryphon']
    samurai = ['orochi', 'kensei', 'shugoki', 'nobushi', 'shinobi', 'aramusha', 'hitokiri', 'kyoshin']
    outlanders = ['pirate', 'medjay', 'afeera', 'ocelotl']
    wulin = ['tiandi', 'shaolin', 'nuxia', 'jiang jun', 'jiangjun', 'zhanhu']

    if champName in vikings:
        return render_template('found.html', name=champName, faction='viking')
    elif champName in knights:
        return render_template('found.html', name=champName, faction='knight')
    elif champName in samurai:
        return render_template('found.html', name=champName, faction='samurai')
    elif champName in outlanders:
        return render_template('found.html', name=champName, faction='outlander')
    elif champName in wulin:
        return render_template('found.html', name=champName, faction='wulin')
    else:
        return "We didn't find that one... Are you sure you spelled the champion name right?"

@app.route('/search', methods = ['POST', 'GET'])
def search():
    if request.method == 'POST':
        if request.form.get('nm'):
            champ = request.form.get('nm')
        else:
            champ = 'not_specified'

    elif request.method == 'GET':
        if request.form.get('nm'):
            champ = request.form.get('nm')
        else:
            champ = 'not_specified'

    if champ == 'not_specified':
        return redirect(url_for("start"))
    else:
        #return redirect(url_for("found", champName=champ.lower()))
        return redirect(f"/found/{champ.lower()}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2224)
