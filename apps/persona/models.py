from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)



class Persona(models.Model):
    nombre = models.CharField(max_length=150, blank=True, default='')
    apellido = models.CharField(max_length=100, blank=True, default='')
    telefono = models.CharField(max_length=100, blank=True, default='') # models.TextField()
    email = models.BooleanField(default=False)
    fecha_nacimiento = models.DateField()
    #evento  = models.ForeignKey(Evento, related_name='personas', on_delete=models.CASCADE) 

    class Meta:
        ordering = ('nombre',)
    
    def __str__(self):
            return "%s - %s" % (self.nombre, self.apellido)

    def __unicode__(self):
        return '%s: %s' % (self.nombre, self.apellido)

    def get_absolute_url(self):
        return "/persona/%i/" % self.id

class Evento(models.Model):
    motivo  =  models.CharField(max_length=100, blank=True, default='') # models.TextField()
    lugar   =  models.CharField(max_length=100, blank=True, default='')
    fecha   =  models.DateField()
    personas = models.ManyToManyField(Persona)
    class Meta:
        ordering = ('fecha',)

    def __str__(self):
            return "%s - %s" % (self.motivo, self.lugar)

    def __unicode__(self):
        return '%s: %s' % (self.lugar, self.motivo)




