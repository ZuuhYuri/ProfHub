from django.db import models

from multiselectfield import MultiSelectField

# Create your models here.
NIVEIS = (
    ('A1','A1'),
    ('A2', 'A2'),
    ('B1','B1'),
    ('B2','B2'),
    ('C1','C1'),
    ('C2','C2'),
)

HORARIOS = (
    ('07:00','07:00'),
    ('08:00','08:00'),
    ('09:00','09:00'),
    ('10:00','10:00'),
    ('11:00','11:00'),
    ('12:00','12:00'),
    ('13:00','13:00'),
    ('14:00','14:00'),
    ('15:00','15:00'),
    ('16:00','16:00'),
    ('17:00','17:00'),
    ('18:00','18:00'),
    ('19:00','19:00'),
    ('20:00','20:00'),
    ('21:00','21:00'),
)

DIAS = (
    ('01','01'),
    ('02','02'),
    ('03','03'),
    ('04','04'),
    ('05','05'),
    ('06','06'),
    ('07','07'),
    ('08','08'),
    ('09','09'),
    ('10','10'),
    ('11','11'),
    ('12','12'),
    ('13','13'),
    ('14','14'),
    ('15','15'),
    ('16','16'),
    ('17','17'),
    ('18','18'),
    ('19','19'),
    ('20','20'),
    ('21','21'),
    ('22','22'),
    ('23','23'),
    ('24','24'),
    ('25','25'),
    ('26','26'),
    ('27','27'),
    ('28','28'),
    ('29','29'),
    ('30','30'),
    ('31','31'),

)

SEMANA = (('seg', 'segunda-feira'),
              ('ter', 'terça-feira'),
              ('qua', 'quarta-feira'),
              ('qui', 'quinta-feira'),
              ('sex', 'sexta-feira'),
              ('sáb', 'sábado'),
              ('dom', 'domingo'),
              ('desistente', 'desistente'),
              )
    
class Produtos(models.Model):
    nome = models.CharField(max_length=30)
    nascimento = models.CharField(max_length=10)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    nivel = models.CharField(max_length=6, choices=NIVEIS)
    semana = MultiSelectField(choices=SEMANA)
    pagamento = models.CharField(max_length=10, choices=DIAS)
    obervacao = models.TextField(max_length=1000)
    horario = models.CharField(max_length=10, choices=HORARIOS)
    


class Empresas(models.Model):
    cnpj = models.CharField(max_length=14, default="14 dígitos")
    razaoSocial = models.CharField(max_length=10, default=" ")
    email = models.CharField(max_length=50, default=" ")
    cidade = models.CharField(max_length=20, default=" ")
    estado = models.CharField(max_length=2, default="Ex: SP" )