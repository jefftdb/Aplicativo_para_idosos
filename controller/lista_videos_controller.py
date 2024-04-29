from app import app
from flask import render_template,request,redirect,url_for
from model.video_model import Lista_videos,Video
from model.login_model import User
import os
from werkzeug.utils import secure_filename


@app.route('/lista_videos/<id>')
def lista_videos(id):
  
    todas_as_listas = Lista_videos().get_lista_user(id)
    videos = Video().get_videos(id)

    return render_template('lista_videos.html',lista_videos = todas_as_listas,videos = videos)

@app.route('/add_video/<id_lista>',methods = ['GET','POST'])
def add_video(id_lista):
    if request.method == 'POST':
        titulo = request.form['titulo']
        video = request.files['video']
        filename = secure_filename(video.filename)
        video.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        print(titulo)
        print(video)
        return 'metodo post'
    else:
        return render_template('add_video.html')


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
