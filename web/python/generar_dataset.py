def generar_dataset():
    import csv
    import os
    import random 
    from datetime import datetime, timedelta
    
    # Crear carpeta de salida
    os.makedirs('data/tablas', exist_ok=True)
    
    # Tabla: Empleado 
    empleados = [
            ['001', '20240001', '2021-01-02', 'Ildefonso', 'Juárez', 4, 3, 1, True, ' '],
            ['002', '20240002', '2022-06-24', 'Régulo', 'Benito', 1, 3, 2, True, ' '],
            ['003', '20240003', '2024-01-19', 'Guiomar', 'Borrell', 1, 1, 2, True, ' '],
            ['004', '20240004', '2022-10-11', 'Joel', 'Melero', 3, 1, 3, True, ' '],
            ['005', '20240005', '2020-12-03', 'María', 'Corral', 2, 3, 1, True, ' '],
            ['006', '20240006', '2022-05-17', 'Heriberto', 'Abella', 1, 2, 2, True, ' '],
            ['007', '20240007', '2022-01-25', 'Trinidad', 'Leon', 2, 3, 3, True, ' '],
            ['008', '20240008', '2020-09-16', 'Josué', 'Suarez', 1, 1, 1, True, ' '],
            ['009', '20240009', '2020-10-15', 'César', 'Catalá', 4, 3, 3, True, ' '],
            ['010', '20240010', '2023-12-23', 'Federico', 'Lillo', 4, 2, 2, True, ' '],
            ['011', '20240011', '2023-09-22', 'Celestino', 'Almeida', 4, 3, 3, True, ' '],
            ['012', '20240012', '2025-07-12', 'Leonor', 'Iglesias', 1, 1, 3, True, ' '],
            ['013', '20240013', '2021-03-02', 'Feliciana', 'Vázquez', 3, 3, 1, True, ' '],
            ['014', '20240014', '2023-09-30', 'Lina', 'Raya', 1, 1, 3, True, ' '],
            ['015', '20240015', '2021-03-29', 'Adela', 'Giner', 2, 1, 2, True, ' '],
            ['016', '20240016', '2024-10-31', 'Iris', 'Vidal', 2, 3, 3, True, ' '],
            ['017', '20240017', '2024-10-01', 'Valentina', 'Navarrete', 2, 3, 3, True, ' '],
            ['018', '20240018', '2021-08-15', 'Rosalina', 'Sedano', 3, 1, 2, True, ' '],
            ['019', '20240019', '2025-09-20', 'Blanca', 'Azcona', 1, 1, 3, False, ' '],
            ['020', '20240020', '2025-10-14', 'Charo', 'Abad', 3, 1, 2, False, ' ']
    ]
    
    with open('data/tablas/empleado.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id_empleado', 'legajo', 'fecha_ingreso', 'nombre', 'apellido', 'id_sector', 'id_turno', 'nivel_acceso', 'registro_facial_activo', 'observacion'])
        writer.writerows(empleados)

    # Tabla: Sector
    sectores = [
        [1, 'Producción', 'Transformación de materias primas en productos elaborados'],
        [2, 'Logística', 'Gestión de transporte, carga y descarga de productos'],
        [3, 'Calidad', 'Supervisión de normas sanitarias y control de procesos'],
        [4, 'Administración', 'Tareas administrativas, planificación y soporte']
    ]
    with open('data/tablas/sector.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id_sector', 'nombre', 'detalle'])
        writer.writerows(sectores)

    # Tabla: Turno
    turnos = [
        [1, 'Mañana', 'Turno matutino', '06:00:00', '14:00:00', '00:15:00', '00:10:00'],
        [2, 'Tarde', 'Turno vespertino', '14:00:00', '22:00:00', '00:15:00', '00:10:00'],
        [3, 'Noche', 'Turno nocturno', '22:00:00', '06:00:00', '00:15:00', '00:10:00']
    ]
    with open('data/tablas/turno.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id_turno', 'nombre', 'observacion', 'hora_entrada', 'hora_salida', 'tolerancia_entrada', 'tolerancia_salida'])
        writer.writerows(turnos)


    # Tabla: Imagen (simulada)
    imagenes = []
    for i in range(1, 21):
        for j in range(1, 6):  # 5 imágenes por empleado
            id_img = f'{i:02}{j:02}'
            imagenes.append([id_img, f'{i:03}', f'empleado_{i:03}_{j}.jpg', f'imagenes/empleado_{i:03}_{j}.jpg'])
            
            
    with open('data/tablas/imagen.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id_imagen', 'id_empleado', 'nombre_archivo', 'ubicacion_archivo'])
        writer.writerows(imagenes)

    # Tabla: Fichada (simulada)
    fichadas = []
    for i in range(1, 21):
        fecha_base = datetime(2025, 8, 24, 8, 0)
        for tipo in ['entrada', 'salida']:
            id_fichada = f'{i:03}{tipo[:1]}'
            id_imagen = f'{i:02}01'
            fecha_hora = (fecha_base + timedelta(hours=0 if tipo == 'entrada' else 8)).isoformat() + '-03:00'
            decision = 'Aceptada' if tipo == 'entrada' else 'Aceptada'
            fichadas.append([id_fichada, f'{i:03}', id_imagen, tipo, fecha_hora, decision])

    with open('data/tablas/fichada.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id_fichada', 'id_empleado', 'id_imagen', 'tipo', 'fecha_hora', 'decision'])
        writer.writerows(fichadas)


    # Tabla: Registro de Producción (simulada)
    registro_produccion = [
        ['PR001','2025-08-17','Tipo_A','97','9','4.59','1','90.72'],
        ['PR002','2025-08-23','Tipo_B','122','16','4.25','3','86.89'],
        ['PR003','2025-08-07','Tipo_C','125','10','2.0','1','92.0'],
        ['PR004','2025-08-23','Tipo_A','117','8','4.17','2','93.16'],
        ['PR005','2025-08-15','Tipo_A','142','19','4.79','2','86.62'],
        ['PR006','2025-08-10','Tipo_A','86','8','4.77','1','90.7'],
        ['PR007','2025-08-11','Tipo_C','89','10','3.68','1','88.76'],
        ['PR008','2025-08-12','Tipo_A','81','15','2.09','2','81.48'],
        ['PR009','2025-08-06','Tipo_B','145','6','4.04','1','95.86'],
        ['PR010','2025-08-18','Tipo_B','89','6','4.97','1','93.26'],
        ['PR011','2025-08-19','Tipo_C','121','10','3.25','3','91.74'],
        ['PR012','2025-08-14','Tipo_C','131','13','3.45','1','90.08'],
        ['PR013','2025-08-16','Tipo_C','108','8','2.64','3','92.59'],
        ['PR014','2025-08-01','Tipo_C','83','20','4.92','1','75.9'],
        ['PR015','2025-08-08','Tipo_C','95','19','3.87','2','80.0'],
        ['PR016','2025-08-03','Tipo_B','142','20','4.59','3','85.92'],
        ['PR017','2025-08-12','Tipo_C','133','13','3.79','3','90.23'],
        ['PR018','2025-08-16','Tipo_C','104','20','4.9','1','80.77'],
        ['PR019','2025-08-14','Tipo_C','149','11','4.74','1','92.62'],
        ['PR020','2025-08-22','Tipo_A','108','16','3.6','1','85.19'],
        ['PR021','2025-08-18','Tipo_C','120','7','3.44','1','94.17'],
        ['PR022','2025-08-16','Tipo_C','94','11','4.26','2','88.3'],
        ['PR023','2025-08-20','Tipo_C','109','16','3.07','3','85.32'],
        ['PR024','2025-08-24','Tipo_B','121','18','2.07','1','85.12'],
        ['PR025','2025-08-02','Tipo_C','95','16','2.74','2','83.16'],
        ['PR026','2025-08-23','Tipo_A','119','8','4.28','3','93.28'],
        ['PR027','2025-08-09','Tipo_C','98','18','4.78','1','81.63'],
        ['PR028','2025-08-22','Tipo_B','149','11','3.58','2','92.62'],
        ['PR029','2025-08-03','Tipo_B','134','6','3.83','1','95.52'],
        ['PR030','2025-08-07','Tipo_C','87','7','2.48','2','91.95']     
    ]
    
    with open('data/tablas/registro_produccion.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            'id_registro', 'fecha', 'tipo_producto', 'cantidad_producida',
            'cantidad_desperdiciada', 'tiempo_produccion', 'id_sector', 'eficiencia'
        ])
        writer.writerows(registro_produccion)



    print("Tablas generadas correctamente en: data/tablas/")

if __name__ == '__main__':
    generar_dataset()

