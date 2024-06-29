from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.utils.timezone import localtime, now

class PacientesForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = [ 'name', 'lastName','email','dni', 'celp', 'address', 'fechaNac', 'seguro']
        labels = {'name': 'Nombre',
                  'lastName': 'Apellido',
                  'email': 'Correo',
                  'dni': 'Numero de DNI',
                  'celp': 'Telefono',
                  'address': 'Direccion',
                  'fechaNac': 'Fecha de Nacimiento',
                  'seguro': 'Seguro'
                  }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'celp': forms.NumberInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaNac': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'seguro': forms.Select(attrs={'class': 'form-control'}),
        }


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True, label='username', help_text='',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label='email', help_text='',
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, label='Nombre', help_text='',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, label='Apellido', help_text='',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Clave', widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text='')
    password2 = forms.CharField(label='Repetir Clave', widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                                help_text='')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    username = forms.CharField(required=True, label='username', help_text='',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, label='email', help_text='',
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True, label='Nombre', help_text='',
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, label='Apellido', help_text='',
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = None

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})


class ImportExcelForm(forms.Form):
    my_file = forms.FileField(label='Cargar archivo de Excel')


class CitaForm(forms.ModelForm):

        class Meta:
            model = Citas
            fields = ('paciente', 'fechaEmision', 'fechaProgramada', 'motivo','area','examen')
            widgets = {
                'paciente': forms.Select(attrs={'class': 'form-control'}),
                'fechaEmision': forms.DateTimeInput(attrs={'class': 'form-control', 'value': localtime(now()).strftime('%Y-%m-%dT%H:%M:%S'), 'type': 'datetime-local'}),
                'fechaProgramada': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
                'motivo': forms.Textarea(attrs={'class': 'form-control'}),
                'area': forms.Select(attrs={'class': 'form-control'}),
                'examen': forms.Select(attrs={'class': 'form-control'}),
            }
            labels = {
                'paciente': _('Paciente'),
                'fechaEmision': _('Fecha de emisión'),
                'fechaProgramada': _('Fecha programada'),
                'motivo': _('motivo'),
                'area': _('Area'),
                'examen':_('Examen'),
            }


class TicketForm(forms.ModelForm):
    ESTADO_CHOICES = (
        ('Pendiente', 'Pendiente'),
        ('Atendido', 'Atendido'),
    )

    estado = forms.ChoiceField(choices=ESTADO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Ticket
        fields = ('paciente', 'fechaTicket', 'estado')
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'fechaTicket': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
        labels = {
            'paciente': _('Paciente'),
            'fechaTicket': _('Fecha Emitida'),
            'estado': _('Estado')
        }

    def save(self, commit=True):
        ticket = super().save(commit=False)

        # Generar número de ticket
        ultimo_ticket = Ticket.objects.latest('id')
        numero_ticket = ultimo_ticket.id + 1
        codigo_ticket = f"AM{str(numero_ticket).zfill(3)}"

        ticket.nroTicket = codigo_ticket

        if commit:
            ticket.save()

        return ticket


class MedicosForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = ['name', 'lastName','email','dni', 'celp', 'tipo','horario']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'celp': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'horario': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {'name': 'Nombre',
                  'lastName': 'Apellido',
                  'email': 'Correo',
                  'dni': 'Numero de DNI',
                  'celp': 'Telefono',
                  'tipo': _('Area'),
                  'horario': _('Horario')
                  }
        
class HistoriasForm(forms.ModelForm):
    class Meta:
        model = Historias
        fields = ['paciente', 'medico','cita','observacion']
        labels = {'paciente': 'Paciente',
                  'medico': 'Medico',
                  'cita': 'cita',
                  'observacion': 'Observacion'
                  }
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'medico': forms.Select(attrs={'class': 'form-control'}),
            'cita': forms.Select(attrs={'class': 'form-control'}),
            'observacion': forms.Textarea(attrs={'class': 'form-control'}),
        }
class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre']
        labels = {'nombre': 'Nombre'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class SalaForm(forms.ModelForm):
    ESTADO_CHOICES = (
        ('Pendiente', 'Ocupado'),
        ('Atendido', 'Disponible'),
    )

    estado = forms.ChoiceField(choices=ESTADO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = SalaOperaciones
        fields = ['nombre','estado']
        labels = {'nombre': 'Nombre','estado':'Estado'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class TecnicosForm(forms.ModelForm):
    class Meta:
        model = Tecnicos
        fields = ['name', 'lastName','email','dni', 'celp', 'tipo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'celp': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {'name': 'Nombre',
                  'lastName': 'Apellido',
                  'email': 'Correo',
                  'dni': 'Numero de DNI',
                  'celp': 'Telefono',
                  'tipo': _('Area')
                  }
class EnfermerosForm(forms.ModelForm):
    class Meta:
        model = Enfermeros
        fields = ['name', 'lastName','email','dni', 'celp', 'tipo']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.NumberInput(attrs={'class': 'form-control'}),
            'celp': forms.NumberInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {'name': 'Nombre',
                  'lastName': 'Apellido',
                  'email': 'Correo',
                  'dni': 'Numero de DNI',
                  'celp': 'Telefono',
                  'tipo': _('Area')
                  }
        
class EquipoForm(forms.ModelForm):
    class Meta:
        model = EquipoMedico
        fields = ['nombre', 'medicos', 'tecnicos', 'enfermeros', 'pacientes', 'sala', 'fecha', 'hora', 'observacion']
        labels = {'nombre': 'Nombre',
                  'medicos': 'Médicos',
                  'tecnicos': 'Técnicos',
                  'enfermeros': 'Enfermeros',
                  'pacientes': 'Pacientes',
                  'sala': 'Sala de Operaciones',
                  'fecha': 'Fecha',
                  'hora': 'Hora',
                  'observacion': 'Observación'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'medicos': forms.Select(attrs={'class': 'form-control'}),
            'tecnicos': forms.Select(attrs={'class': 'form-control'}),
            'enfermeros': forms.Select(attrs={'class': 'form-control'}),
            'pacientes': forms.Select(attrs={'class': 'form-control'}),
            'sala': forms.Select(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'observacion': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Recetas
        fields = ['paciente', 'medico', 'cita', 'medicamento', 'dosis', 'observacion']
        labels = {'paciente': 'Paciente',
                  'medico': 'Médico',
                  'cita': 'Cita',
                  'medicamento': 'Medicamento',
                  'dosis': 'Dosis',
                  'observacion': 'Observación'}
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'medico': forms.Select(attrs={'class': 'form-control'}),
            'cita': forms.Select(attrs={'class': 'form-control'}),
            'medicamento': forms.TextInput(attrs={'class': 'form-control'}),
            'dosis': forms.TextInput(attrs={'class': 'form-control'}),
            'observacion': forms.TextInput(attrs={'class': 'form-control'}),
        }
        

class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = ['nombre']
        labels = {'nombre': 'Nombre'}
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class HorarioMedicoForm(forms.ModelForm):
    class Meta:
        model = HorarioMedico
        fields = [ 'dia', 'horaInicio', 'horaFin']
        labels = {'dia': 'Día',
                  'horaInicio': 'Hora de inicio',
                  'horaFin': 'Hora de fin'}
        widgets = {
            'dia': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'horaInicio': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'horaFin': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
        }