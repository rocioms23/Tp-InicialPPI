from flask import render_template, request, jsonify, Blueprint, flash
import base64, cv2
import numpy as np
from deepface import DeepFace
import os,sys
import csv, datetime

vistas = Blueprint('vistas', __name__)
@vistas.route('/')
def inicio():
    return render_template('inicio.html')

@vistas.route('/inicioCamara', methods=['GET', 'POST'])
def inicioCamara():
    return render_template('inicioCamara.html')

def registrar_rutas(app):
    @app.route('/verificar', methods=['POST'])
    def verificar():
        try:
            data = request.get_json()
            img_base64 = data["image"].split(",")[1]
            img_bytes = base64.b64decode(img_base64)

        # Convierte los bytes a una matriz de numpy
            nparr = np.frombuffer(img_bytes, np.uint8)
        
        # Lee la imagen con OpenCV
            frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Ahora 'frame' es la imagen de OpenCV que puedes procesar
            ruta_imagen_recibida = "web/data/db_rostros/imagen_recibida.jpg"
            cv2.imwrite(ruta_imagen_recibida, frame)
            if os.path.exists(ruta_imagen_recibida):
                print("Archivo de imagen recibido existe.")
            # Asegúrate de que la ruta a la imagen del empleado también sea correcta
                ruta_rostro_empleado = "web/data/db_rostros/rostro_empleado.png"

                if os.path.exists(ruta_rostro_empleado):
                    resultado=DeepFace.verify(ruta_imagen_recibida, ruta_rostro_empleado, model_name="Facenet", detector_backend="opencv")
                    verificado = resultado['verified']
                    print(verificado)
                    if verificado:
                        
                        rutaTablaFichada = "web/data/tablas/fichada.csv"
                        ahora = datetime.datetime.now()
                        fecha = ahora.strftime("%Y-%m-%d")
                        hora = ahora.strftime("%H:%M:%S")
                        id_Empleado= "002"
                        id_Fichada="023f"
                        id_Imagen="4442"
                        movimiento="Salida"
                        estado="Aceptado"

                        os.makedirs("web/data/tablas", exist_ok=True)
                        with open(rutaTablaFichada, 'a', newline='', encoding='utf-8') as f:
                            writer = csv.writer(f)
                            if not os.path.isfile(rutaTablaFichada):
                                writer.writerow(['id_fichada', 'id_empleado', 'id_imagen', 'tipo', 'fecha_hora', 'decision'])
                            writer.writerow([id_Fichada,id_Empleado,id_Imagen,movimiento,fecha+"T"+hora,estado])
                        
                        print("Listo")
  
                        return jsonify({"status": "success", "message": "Rostro Verificado correctamente.", "verified": True})
                    else:
                        return jsonify({"status": "error", "message": "Imágenes verificadas incorrectamente.", "verified": False})
                else:
                     return jsonify({"status": "error", "message": "El archivo de la imagen del empleado no se encontró."}), 404
            else:
                return jsonify({"status": "error", "message": "No se pudo guardar la imagen recibida."}), 500
            
        except Exception as e:
            return jsonify({"status": "error", "message": str(e)}), 500
