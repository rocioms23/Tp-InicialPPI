import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def mostrar_graficos():
    # Configuración estética
    sns.set(style="whitegrid")
    plt.rcParams["figure.figsize"] = (10, 6)

    # Cargar datasets
    empleados = pd.read_csv("data/tablas/empleado.csv")
    fichadas = pd.read_csv("data/tablas/fichada.csv")
    imagenes = pd.read_csv("data/tablas/imagen.csv")
    produccion = pd.read_csv("data/tablas/registro_produccion.csv")

    # 1. Distribución por nivel de acceso
    plt.figure()
    empleados['nivel_acceso'].value_counts().sort_index().plot(kind='bar', color='skyblue')
    plt.title("Distribución de empleados por nivel de acceso")
    plt.xlabel("Nivel de acceso")
    plt.ylabel("Cantidad de empleados")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()

    # 2. Histograma de fechas de ingreso
    plt.figure()
    empleados['fecha_ingreso'] = pd.to_datetime(empleados['fecha_ingreso'])
    empleados['fecha_ingreso'].dt.to_period('M').value_counts().sort_index().plot(kind='bar', color='lightgreen')
    plt.title("Empleados por mes de ingreso")
    plt.xlabel("Mes")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # 3. Mapa de calor: sector vs turno
    pivot = empleados.pivot_table(index='id_sector', columns='id_turno', aggfunc='size', fill_value=0)
    plt.figure()
    sns.heatmap(pivot, annot=True, cmap='Blues', fmt='d')
    plt.title("Relación entre sector y turno")
    plt.xlabel("ID Turno")
    plt.ylabel("ID Sector")
    plt.tight_layout()
    plt.show()

    # 4. Registro facial activo/inactivo
    plt.figure()
    empleados['registro_facial_activo'].value_counts().plot(
        kind='pie',
        labels=['Activo', 'Inactivo'],
        autopct='%1.1f%%',
        colors=['#66c2a5','#fc8d62']
    )
    plt.title("Estado del registro facial")
    plt.ylabel("")
    plt.tight_layout()
    plt.show()

    # 5. Producción total por tipo de producto
    plt.figure()
    sns.barplot(data=produccion, x='tipo_producto', y='cantidad_producida', estimator=sum, palette='pastel')
    plt.title("Producción total por tipo de producto")
    plt.xlabel("Tipo de producto")
    plt.ylabel("Unidades producidas")
    plt.tight_layout()
    plt.show()

    # 6. Desperdicio total por tipo de producto
    plt.figure()
    sns.barplot(
        data=produccion,
        x='tipo_producto',
        y='cantidad_desperdiciada',
        hue='tipo_producto',
        estimator=sum,
        palette='Reds',
        legend=False
    )
    plt.title("Desperdicio por tipo de producto")
    plt.xlabel("Tipo de producto")
    plt.ylabel("Unidades desperdiciadas")
    plt.tight_layout()
    plt.show()

    # 7. Eficiencia por sector (boxplot)
    plt.figure()
    sns.boxplot(
        data=produccion,
        x='id_sector',
        y='eficiencia',
        hue='id_sector',
        palette='coolwarm',
        legend=False
    )
    plt.title("Eficiencia por sector (%)")
    plt.xlabel("ID Sector")
    plt.ylabel("Eficiencia (%)")
    plt.tight_layout()
    plt.show()

   

# Ejecución directa
if __name__ == '__main__':
    mostrar_graficos()
