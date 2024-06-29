from import_export import resources
from .models import Pacientes,Medicos

class PacientesResource(resources.ModelResource):
    class meta:
        model = Pacientes

class MedicosResource(resources.ModelResource):
    class meta:
        model = Medicos