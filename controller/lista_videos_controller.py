from app import app
from flask import render_template,request,redirect,url_for
from model.video_model import Lista_videos,Lista_favorito


@app.route('/lista_videos/<id>')
def lista_videos(id):

    todas_as_listas = Lista_videos().get_lista_user(id)

    return render_template('lista_videos.html',lista_videos = todas_as_listas)

@app.route('/lista_favoritos/<id>')
def lista_favoritos(id):

    todas_as_listas = Lista_favorito().get_lista_favorito_user(id)

    return render_template('lista_videos.html',lista_favorito = todas_as_listas)