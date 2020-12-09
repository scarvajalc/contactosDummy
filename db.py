from pydantic import BaseModel


class Contacto(BaseModel):
    id: int
    nombre: str
    direccion: str
    telefono: str


contactos = {
    1: Contacto(id=1, nombre="pepe", direccion="cll3242", telefono="324234"),
    2: Contacto(id=2, nombre="maria", direccion="cll3242324", telefono="4354354"),
}


def obtener_lista_contactos():
    lista_contactos = []
    for contacto in contactos:
        lista_contactos.append(contactos[contacto])
    return lista_contactos


def obtener_contacto_por_id(id: int):
    if id in contactos:
        return contactos[id]
    else:
        return None


def crear_contacto(contacto: Contacto):
    if contacto.id in contactos:
        return False
    else:
        contactos[contacto.id] = contacto
        return True
