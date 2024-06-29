from django.db import models

# Create your models here.
class Cobertura(models.Model):
    nombre = models.CharField(max_length=50)
    descuento = models.DecimalField(max_digits=5, decimal_places=2)
    Especialidad = models.ForeignKey('Especialidad', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
class SeguroPaciente(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}'
    
class BeneficiosSeguro(models.Model):
    seguro = models.ForeignKey(SeguroPaciente, on_delete=models.CASCADE)
    beneficio = models.CharField(max_length=100)
    cobertura = models.ForeignKey(Cobertura, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.seguro.nombre} - {self.beneficio} - {self.cobertura.nombre}'
class Pacientes(models.Model):
    name= models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    dni = models.PositiveIntegerField()
    celp = models.PositiveIntegerField()
    address=models.CharField(max_length=100)
    fechaNac= models.DateField()
    seguro= models.ForeignKey(SeguroPaciente, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f' {self.name} {self.lastName}'

class Examen(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}'

class Especialidad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre}'

class Citas(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    fechaEmision = models.DateTimeField()
    fechaProgramada = models.DateTimeField()
    motivo = models.CharField(max_length=200)
    area=models.ForeignKey(Especialidad, on_delete=models.CASCADE,default=1)
    examen = models.ForeignKey(Examen, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f' {self.paciente.name} {self.paciente.lastName} el {self.fechaProgramada}'

class Ticket(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    nroTicket = models.CharField(max_length=20)
    fechaTicket = models.DateTimeField()
    estado = models.CharField(max_length=200)

    def __str__(self):
        return f' {self.nroTicket} {self.paciente}'
    

class HorarioMedico(models.Model):
    dia = models.DateField()
    horaInicio = models.TimeField()
    horaFin = models.TimeField()

    def __str__(self):
        return f' {self.dia} {self.horaInicio} {self.horaFin}'    

    
class Medicos(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    dni = models.PositiveIntegerField()
    celp = models.PositiveIntegerField()
    tipo = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    horario=models.ForeignKey(HorarioMedico, on_delete=models.CASCADE)
    

    def __str__(self):
        return f'{self.name} {self.lastName}'
    
class Historias(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    medico =models.ForeignKey(Medicos, on_delete=models.CASCADE)
    cita = models.ForeignKey(Citas,on_delete=models.CASCADE)
    observacion = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.paciente.name} {self.paciente.lastName} {self.medico.name} {self.cita}'

class SalaOperaciones(models.Model):
    nombre =models.CharField(max_length=100)
    estado=models.CharField(max_length=100)
    
    def __str__(self):
        return f' {self.nombre}'
    
class Tecnicos(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    dni = models.PositiveIntegerField()
    celp = models.PositiveIntegerField()
    tipo = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.name} {self.lastName}'

class Enfermeros(models.Model):
    name = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    dni = models.PositiveIntegerField()
    celp = models.PositiveIntegerField()
    tipo = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.name} {self.lastName}'
    
class EquipoMedico(models.Model):
    nombre = models.CharField(max_length=50)
    medicos = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    tecnicos = models.ForeignKey(Tecnicos, on_delete=models.CASCADE)
    enfermeros = models.ForeignKey(Enfermeros, on_delete=models.CASCADE)
    pacientes = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    sala = models.ForeignKey(SalaOperaciones, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    observacion = models.CharField(max_length=200)
    
    def __str__(self):
        return f'{self.nombre}'

class Recetas(models.Model):
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    cita = models.ForeignKey(Citas, on_delete=models.CASCADE)
    medicamento = models.CharField(max_length=50)
    dosis = models.CharField(max_length=50)
    observacion = models.CharField(max_length=200)

    def __str__(self):
        return f' {self.paciente.name} {self.paciente.lastName} {self.medico.name} {self.cita}'
    
