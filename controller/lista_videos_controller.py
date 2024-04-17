from app import app
from flask import render_template,request,redirect,url_for
from model.video_model import Lista_videos,Video
from model.login_model import User


@app.route('/lista_videos/<id>')
def lista_videos(id):
  
    todas_as_listas = Lista_videos().get_lista_user(id)
    videos = Video().get_videos(id)

    return render_template('lista_videos.html',lista_videos = todas_as_listas,videos = videos)

@app.route('/lista_favoritos/<id>')
def lista_favoritos(id):
    
    user = User.query.get(id)
    if user:
        todas_as_listas= user.get_listas_favoritas()
    else:
        todas_as_listas= None
     

    return render_template('lista_favoritos.html',lista_favorito = todas_as_listas)

@app.route('/todas_as_listas')
def todas_as_listas():
     return render_template("todas_as_listas.html",lista_videos = Lista_videos().get_lista_videos())
