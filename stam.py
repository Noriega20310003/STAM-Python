from flask import Flask, render_template, redirect, url_for, session, request
from flask_mysqldb import MySQL, MySQLdb
from flask_bcrypt import bcrypt
from PIL import Image, ImageFilter

import os
import io

stamApp = Flask(__name__)
stamApp.config['MYSQL_HOST'] ='localhost'
stamApp.config['MYSQL_USER'] ='root'
stamApp.config['MYSQL_PASSWORD'] ='mysql'
stamApp.config['MYSQL_DB'] ='juegos'
stamApp.config['MYSQL_CURSORCLASS'] ='DictCursor'
mysql = MySQL(stamApp)
APP_ROOT=os.path.dirname(os.path.abspath(__file__))

@stamApp.route('/')
def index():
    return render_template('login.html')


@stamApp.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        
        nombredes    = request.form['nombredes']
        try:
            iddist = request.form['iddist']
        except Exception as e:
            iddist = ""

        if iddist == "":
            iddist= 1
            nombre    = 'sitribuidor nulo'
            clausulas   = 'NA'
            fd = '2019-12-04'
            regdist = mysql.connection.cursor()
            regdist.execute("INSERT INTO dist (nombre, clausulas, fd) VALUES (%s, %s, %s)",(nombre, clausulas, fd))
            mysql.connection.commit()
            regdist.close()
            return redirect(url_for("register"))

        contra   = request.form['contra'].encode('utf-8')
        clavecifrada = bcrypt.hashpw(contra, bcrypt.gensalt())

        regdes = mysql.connection.cursor()
        regdes.execute("INSERT INTO desarrollador (nombredes, contra, iddist) VALUES (%s,%s,%s)", (nombredes, clavecifrada, iddist))
        mysql.connection.commit()
        return redirect(url_for("login"))
        
    else:
        seldist = mysql.connection.cursor()
        seldist.execute("SELECT * FROM dist")
        di = seldist.fetchall()
        seldist.close()
        return render_template("register.html", dist=di)


@stamApp.route('/registeru', methods=["GET", "POST"])
def registeru():
    if request.method == 'POST':
        
        region    = request.form['region']
        direccion    = request.form['direccion']
        nombreu    = request.form['nombreu']
        tarjeta    = request.form['tarjeta']
        contra   = request.form['contra'].encode('utf-8')
        clavecifrada = bcrypt.hashpw(contra, bcrypt.gensalt())

        regdes = mysql.connection.cursor()
        regdes.execute("INSERT INTO usuario (region,direccionfactura,nombreusuario,tarjeta,contra) VALUES (%s,%s,%s,%s,%s)",(region,direccion,nombreu,tarjeta,clavecifrada))
        mysql.connection.commit()
        return redirect(url_for("login"))
        
    else:
        return render_template("registeru.html")
    

@stamApp.route('/login', methods=["GET","POST"])
def login():
    if request.method == 'POST':
        nombredes  = request.form['nombredes']
        contra = request.form['contra'].encode('utf-8')
        selemp = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        selemp.execute("SELECT * FROM desarrollador WHERE nombredes=%s",(nombredes,))
        amd = selemp.fetchone()
        selemp.close()

        if amd is not None:
            if bcrypt.hashpw(contra, amd["contra"].encode('utf-8'))==amd["contra"].encode('utf-8'):
                session['nombredes'] = amd['nombredes']
                return render_template("home.html")
            else:
                return"Error: contraseña incorrecta"
        
        else:
            selus = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            selus.execute("SELECT * FROM usuario WHERE nombreusuario=%s",(nombredes,))
            usr = selus.fetchone()
            selus.close
            if usr is not None:
                if bcrypt.hashpw(contra, usr["contra"].encode('utf-8'))==usr["contra"].encode('utf-8'):
                    session['nombreusuario'] = usr['nombreusuario']
                    return render_template("home.html")
                else:
                    return"Error: contraseña incorrecta"
            else:"Error Usuario no existe"
    
    else: return render_template("login.html")



@stamApp.route('/logout')
def logout():
    session.clear()
    return render_template("login.html")

@stamApp.route('/productos/<string:idg>', methods=["GET"])
def productos(idg):
    selg = mysql.connection.cursor()
    selg.execute("SELECT * FROM juego WHERE idg=%s",(idg,))
    j = selg.fetchall()
    selg.close()
    nombreu =session

    Selempleado =mysql.connection.cursor()
    Selempleado.execute("SELECT * FROM usuario WHERE nombreusuario=%s",(nombreu,))
    u = Selempleado.fetchall()
    Selempleado.close()

    return render_template("productos.html", juegos=j, usuario=u)

#------------------------------------------------home-------------------------------------------------    

@stamApp.route('/home')
def home():
    selg = mysql.connection.cursor()
    selg.execute("SELECT * FROM juego")
    j = selg.fetchall()
    selg.close()


    return render_template('home.html', juegos=j)




# -----------------dist----------------------------#


@stamApp.route('/sdis',methods = ["POST" , "GET"])
def sdis():
    sdis =mysql.connection.cursor()
    sdis.execute("SELECT * FROM dist")
    d = sdis.fetchall()
    return render_template('dist.html', dist = d)

@stamApp.route('/idis',methods = ["POST" , "GET"])
def idis():
        nombre    = request.form['nombre']
        clausulas   = request.form['clausulas']  
        fd = request.form['fd']
        regdist = mysql.connection.cursor()
        regdist.execute("INSERT INTO dist (nombre, clausulas, fd) VALUES (%s, %s, %s)",(nombre, clausulas, fd))
        mysql.connection.commit()
        regdist.close()
        return redirect(url_for('sdis'))

@stamApp.route('/udis',methods = ["POST" , "GET"])
def udis():
        iddist   = request.form['iddist'] 
        nombre    = request.form['nombre']
        clausulas   = request.form['clausulas']  
        fd = request.form['fd']
        udist = mysql.connection.cursor()
        udist.execute("UPDATE dist SET nombre = %s, clausulas = %s, fd = %s WHERE iddist=%s",(nombre, clausulas, fd, iddist))
        mysql.connection.commit()
        udist.close()
        return redirect(url_for('sdis'))

@stamApp.route('/ddis/<string:iddist>', methods = ["GET"])
def ddis(iddist):
    delempleado = mysql.connection.cursor()
    delempleado.execute("DELETE FROM dist WHERE iddist=%s",(iddist,))
    mysql.connection.commit()
    return redirect(url_for('sdis'))

#------------------------desarrollador--------------------------
@stamApp.route('/sdes')
def sdes():
    seldesarrollador = mysql.connection.cursor()
    seldesarrollador.execute("SELECT * FROM desarrollador INNER JOIN dist ON desarrollador.iddist = dist.iddist")
    des = seldesarrollador.fetchall()
    seldesarrollador.close()

    seldist = mysql.connection.cursor()
    seldist.execute("SELECT * FROM dist")
    di = seldist.fetchall()
    seldist.close()

    return render_template('admin.html', dist=di, desarrollador=des) 

@stamApp.route('/ides', methods=["POST", "GET"]) 
def ides():
    nombredes  = request.form['nombredes']
    contra   = request.form['contra'].encode('utf-8')
    iddist   = request.form['iddist']
    clavecifrada = bcrypt.hashpw(contra, bcrypt.gensalt())

    regPedido = mysql.connection.cursor()
    regPedido.execute("INSERT INTO desarrollador (nombredes, contra, iddist) VALUES (%s,%s,%s)", (nombredes, clavecifrada, iddist))
    mysql.connection.commit()
    regPedido.close()
    return redirect (url_for('sdes'))

@stamApp.route('/udes',methods = ["POST" , "GET"])
def udes():
    iddesarrollador  = request.form['iddesarrollador']
    nombredes  = request.form['nombredes']
    contra   = request.form['contra'].encode('utf-8')
    iddist   = request.form['iddist']
    clavecifrada = bcrypt.hashpw(contra, bcrypt.gensalt())
    uus = mysql.connection.cursor()
    uus.execute("UPDATE desarrollador SET nombredes = %s,contra = %s,iddist = %s WHERE iddesarrollador=%s",(nombredes,clavecifrada,iddist,iddesarrollador ))
    mysql.connection.commit()
    return redirect(url_for('sdes'))

@stamApp.route('/ddes/<string:iddesarrollador>', methods = ["GET"])
def ddes(iddesarrollador):
    ddes = mysql.connection.cursor()
    ddes.execute("DELETE FROM desarrollador WHERE iddesarrollador=%s",(iddesarrollador,))
    mysql.connection.commit()
    ddes.close()
    return redirect(url_for('sdes'))

#-----------------------Juego---------------------------

@stamApp.route('/sg')
def sg():
    selg = mysql.connection.cursor()
    selg.execute("SELECT * FROM juego INNER JOIN dist ON juego.iddist = dist.iddist")
    j = selg.fetchall()
    selg.close()

    seldist = mysql.connection.cursor()
    seldist.execute("SELECT * FROM dist")
    di = seldist.fetchall()
    seldist.close()

    return render_template('juegos.html', dist=di, juegos=j) 

@stamApp.route('/ig', methods=["POST", "GET"]) 
def ig():
    													 

    version  = request.form['version']
    DLC  = request.form['DLC']
    nomreg  = request.form['nomreg']
    pg  = request.form['pg']
    genero  = request.form['genero']
    fechadist  = request.form['fechadist']
    compat  = request.form['compat']
    opgraficos  = request.form['opgraficos']
    valoracion  = request.form['valoracion']
    bloqueo  = request.form['bloqueo']
    pracio  = request.form['pracio']
    descripcion = request.form['descripcion']
    dn  = request.form['dn']
    iddist   = request.form['iddist']

        #------imagen----------
    file=request.files['imagen']
    target = os.path.join(APP_ROOT, 'static/file')
    if not os.path.isdir(target):
        os.makedirs(target)
    filename = file.filename
    destination = "/".join([target, filename])
    file.save(destination)
    datafile = open(destination, "rb")
    d = open("E:/server/stam/static/img/test.jpg", "wb")
    thedata = datafile.read()
    d.write(thedata)
    d.close()
    datafile.close()

    regPedido = mysql.connection.cursor()
    regPedido.execute("INSERT INTO juego (version, DLC, nomreg, pg, genero, fechadist, compat, opgraficos, valoracion, bloqueo, pracio, dn, descripcion, imagen, iddist) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (version, DLC, nomreg, pg, genero, fechadist, compat, opgraficos, valoracion, bloqueo, pracio, dn, descripcion, filename ,iddist))
    mysql.connection.commit()
    regPedido.close()
    return redirect (url_for('sg'))

@stamApp.route('/ug',methods = ["POST" , "GET"])
def ug():
    idg  = request.form['idg']
    version  = request.form['version']
    DLC  = request.form['DLC']
    nomreg  = request.form['nomreg']
    pg  = request.form['pg']
    genero  = request.form['genero']
    fechadist  = request.form['fechadist']
    compat  = request.form['compat']
    opgraficos  = request.form['opgraficos']
    valoracion  = request.form['valoracion']
    bloqueo  = request.form['bloqueo']
    pracio  = request.form['pracio']
    descripcion = request.form['descripcion']
    dn  = request.form['dn']
    iddist   = request.form['iddist']
            #------imagen----------
    file=request.files['imagen']
    target = os.path.join(APP_ROOT, 'static/file')
    if not os.path.isdir(target):
        os.makedirs(target)
    filename = file.filename
    destination = "/".join([target, filename])
    file.save(destination)
    datafile = open(destination, "rb")
    d = open("E:/server/stam/static/img/test.jpg", "wb")
    thedata = datafile.read()
    d.write(thedata)
    d.close()
    datafile.close()

    uus = mysql.connection.cursor()
    uus.execute("UPDATE juego SET version = %s,DLC = %s,nomreg = %s,pg = %s,genero = %s,fechadist = %s,compat = %s,opgraficos = %s,valoracion = %s,bloqueo = %s,pracio = %s,dn = %s,descripcion = %s, imagen =%s, iddist = %s WHERE idg=%s",(version, DLC, nomreg, pg, genero, fechadist, compat, opgraficos, valoracion, bloqueo, pracio, dn,descripcion,filename , iddist, idg ))
    mysql.connection.commit()
    return redirect(url_for('sg'))

@stamApp.route('/dg/<string:idg>', methods = ["GET"])
def dg(idg):
    ddes = mysql.connection.cursor()
    ddes.execute("DELETE FROM juego WHERE idg=%s",(idg,))
    mysql.connection.commit()
    ddes.close()
    return redirect(url_for('sg'))


    
#------------------------usuario--------------------#    



@stamApp.route('/sus',methods = ["POST" , "GET"])
def sus():
    sus =mysql.connection.cursor()
    sus.execute("SELECT * FROM usuario")
    a = sus.fetchall()
    return render_template('adminxusuarios.html', usr = a)

@stamApp.route('/ius',methods = ["POST" , "GET"])
def ius():
        region    = request.form['region']
        direccion    = request.form['direccion']
        nombreu    = request.form['nombreusuario']
        tarjeta    = request.form['tarjeta']
        contraseña   = request.form['contra'].encode('utf-8')
        clavecifrada = bcrypt.hashpw(contraseña, bcrypt.gensalt())
        ius = mysql.connection.cursor()
        ius.execute("INSERT INTO usuario (region,direccionfactura,nombreusuario,tarjeta,contra) VALUES (%s,%s,%s,%s, %s)",(region,direccion,nombreu,tarjeta,clavecifrada))
        mysql.connection.commit()
        return redirect(url_for('sus'))

@stamApp.route('/uus',methods = ["POST" , "GET"])
def uus():
        idu   = request.form['idu'] 
        region    = request.form['region']
        direccion    = request.form['direccion']
        nombreu    = request.form['nombreusuario']
        tarjeta    = request.form['tarjeta']
        contraseña   = request.form['contra'].encode('utf-8')
        clavecifrada = bcrypt.hashpw(contraseña, bcrypt.gensalt())
        uus = mysql.connection.cursor()
        uus.execute("UPDATE usuario SET region = %s,direccionfactura = %s,nombreusuario = %s,tarjeta = %s,contra = %s WHERE idu=%s",(region,direccion,nombreu,tarjeta,clavecifrada, idu))
        mysql.connection.commit()
        return redirect(url_for('sus'))

@stamApp.route('/dus/<string:idu>', methods = ["GET"])
def dus(idu):
    dus = mysql.connection.cursor()
    dus.execute("DELETE FROM usuario WHERE idu=%s",(idu,))
    mysql.connection.commit()
    return redirect(url_for('sus'))

# ------------------------transacción---------------------#


@stamApp.route('/stransaccion',methods = ["POST" , "GET"])
def stransaccion():
    Selpedido =mysql.connection.cursor()
    Selpedido.execute("SELECT * FROM transaccion INNER JOIN usuario  ON  transaccion.idu = usuario.idu INNER JOIN juego ON transaccion.idg = juego.idg")
    tuj = Selpedido.fetchall()
    Selpedido.close()
    
    Selempleado =mysql.connection.cursor()
    Selempleado.execute("SELECT * FROM usuario")
    u = Selempleado.fetchall()
    Selempleado.close()

    seljuego =mysql.connection.cursor()
    seljuego.execute("SELECT * FROM juego")
    j = seljuego.fetchall()
    seljuego.close()

    return render_template('transaccion.html', usu = u, juego = j, transaccion = tuj)


@stamApp.route('/itransaccion',methods = ["POST" , "GET"])
def itransaccion():
        NT      = 1
        metodo      = request.form['metodo']
        verificacion = request.form['verificasion']
        nu      = request.form['nu']

        Selempleado =mysql.connection.cursor()
        Selempleado.execute("SELECT * FROM usuario WHERE nombreusuario=%s",(nu,))
        u = Selempleado.fetchall()
        Selempleado.close()
        
        
        idg = request.form['idg']
        
        regbanda    = mysql.connection.cursor()
        regbanda.execute("INSERT INTO transaccion (NT, metodo, verificacion, idu, idg) VALUES (%s, %s, %s, %s, %s)",(NT, metodo, verificacion, idu, idg))
        mysql.connection.commit()
        return redirect(url_for('home'))

@stamApp.route('/utransaccion',methods = ["POST" , "GET"])
def utransaccion():
        idt   = request.form['idt'] 
        metodo      = request.form['metodo']
        NT      = request.form['NT']
        verificacion = request.form['verificacion']
        idu = request.form['idu']
        idg = request.form['idg']
        regUsuario = mysql.connection.cursor()
        regUsuario.execute("UPDATE transaccion SET NT = %s, metodo = %s, verificacion = %s, idu = %s, idg = %s, where idt=%s",(NT, metodo, verificacion, idu, idg, idt))
        mysql.connection.commit()
        return redirect(url_for('stransaccion'))

@stamApp.route('/dtransaccion/<string:idt>', methods = ["GET"])
def dtransaccion(idt):
    delempleado = mysql.connection.cursor()
    delempleado.execute("DELETE FROM transaccion WHERE idt=%s",(idt,))
    mysql.connection.commit()
    return redirect(url_for('stransaccion'))


if __name__ == '__main__':
    stamApp.secret_key='st '
    stamApp.run(host="0.0.0.0",port=3000, debug=True)
