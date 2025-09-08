import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mysql.connector


def generar_graficos():
    # Configuración estética
    sns.set(style="whitegrid")
    plt.rcParams["figure.figsize"] = (10, 6)
    try:

        db_connection = mysql.connector.connect(
        host="interchange.proxy.rlwy.net",
        user="root",
        port=51042,
        password="kQCBSPUMdAGOiWjpYRTXKoZjBWiuHqmF",
        database="railway"
        )

        # Cargar datasets
        empleados = pd.read_sql_query("SELECT e.id, e.id_rol, e.fecha_ingreso, t.nombre AS nombre_turno , s.nombre AS nombre_sector FROM empleados AS e JOIN sectores AS s ON e.id_sector = s.id JOIN turnos AS t ON e.id_turno = t.id;", db_connection)
        produccion = pd.read_sql_query("SELECT * FROM productos", db_connection)

        # 1. Distribución por nivel de acceso
        plt.figure()
        empleados['id_rol'].value_counts().sort_index().plot(kind='bar', color='skyblue')
        plt.title("Distribución de empleados por rol")
        plt.xlabel("Rol")
        plt.ylabel("Cantidad de empleados")
        plt.xticks(rotation=0)
        plt.tight_layout()
        plt.savefig("web/static/assets/graficos/nivel_acceso.png")

        # 2. Histograma de fechas de ingreso
        plt.figure()
        plt.figure()
        empleados['fecha_ingreso'] = pd.to_datetime(empleados['fecha_ingreso'])
        empleados['fecha_ingreso'].dt.to_period('M').value_counts().sort_index().plot(kind='bar', color='lightgreen')   
        plt.title("Empleados por mes de ingreso")
        plt.xlabel("Mes")
        plt.ylabel("Cantidad")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig("web/static/assets/graficos/fecha_acceso.png")

        # 3. Mapa de calor: sector vs turno
        pivot = empleados.pivot_table(index='nombre_sector', columns='nombre_turno', aggfunc='size', fill_value=0)
        plt.figure()
        sns.heatmap(pivot, annot=True, cmap='Blues', fmt='d')
        plt.title("Relación entre sector y turno")
        plt.xlabel("Turno")
        plt.ylabel("Sector")
        plt.tight_layout()
        plt.savefig("web/static/assets/graficos/turnos.png")

        # 5. Producción total por tipo de producto
        plt.figure()
        sns.barplot(data=produccion, x='tipo', y='cantidad', estimator=sum, palette='pastel')
        plt.title("Producción total por tipo de producto")
        plt.xlabel("Tipo de producto")
        plt.ylabel("Unidades producidas")
        plt.tight_layout()
        plt.savefig("web/static/assets/graficos/produccion.png")

        # 6. Desperdicio total por tipo de producto
        plt.figure()
        sns.barplot(
            data=produccion,
            x='tipo',
            y='cant_descartada',
            hue='tipo',
            estimator=sum,
            palette='Reds',
            legend=False
        )
        plt.title("Desperdicio por tipo de producto")
        plt.xlabel("Tipo de producto")
        plt.ylabel("Unidades desperdiciadas")
        plt.tight_layout()
        plt.savefig("web/static/assets/graficos/desperdicio.png")


    except Exception as e:
        print("Error al conectar la base:", e)
    finally:
        if 'db_connection' in locals() and db_connection.is_connected():
            db_connection.close()

   