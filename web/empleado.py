from flask import render_template, Blueprint, session, flash, redirect, url_for, send_from_directory

import mysql.connector

empleado = Blueprint('empleado', __name__,
                     static_folder='../web/data/db_rostros', 
                     static_url_path='/fotos_empleados')

@empleado.route('/fotos_empleados/<path:filename>')
def servir_foto(filename):
    # The directory where your images are located
    media_dir = 'web/data/db_rostros'

    return send_from_directory(media_dir, filename)

@empleado.route('/')
def empleado_inicio():
    id_empleado = session.get('id_empleado', None)
    if not id_empleado:
        flash('Debes iniciar sesión para acceder a esta página.')
        print("a")
        return redirect(url_for('vistas.inicio'))

    db_connection = None
    try:
        db_connection = mysql.connector.connect(
            host="interchange.proxy.rlwy.net",
            user="root",
            port=51042,
            password="kQCBSPUMdAGOiWjpYRTXKoZjBWiuHqmF",
            database="railway"
        )
        cursor = db_connection.cursor(dictionary=True)
        
        sql_select_empleado = """SELECT 
                e.*, 
                s.nombre AS nombre_sector, 
                i.ubicacion_archivo AS ruta_imagen_perfil,
                r.nombre AS nombre_rol,
                r.rol AS autoridad
            FROM 
                empleados AS e 
            JOIN 
                sectores AS s ON e.id_sector = s.id 
            JOIN 
                imagenes AS i ON e.id_imagen = i.id 
            JOIN
                Puestos AS r ON e.id_rol = r.id
            WHERE 
                e.id = %s"""
        
        cursor.execute(sql_select_empleado, (id_empleado,))
        
        empleado_data = cursor.fetchone()

        if empleado_data:
            sector_empleado = empleado_data['id_sector'] # Asumiendo que existe una columna 'sector'

            sql_select_sector = """
                SELECT
                    e.*,
                    i.ubicacion_archivo AS ruta_imagen,
                    r.nombre AS nombre_rol
                FROM
                    empleados AS e
                JOIN
                    imagenes AS i ON e.id_imagen = i.id
                JOIN
                    Puestos AS r ON e.id_rol = r.id
                WHERE
                    e.id_sector = %s AND e.id != %s;
            """
            cursor.execute(sql_select_sector, (sector_empleado, id_empleado,))
            empleados_del_sector = cursor.fetchall()

            # 3. Pasar los datos a la plantilla
            return render_template(
                '/empleado/inicio-empleado.html',
                empleado=empleado_data,
                empleados_del_sector=empleados_del_sector
            )
        else:
            # No se encontraron los datos del empleado
            flash('No se encontraron los datos del empleado.')
            return redirect(url_for('vistas.inicio'))

    except mysql.connector.Error as err:
        flash(f"Error en la base de datos: {err}")
        return redirect(url_for('vistas.inicio'))
    finally:
        if db_connection and db_connection.is_connected():
            cursor.close()
            db_connection.close()


@empleado.route('/registro')
def empleado_registro():
    return render_template('/empleado/anadir_registro.html')


