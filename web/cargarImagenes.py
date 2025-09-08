import mysql.connector
from deepface import DeepFace
import numpy as np
import os
import json

def generar_y_guardar_vectores(directorio_imagenes):

    db_connection = mysql.connector.connect(
        host="interchange.proxy.rlwy.net",
        user="root",
        port=51042,
        password="kQCBSPUMdAGOiWjpYRTXKoZjBWiuHqmF",
        database="railway"
    )
    cursor = db_connection.cursor()
    
    for filename in os.listdir(directorio_imagenes):
        if filename.endswith((".jpg", ".jpeg", ".png")):
            filepath = os.path.join(directorio_imagenes, filename)

            try:
                embedding = DeepFace.represent(img_path=filepath, model_name="Facenet512", enforce_detection=False)[0]['embedding']
                
                embedding_json = json.dumps(embedding)
                id_empleado = int(filename.split('.')[0].replace('empleado', ''))
                print (id_empleado)

                sql = "UPDATE imagenes SET vector_imagen = %s, ubicacion_archivo = %s WHERE id_empleado = %s"
                val = (embedding_json, filepath, id_empleado)

                cursor.execute(sql, val)

            except Exception as e:
                print(f"No se pudo procesar {filename}: {e}")

    db_connection.commit()

    cursor.close()
    db_connection.close()
    print("Proceso de carga de vectores finalizado.")
