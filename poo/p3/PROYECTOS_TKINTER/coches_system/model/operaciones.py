from conexionBD import conexion, cursor

def crear_tabla_autos():
    sql = '''CREATE TABLE IF NOT EXISTS autos (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        marca VARCHAR(60) NOT NULL,
        color VARCHAR(60) NOT NULL,
        modelo VARCHAR(4) NOT NULL,
        velocidad INT NOT NULL,
        caballaje INT NOT NULL,
        plazas INT NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;'''
    cursor.execute(sql)
    try:
        conexion.commit()
    except Exception:
        pass

def insertar_auto(marca, color, modelo, velocidad, caballaje, plazas):
    crear_tabla_autos()
    sql = "INSERT INTO autos (marca, color, modelo, velocidad, caballaje, plazas) VALUES (%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas))
    conexion.commit()
    return cursor.lastrowid

def obtener_autos():
    crear_tabla_autos()
    cursor.execute("SELECT id, marca, color, modelo, velocidad, caballaje, plazas FROM autos")
    return cursor.fetchall()

def actualizar_auto(id_, marca=None, color=None, modelo=None, velocidad=None, caballaje=None, plazas=None):
    crear_tabla_autos()
    fields = []
    params = []
    if marca is not None:
        fields.append('marca = %s')
        params.append(marca)
    if color is not None:
        fields.append('color = %s')
        params.append(color)
    if modelo is not None:
        fields.append('modelo = %s')
        params.append(modelo)
    if velocidad is not None:
        fields.append('velocidad = %s')
        params.append(velocidad)
    if caballaje is not None:
        fields.append('caballaje = %s')
        params.append(caballaje)
    if plazas is not None:
        fields.append('plazas = %s')
        params.append(plazas)
    if not fields:
        return 0
    sql = f"UPDATE autos SET {', '.join(fields)} WHERE id = %s"
    params.append(id_)
    cursor.execute(sql, tuple(params))
    conexion.commit()
    return cursor.rowcount

def eliminar_auto(id_):
    crear_tabla_autos()
    sql = "DELETE FROM autos WHERE id = %s"
    cursor.execute(sql, (id_,))
    conexion.commit()
    return cursor.rowcount

def crear_tabla_camiones():
    sql = '''CREATE TABLE IF NOT EXISTS camiones (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        marca VARCHAR(60) NOT NULL,
        color VARCHAR(60) NOT NULL,
        modelo VARCHAR(4) NOT NULL,
        velocidad INT NOT NULL,
        caballaje INT NOT NULL,
        plazas INT NOT NULL,
        eje INT NOT NULL,
        capacidadcarga INT NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;'''
    cursor.execute(sql)
    try:
        conexion.commit()
    except Exception:
        pass

def insertar_camion(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga):
    crear_tabla_camiones()
    sql = "INSERT INTO camiones (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga))
    conexion.commit()
    return cursor.lastrowid

def obtener_camiones():
    crear_tabla_camiones()
    cursor.execute("SELECT id, marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga FROM camiones")
    return cursor.fetchall()

def actualizar_camion(id_, marca=None, color=None, modelo=None, velocidad=None, caballaje=None, plazas=None, eje=None, capacidadcarga=None):
    crear_tabla_camiones()
    fields = []
    params = []
    if marca is not None:
        fields.append('marca = %s')
        params.append(marca)
    if color is not None:
        fields.append('color = %s')
        params.append(color)
    if modelo is not None:
        fields.append('modelo = %s')
        params.append(modelo)
    if velocidad is not None:
        fields.append('velocidad = %s')
        params.append(velocidad)
    if caballaje is not None:
        fields.append('caballaje = %s')
        params.append(caballaje)
    if plazas is not None:
        fields.append('plazas = %s')
        params.append(plazas)
    if eje is not None:
        fields.append('eje = %s')
        params.append(eje)
    if capacidadcarga is not None:
        fields.append('capacidadcarga = %s')
        params.append(capacidadcarga)
    if not fields:
        return 0
    sql = f"UPDATE camiones SET {', '.join(fields)} WHERE id = %s"
    params.append(id_)
    cursor.execute(sql, tuple(params))
    conexion.commit()
    return cursor.rowcount

def eliminar_camion(id_):
    crear_tabla_camiones()
    sql = "DELETE FROM camiones WHERE id = %s"
    cursor.execute(sql, (id_,))
    conexion.commit()
    return cursor.rowcount

def crear_tabla_camionetas():
    sql = '''CREATE TABLE IF NOT EXISTS camionetas (
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        marca VARCHAR(60) NOT NULL,
        color VARCHAR(60) NOT NULL,
        modelo VARCHAR(4) NOT NULL,
        velocidad INT NOT NULL,
        caballaje INT NOT NULL,
        plazas INT NOT NULL,
        traccion VARCHAR(60) NOT NULL,
        cerrada TINYINT(1) NOT NULL
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;'''
    cursor.execute(sql)
    try:
        conexion.commit()
    except Exception:
        pass

def insertar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
    crear_tabla_camionetas()
    sql = "INSERT INTO camionetas (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada))
    conexion.commit()
    return cursor.lastrowid

def obtener_camionetas():
    crear_tabla_camionetas()
    cursor.execute("SELECT id, marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada FROM camionetas")
    return cursor.fetchall()

def actualizar_camioneta(id_, marca=None, color=None, modelo=None, velocidad=None, caballaje=None, plazas=None, traccion=None, cerrada=None):
    crear_tabla_camionetas()
    fields = []
    params = []
    if marca is not None:
        fields.append('marca = %s')
        params.append(marca)
    if color is not None:
        fields.append('color = %s')
        params.append(color)
    if modelo is not None:
        fields.append('modelo = %s')
        params.append(modelo)
    if velocidad is not None:
        fields.append('velocidad = %s')
        params.append(velocidad)
    if caballaje is not None:
        fields.append('caballaje = %s')
        params.append(caballaje)
    if plazas is not None:
        fields.append('plazas = %s')
        params.append(plazas)
    if traccion is not None:
        fields.append('traccion = %s')
        params.append(traccion)
    if cerrada is not None:
        fields.append('cerrada = %s')
        params.append(cerrada)
    if not fields:
        return 0
    sql = f"UPDATE camionetas SET {', '.join(fields)} WHERE id = %s"
    params.append(id_)
    cursor.execute(sql, tuple(params))
    conexion.commit()
    return cursor.rowcount

def eliminar_camioneta(id_):
    crear_tabla_camionetas()
    sql = "DELETE FROM camionetas WHERE id = %s"
    cursor.execute(sql, (id_,))
    conexion.commit()
    return cursor.rowcount

__all__ = ['crear_tabla_autos', 'insertar_auto', 'obtener_autos', 'actualizar_auto', 'eliminar_auto',
           'crear_tabla_camiones', 'insertar_camion', 'obtener_camiones', 'actualizar_camion', 'eliminar_camion',
           'crear_tabla_camionetas', 'insertar_camioneta', 'obtener_camionetas', 'actualizar_camioneta', 'eliminar_camioneta']
