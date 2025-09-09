from flask import render_template, request, jsonify, Blueprint, session, redirect, url_for
import base64, cv2, os, csv, datetime, mysql.connector, json, uuid
import numpy as np
from deepface import DeepFace

vistas = Blueprint('vistas', __name__)
@vistas.route('/')
def inicio():
    return render_template('inicio.html')

@vistas.route('/inicioCamara', methods=['GET', 'POST'])
def inicioCamara():
    return render_template('inicioCamara.html')

@vistas.route('/cerrarSesion')
def cerrarSesion():
    session.clear()
    return redirect(url_for('vistas.inicio'))

@vistas.route('/verificarAdmin', methods=['GET','POST'])
def verificarAdmin():
    db_connection = None
    cursor = None
    try:
        data = request.get_json()
        email = data.get('email')
        contrasena = data.get('contrasena')

        # Si los datos no se recibieron, retornar un error
        if not email or not contrasena:
            return jsonify({"status": "error", "message": "Datos de inicio de sesión incompletos"}), 400
        
        db_connection = mysql.connector.connect(
        host="interchange.proxy.rlwy.net",
        user="root",
        port=51042,
        password="kQCBSPUMdAGOiWjpYRTXKoZjBWiuHqmF",
        database="railway"
        )

        cursor = db_connection.cursor(dictionary=True)
        sql_select_vectors = "SELECT * FROM cuentas WHERE correo = %s AND contrasena = %s"
        cursor.execute(sql_select_vectors, (email, contrasena,))
        usuario = cursor.fetchone()
        existe=False
        if(usuario):
            existe=True
            session['id_empleado'] = usuario['id_empleado']
            return jsonify({"status": "success", "message": "Inicio de sesión exitoso", "existe": existe}), 200
        else:
             return jsonify({"status": "error", "message": "Correo o contraseña incorrectos","existe":existe}), 401
        
    except mysql.connector.Error as err:
        return jsonify({"status": "error", "message": f"Error de base de datos: {err}"}), 500

    except Exception as e:
        error=jsonify({"status": "error", "message": str(e)})
        print(error)
        return error, 502
    finally:
        if cursor:
            cursor.close()
        if db_connection and db_connection.is_connected():
            cursor.close()
            db_connection.close()
    


@vistas.route('/verificar', methods=['POST'])
def verificar():
    try:
    
        db_connection = mysql.connector.connect(
        host="interchange.proxy.rlwy.net",
        user="root",
        port=51042,
        password="kQCBSPUMdAGOiWjpYRTXKoZjBWiuHqmF",
        database="railway"
        )
        cursor = db_connection.cursor(dictionary=True)
        sql_select_vectors = "SELECT e.id, i.vector_imagen AS vector_imagen FROM empleados AS e JOIN imagenes AS i ON e.id_imagen= i.id"
        cursor.execute(sql_select_vectors)
        db_vectors = cursor.fetchall()

        data = request.get_json()
        img_base64 = data["image"].split(",")[1]
        img_bytes = base64.b64decode(img_base64)

        nparr = np.frombuffer(img_bytes, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        embedding_recibido = DeepFace.represent(img_path=frame, model_name="Facenet512",enforce_detection=False)[0]['embedding']

        match_found = False
        id_empleado_encontrado = None

        for columna in db_vectors:
            db_id_empleado = columna['id']
            db_embedding_json = columna['vector_imagen']
            db_embedding = json.loads(db_embedding_json)

            from numpy.linalg import norm
            distancia_coseno = 1 - np.dot(embedding_recibido, db_embedding) / (norm(embedding_recibido) * norm(db_embedding))

            if distancia_coseno < 0.25: 
                match_found = True
                id_empleado_encontrado = db_id_empleado
                
                break
        
        if match_found:
            ahora = datetime.datetime.utcnow()
            movimiento = "Entrada" 
            estado = "Aceptada"
            horaArchivo = ahora.strftime('%Y%m%d_%H%M%S')
            nombreArchivo=f"movimientoEmpleado_{id_empleado_encontrado}_{horaArchivo}.jpg"
            direccionImagen = "web/data/db_rostros/movimientos"
            ruta_imagen_movimiento = os.path.join(direccionImagen, nombreArchivo)
            cv2.imwrite(ruta_imagen_movimiento, frame)
            
            sql_insert_fichada = """
                INSERT INTO fichada (id_empleado, imagen, tipo, fecha_hora, decision) 
                VALUES (%s, %s, %s, %s, %s)
            """
            val = (id_empleado_encontrado,ruta_imagen_movimiento, movimiento, ahora, estado)
            cursor.execute(sql_insert_fichada, val)
            db_connection.commit()

            session['id_empleado'] = id_empleado_encontrado
            return jsonify({"status": "success", "message": "Rostro verificado y fichada registrada.", "verified": True})
        else:
            return jsonify({"status": "error", "message": "No se encontró coincidencia.", "verified": False})
        
    except Exception as e:
        error=jsonify({"status": "error", "message": str(e)})
        print(error)
        return error, 5002
    finally:
        if db_connection and db_connection.is_connected():
            cursor.close()
            db_connection.close()
