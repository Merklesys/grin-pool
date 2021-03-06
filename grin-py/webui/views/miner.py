from datetime import datetime
import hashlib
import timeit
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen # python 3 syntax
import requests
import time
import pygal
from pygal.style import Style
import json
import sys
import traceback 
import cairosvg


from flask import Flask, Blueprint, render_template, request, session, make_response, flash, url_for, redirect
from wtforms import Form, BooleanField, StringField, PasswordField, validators, SelectField, IntegerField
from flask import Flask, Blueprint, render_template, request, session, make_response


miner_profile = Blueprint('miner_profile'
                           , __name__
                           , template_folder='templates'
                           , static_folder='static'
                           )

@miner_profile.route('/miner')
def miner_template():
    return render_template('miner/miner.html')
