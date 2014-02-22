from shortenerapp import shortenerapp, db
from flask import Flask, jsonify, request, render_template, redirect
from models import Url
import string,random,webbrowser

@shortenerapp.route('/')
@shortenerapp.route('/index')
def index():
    return render_template('index.html')

def genurl():
    rand = ''.join(random.choice(string.ascii_letters + string.digits) for x in range(5))    
    return rand

@shortenerapp.route('/shorten')
def shorten():
    url = request.args.get('longurl')
    if url[:4] != "http":
        url = "http://"+url
    existingurl = 'placeholder'

    while existingurl is not None:
        shorturl = genurl()
        existingurl = Url.query.filter_by(shortu=shorturl).first()
        print 'existing: '+ str(existingurl)
    
    newurl = Url(shortu=shorturl, longu=url)
    db.session.add(newurl)
    db.session.commit()   
    print request.url_root 
    shorturl=request.url_root+shorturl
    return jsonify(result=shorturl)

@shortenerapp.route('/<shorturl>')
def redirecturl(shorturl):
    longurl = Url.query.filter_by(shortu=shorturl).first()
    if longurl is None:
        return "invalid url"
    else:
        print shorturl + ' -> ' + longurl.longu
        return redirect(longurl.longu)
