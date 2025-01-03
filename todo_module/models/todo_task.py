from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'ToDo Task'
    
    name = fields.Char(string='Nombre de la tarea', required=True)
    description = fields.Text(string='Descripción')
    is_done = fields.Boolean(string='¿Completada?')
    priority = fields.Integer(string='Prioridad', default=1)
