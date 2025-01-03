{
    'name': 'ToDo Module',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Gestión básica de tareas',
    'description': """
Módulo básico que permite crear y administrar tareas sencillas.
""",
    'author': 'Jose Serrano',
    'depends': ['base'], 
    'data': [
        'security/ir.model.access.csv',
        'views/todo_task_views.xml',
    ],
    'installable': True,
    'application': True
}
