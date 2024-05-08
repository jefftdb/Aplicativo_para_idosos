from app import app,db
from flask import render_template,request,redirect,url_for
from model.video_model import Lista_videos,Video,Categoria
from model.login_model import User
import os
from werkzeug.utils import secure_filename
from Utils.utils import Utils

utilitario = Utils()


@app.route('/lista_videos/<id>',methods = ['GET','POST'])
def lista_videos(id):
    if request.method == 'POST':
        titulo = request.form['titulo']
        user_id= request.form['user_id']
        categoria = request.form['categoria']

        nova_lista = Lista_videos(titulo,user_id,categoria)
        
        db.session.add(nova_lista)
        db.session.commit()

      
    todas_as_listas = Lista_videos.query.filter_by(id_user = id)
    videos = Video.query.all()
    categorias = Categoria.query.all()

    return render_template('lista_videos.html',lista_videos = todas_as_listas,videos = videos,categorias = categorias)


     



@app.route('/add_video/<id_lista>',methods = ['GET','POST'])
def add_video(id_lista):
    if request.method == 'POST':
        titulo = request.form['titulo']
        arquivo = request.files['video']
        filename = utilitario.set_name()
        arquivo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        url_video = 'data/' + filename

        video = Video(titulo,url_video,id_lista)

        db.session.add(video)
        db.session.commit()

        return redirect(url_for('lista_videos', id = id_lista) )
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
