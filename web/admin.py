from flask import render_template, Blueprint,  flash, redirect, url_for, session, send_from_directory
import mysql.connector

admin = Blueprint('admin', __name__,static_folder='../web/data/db_rostros', static_url_path='/fotos_empleados')

@admin.route('/fotos_empleados/<path:filename>')
def servir_foto(filename):
    # The directory where your images are located
    media_dir = 'web/data/db_rostros'

    return send_from_directory(media_dir, filename)

@admin.route('/')
def admin_inicio():
    session['id_empleado'] = 6
    id_empleado = session.get('id_empleado', None)
    
    if not id_empleado:
         flash('Debes iniciar sesión para acceder a esta página.')
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
                r.nombre AS nombre_rol 
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
            cursor.execute(sql_select_sector, (1, id_empleado,))
            empleados_del_sector1 = cursor.fetchall()

            cursor.execute(sql_select_sector, (2, id_empleado,))
            empleados_del_sector2 = cursor.fetchall()

            cursor.execute(sql_select_sector, (3, id_empleado,))
            empleados_del_sector3 = cursor.fetchall()

            cursor.execute(sql_select_sector, (4, id_empleado,))
            empleados_del_sector4 = cursor.fetchall()

            cursor.execute(sql_select_sector, (5, id_empleado,))
            empleados_del_sector5 = cursor.fetchall()

            # 3. Pasar los datos a la plantilla
            return render_template(
                '/admin/inicio-admin.html',
                empleado=empleado_data,
                empleados_del_sector1=empleados_del_sector1, empleados_del_sector2=empleados_del_sector2, empleados_del_sector3=empleados_del_sector3,
                empleados_del_sector4=empleados_del_sector4, empleados_del_sector5=empleados_del_sector5
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

@admin.route('/estadisticas')
def estadisticas():
    from .visualizar_dataset import generar_graficos
    generar_graficos()
    return render_template('/admin/estadistica-admin.html')

@admin.route('/actividad')
def actividad_empleados():
    id_empleado = session.get('id_empleado', None)
    if not id_empleado:
         flash('Debes iniciar sesión para acceder a esta página.')
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
        
        sql_select_fichada = """SELECT f.*,
        e.nombre AS nombre_empleado, 
        e.apellido AS apellido_empleado, 
        i_perfil.ubicacion_archivo AS foto_perfil,
        f.imagen AS foto_movimiento,
        s.nombre AS sector
        FROM
            fichada AS f
        JOIN
            empleados AS e ON f.id_empleado=e.id
        JOIN
            imagenes AS i_perfil ON e.id_imagen=i_perfil.id
        JOIN
            sectores AS s ON e.id_sector=s.id
        """
        
        cursor.execute(sql_select_fichada)
        movimientos = cursor.fetchall()
        return render_template('/admin/actividad-admin.html', movimientos=movimientos)
       

    except mysql.connector.Error as err:
        flash(f"Error en la base de datos: {err}")
        return redirect(url_for('admin.admin_inicio'))
    finally:
        if db_connection and db_connection.is_connected():
            cursor.close()
            db_connection.close()

@admin.route('/registros')
def registros():
    return render_template('/admin/registros.html')
