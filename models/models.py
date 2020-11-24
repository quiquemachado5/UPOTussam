#-*- coding: utf-8 -*-
from odoo import models, fields, api


class Pasajero(models.Model):
    _name = 'upotussam.pasajero'
    _description = 'Gestión de pasajeros'

    nombre = fields.Char(string="Nombre", required=True, help="nombre del pasajero")
    dni = fields.Char(string="DNI", required=True, help="DNI del pasajero")
    fechaNacimiento = fields.Datetime('Fecha de nacimiento del pasajero')
    esMinusválido = fields.Selection([('verdadero','Verdadero'),
                                     ('falso','Falso'),],
                                     'Selecciona si un pasajero es minusválido o no')
    esEstudiante = fields.Selection([('verdadero','Verdadero'),
                                     ('falso','Falso'),],
                                     'Selecciona si un pasajero es estudiante o no')
    id_boleto = fields.Many2one('upotussam.boletos', string='Confirmed Boletos')                                     

class Boletos(models.Model):
    _name = 'upotussam.boletos'
    _description = 'Gestión de boletos'

    id_boleto = fields.Integer('ID del boleto')
    precio =  fields.Integer("Precio del boleto") 
    fecha = fields.Datetime('Fecha de la compra del boleto')
    realizaDescuento = fields.Selection([('verdadero','Verdadero'),
                                     ('falso','Falso'),],
                                     'Selecciona si un boleto realiza descuento o no')
    id_pasajero = fields.One2many('upotussam.pasajero', 'id_boleto', 'Confirmed Pasajero')
    id_descuento = fields.Many2many('upotussam.descuento', string='Confirmed Descuento')
    id_paradaPorLinea_Inicio = fields.One2many('upotussam.paradaPorLinea','id_boleto_inicio', string='Confirmed ParadaPorLineaOrigen')    
    id_paradaPorLinea_Destino = fields.One2many('upotussam.paradaPorLinea','id_boleto_destino', string='Confirmed ParadaPorLineaOrigen')    
    
class Conductor(models.Model):
    _name = 'upotussam.conductor'
    _description = 'Gestión de pasajeros'

    nombre = fields.Char(string="Nombre", required=True, help="nombre del pasajero")
    dni = fields.Char(string="DNI", required=True, help="DNI del pasajero")
    fechaNacimiento = fields.Datetime('Fecha de nacimiento del pasajero')
    id_nomina = fields.Many2one('upotussam.nomina', string='Confirmed Nomina')
    id_autobusLinea = fields.Many2one('upotussam.autobusLinea',string='Confirmed AutobusLinea')

class Autobus(models.Model):
    _name = 'upotussam.autobus'
    _description = 'Gestión de la flota de autobuses'

    modelo = fields.Char(string="Modelo", required=True, help="Modelo del autobús")
    matricula = fields.Char(string="Matricula", required=True, help="Matrícula del autobús")
    capacidad =  fields.Integer("Capacidad del autobús") 
    estaAdaptado = fields.Selection([('verdadero','Verdadero'),
                                     ('falso','Falso'),],
                                     'Selecciona si un autobus esta adaptado o no')
    id_autobusLinea = fields.Many2one('upotussam.autobusLinea',string='Confirmed AutobusLinea')

class AutobusLinea(models.Model):
    _name = 'upotussam.autobusLinea'
    _description = 'Gestión de Autobús_Linea'

    fecha = fields.Datetime('Fecha de la conducción de un autobús')  
    id_conductor = fields.One2many('upotussam.conductor','id_autobusLinea', string='Confirmed Conductor')
    id_autobus = fields.One2many('upotussam.autobus','id_autobusLinea', string='Confirmed Autobus')
    id_linea = fields.One2many('upotussam.linea','id_autobusLinea', string='Confirmed Linea')

class Lineas(models.Model):
    _name = 'upotussam.lineas'
    _description = 'Gestión de líneas'

    id_linea = fields.Integer('ID de la linea')
    numeroDeAutobuses = fields.Integer('Numero de autobuses que hay en una misma linea')
    id_autobusLinea = fields.Many2one('upotussam.autobusLinea',string='Confirmed AutobusLinea')
    id_paradaPorLinea = fields.Many2one('upotussam.paradaPorLinea',string='Confirmed ParadaPorLinea')

class ParadaPorLinea(models.Model):
    _name = 'upotussam.paradaPorLinea'
    _description = 'Gestión de parada por linea'

    precioParada = fields.Integer('Numero de autobuses que hay en una misma linea')
    id_linea = fields.One2many('upotussam.linea','id_paradaPorLinea', string='Confirmed Linea')
    id_parada = fields.Many2one('upotussam.paradas', string='Confirmed Paradas')
    id_boleto_inicio = fields.Many2one('upotussam.boleto',string='Confirmed Boleto')
    id_boleto_destino = fields.Many2one('upotussam.boleto',string='Confirmed Boleto')
    
class Paradas(models.Model):
    _name = 'upotussam.paradas'
    _description = 'Gestión de paradas'

    id_parada = fields.Integer('ID de la linea')
    ubicación = fields.Char(string="Ubicación", required=True, help="Ubicación de la parada")
    estaActivo = fields.Selection([('verdadero','Verdadero'),
                                     ('falso','Falso'),],
                                     'Selecciona si una parada esta activa o no')
    id_paradaPorLinea = fields.One2many('upotussam.paradaPorLinea','id_parada',string='Confiremd ParadaPorLinea')

class Nomina(models.Model):
    _name = 'upotussam.nomina'
    _description = 'Gestión de nomina de un conductor'

    sueldo = fields.Integer('Sueldo que cobra un conductor')
    id_conductor = fields.One2many('upotussam.conductor','id_nomina', string='Confirmed Conductor')

class Descuento(models.Model):
    _name = 'upotussam.descuento'
    _description = 'Gestión del descuento de un boleto'

    tipoDescuento = fields.Selection([('estudiante','Estudiante'),
                                     ('minusvalido','Minusvalido'),],
                                     'Selecciona el tipo de descuento del boleto')
    descontado = fields.Integer('Precio que se descuenta del boleto')
    id_boleto = fields.Many2many('upotussam.boleto', string='Confiremd Boleto')