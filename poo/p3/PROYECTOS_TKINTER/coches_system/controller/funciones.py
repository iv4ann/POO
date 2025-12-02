from model.operaciones import insertar_auto, obtener_autos, actualizar_auto, eliminar_auto
from model.operaciones import (
    insertar_camion, obtener_camiones, actualizar_camion, eliminar_camion,
    insertar_camioneta, obtener_camionetas, actualizar_camioneta, eliminar_camioneta
)

def insertar_auto_controller(marca, color, modelo, velocidad, caballaje, plazas):
    # Basic validation and conversion (fields are required by SQL schema)
    if not all([marca, color, modelo]):
        raise ValueError('Marca, color y modelo son obligatorios')
    try:
        velocidad = int(velocidad)
    except Exception:
        raise ValueError('Velocidad debe ser un número')
    try:
        caballaje = int(caballaje)
    except Exception:
        raise ValueError('Caballaje debe ser un número')
    try:
        plazas = int(plazas)
    except Exception:
        raise ValueError('Plazas debe ser un número')
    return insertar_auto(marca, color, modelo, velocidad, caballaje, plazas)

def consultar_autos_controller():
    rows = obtener_autos()
    return [
        {
            'id': r[0], 'marca': r[1], 'color': r[2], 'modelo': r[3],
            'velocidad': r[4], 'caballaje': r[5], 'plazas': r[6]
        } for r in rows
    ]

def actualizar_auto_controller(id_, **kwargs):
    if not id_:
        raise ValueError('El ID es obligatorio')
    if 'velocidad' in kwargs and kwargs['velocidad'] != '':
        try:
            kwargs['velocidad'] = int(kwargs['velocidad'])
        except Exception:
            raise ValueError('Velocidad debe ser un número')
    if 'caballaje' in kwargs and kwargs['caballaje'] != '':
        try:
            kwargs['caballaje'] = int(kwargs['caballaje'])
        except Exception:
            raise ValueError('Caballaje debe ser un número')
    if 'plazas' in kwargs and kwargs['plazas'] != '':
        try:
            kwargs['plazas'] = int(kwargs['plazas'])
        except Exception:
            raise ValueError('Plazas debe ser un número')
    return actualizar_auto(int(id_), **{k: v for k, v in kwargs.items() if v != ''})

def eliminar_auto_controller(id_):
    if not id_:
        raise ValueError('El ID es obligatorio')
    return eliminar_auto(int(id_))

__all__ = ['insertar_auto_controller', 'consultar_autos_controller', 'actualizar_auto_controller', 'eliminar_auto_controller']

def insertar_camion_controller(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga):
    if not all([marca, color, modelo]):
        raise ValueError('Marca, color y modelo son obligatorios')
    try:
        velocidad = int(velocidad)
        caballaje = int(caballaje)
        plazas = int(plazas)
        eje = int(eje)
        capacidadcarga = int(capacidadcarga)
    except Exception:
        raise ValueError('Velocidad, caballaje, plazas, eje y capacidadcarga deben ser números')
    return insertar_camion(marca, color, modelo, velocidad, caballaje, plazas, eje, capacidadcarga)

def consultar_camiones_controller():
    rows = obtener_camiones()
    return [
        {
            'id': r[0], 'marca': r[1], 'color': r[2], 'modelo': r[3],
            'velocidad': r[4], 'caballaje': r[5], 'plazas': r[6], 'eje': r[7], 'capacidadcarga': r[8]
        } for r in rows
    ]

def actualizar_camion_controller(id_, **kwargs):
    if not id_:
        raise ValueError('El ID es obligatorio')
    def _int_field(k):
        try:
            return int(kwargs[k])
        except Exception:
            raise ValueError(f'{k} debe ser un número')
    for k in ('velocidad', 'caballaje', 'plazas', 'eje', 'capacidadcarga'):
        if k in kwargs and kwargs[k] != '':
            kwargs[k] = _int_field(k)
    return actualizar_camion(int(id_), **{k: v for k, v in kwargs.items() if v != ''})

def eliminar_camion_controller(id_):
    if not id_:
        raise ValueError('El ID es obligatorio')
    return eliminar_camion(int(id_))

def insertar_camioneta_controller(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada):
    if not all([marca, color, modelo, traccion]):
        raise ValueError('Marca, color, modelo y traccion son obligatorios')
    try:
        velocidad = int(velocidad)
        caballaje = int(caballaje)
        plazas = int(plazas)
        # Cerrar as boolean-ish: allow '0','1' or True/False
        cerrada = 1 if str(cerrada) in ('1', 'True', 'true', 't', 'yes') else 0
    except Exception:
        raise ValueError('Velocidad, caballaje y plazas deben ser números')
    return insertar_camioneta(marca, color, modelo, velocidad, caballaje, plazas, traccion, cerrada)

def consultar_camionetas_controller():
    rows = obtener_camionetas()
    return [
        {
            'id': r[0], 'marca': r[1], 'color': r[2], 'modelo': r[3],
            'velocidad': r[4], 'caballaje': r[5], 'plazas': r[6], 'traccion': r[7], 'cerrada': r[8]
        } for r in rows
    ]

def actualizar_camioneta_controller(id_, **kwargs):
    if not id_:
        raise ValueError('El ID es obligatorio')
    if 'velocidad' in kwargs and kwargs['velocidad'] != '':
        try:
            kwargs['velocidad'] = int(kwargs['velocidad'])
        except Exception:
            raise ValueError('Velocidad debe ser un número')
    if 'caballaje' in kwargs and kwargs['caballaje'] != '':
        try:
            kwargs['caballaje'] = int(kwargs['caballaje'])
        except Exception:
            raise ValueError('Caballaje debe ser un número')
    if 'plazas' in kwargs and kwargs['plazas'] != '':
        try:
            kwargs['plazas'] = int(kwargs['plazas'])
        except Exception:
            raise ValueError('Plazas debe ser un número')
    if 'cerrada' in kwargs and kwargs['cerrada'] != '':
        kwargs['cerrada'] = 1 if str(kwargs['cerrada']) in ('1', 'True', 'true', 't', 'yes') else 0
    return actualizar_camioneta(int(id_), **{k: v for k, v in kwargs.items() if v != ''})

def eliminar_camioneta_controller(id_):
    if not id_:
        raise ValueError('El ID es obligatorio')
    return eliminar_camioneta(int(id_))

__all__ += ['insertar_camion_controller', 'consultar_camiones_controller', 'actualizar_camion_controller', 'eliminar_camion_controller',
            'insertar_camioneta_controller', 'consultar_camionetas_controller', 'actualizar_camioneta_controller', 'eliminar_camioneta_controller']
