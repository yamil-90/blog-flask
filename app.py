from flask import Flask # incluimos todo lo necesario para el uso de flask
from flask import render_template,request,redirect,url_for,flash # incluimos para el renderizado de template 
from flaskext.mysql import MySQL	            # para comunicacion mysql
from datetime import datetime, time
from flask import send_from_directory
import urllib.request, json




app= Flask(__name__)

app.config.from_pyfile('config.py')

mysql = MySQL() 
mysql.init_app(app) 

@app.route('/')
def home():
    conn= mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `blog_flask`.`posts`;")
    posts = cursor.fetchall()
    conn.commit()
    return render_template('index.html', posts=posts)

@app.route('/images/<nombreFoto>')
def images(nombreFoto):
    return send_from_directory(app.config['CARPETA'], nombreFoto)
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    url= 'https://api.mercadolibre.com/sites/MLA/search?nickname=MASCOTASYA_AR&limit=8'

    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)
    return render_template('products.html', products=dict['results'])
# 356239089
@app.route('/message')
def message():
    return render_template('message.html')

@app.route('/message/send', methods=['POST'])
def messageSend():
    pass

@app.route('/create')
def post_create():
    return render_template('create.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/store', methods=["POST"])
def store():
    _title=request.form['txtTitle']
    _content=request.form['txtContent'] 
    _image=request.form['txtImage']
    if _title == '' or _content =='':
        flash('Los campos nombre y correo son obligatorios')
        return redirect(url_for('create'))
    
    sql= "INSERT INTO `blog_flask`.`posts` (`title`,`content`,`image`) VALUES (%s,%s,%s)"
    datos=(_title,_content,_image) 
    conn=mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos) 
    conn.commit()
    return redirect('/')

@app.route('/posts/<int:id>')
def posts(id):
    conn= mysql.connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `blog_flask`.`posts` WHERE id=%s LIMIT 1", id)
    post= cursor.fetchall()
    conn.commit()
    print (post)
    return render_template('posts.html', posts=post)

    #    
# def shutdown_server():
#     func = request.environ.get('werkzeug.server.shutdown')
#     if func is None:
#         raise RuntimeError('Not running with the Werkzeug Server')
#     func()
# @app.route('/shutdown', methods=['GET'])
# def shutdown():
#     shutdown_server()
#     return 'Server shutting down...'

if __name__=='__main__':    

    app.run(debug=True)