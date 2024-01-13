from peewee import *
from datetime import datetime

db = SqliteDatabase('tabela_nutricional.db')

class Base(Model):
    created_at = DateTimeField(default=datetime.now)
    updated_at = DateTimeField(default=datetime.now)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.now()
        return super().save(*args, **kwargs)

    class Meta:
        database = db

class Empresa(Base):
    cnpj = CharField(max_length=20, unique=True)
    razao_social = CharField(max_length=100, unique=True)
    fantasia = CharField(max_length=100, unique=True)
    numero_sif = CharField(max_length=100, unique=True)
    registro_adapi = CharField(max_length=100, unique=True)

class Tipo(Base):
    tipo = CharField(max_length=100, unique=True)

class ItemNutricional(Base):
    tipo = ForeignKeyField(Tipo, backref='tipos', on_delete='CASCADE')
    corte = CharField(max_length=100, unique=True)
    sexo = CharField()
    codigo_barras = CharField()
    porcao_embalagem = CharField()
    porcao = CharField() 
    campo_adicional = CharField()
    valor_energetico_100g = FloatField()
    valor_energetico_vd = FloatField()

    carboidratos_totais_100g = FloatField()
    carboidratos_totais_vd = FloatField()

    acucares_totais_100g = FloatField()
    acucares_totais_vd = FloatField()

    acucares_adicionados_100g = FloatField()
    acucares_adicionados_vd = FloatField()

    proteinas_100g = FloatField()
    proteinas_vd = FloatField()

    gorduras_totais_100g = FloatField()
    gorduras_totais_vd = FloatField()

    gorduras_saturadas_100g = FloatField()
    gorduras_saturadas_vd = FloatField()

    gorduras_trans_100g = FloatField()
    gorduras_trans_vd = FloatField()

    fibra_alimentar_100g = FloatField()
    fibra_alimentar_vd = FloatField()

    sodio_100g = FloatField()
    sodio_vd = FloatField()

    porcao_embalagem = CharField(default="")
    porcao = CharField(default="")

    informacoes_adicionais = TextField(default="")

# Conectar e criar tabelas
db.connect()
db.create_tables([ItemNutricional, Empresa, Tipo])
