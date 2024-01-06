from models import Empresa, Tipo, ItemNutricional, db


class TkinterController:
    @staticmethod
    @classmethod
    def criar_empresa(cls, cnpj, razao_social, fantasia, numero_sif, registro_adapi):
        with db.atomic():
            Empresa.create(
                cnpj=cnpj,
                razao_social=razao_social,
                fantasia=fantasia,
                numero_sif=numero_sif,
                registro_adapi=registro_adapi
            )

    @classmethod
    def atualizar_empresa(cls, empresa_id, cnpj, razao_social, fantasia, numero_sif, registro_adapi):
        with db.atomic():
            empresa = Empresa.get_by_id(empresa_id)
            empresa.cnpj = cnpj
            empresa.razao_social = razao_social
            empresa.fantasia = fantasia
            empresa.numero_sif = numero_sif
            empresa.registro_adapi = registro_adapi
            empresa.save()

    @staticmethod
    def criar_tipo(cls, tipo):
        with db.atomic():
            Tipo.create(
                tipo=tipo
            )

    @staticmethod
    def criar_item_nutricional(tipo, corte, valores_entradas):
        return ItemNutricional.create(
            tipo=tipo,
            corte=corte,
            valor_energetico_100g=valores_entradas.get("valor_energetico_100g", 0.0),
            valor_energetico_vd=valores_entradas.get("valor_energetico_vd", 0.0),
            carboidratos_totais_100g=valores_entradas.get("carboidratos_totais_100g", 0.0),
            carboidratos_totais_vd=valores_entradas.get("carboidratos_totais_vd", 0.0),
            acucares_totais_100g=valores_entradas.get("acucares_totais_100g", 0.0),
            acucares_totais_vd=valores_entradas.get("acucares_totais_vd", 0.0),
            acucares_adicionados_100g=valores_entradas.get("acucares_adicionados_100g", 0.0),
            acucares_adicionados_vd=valores_entradas.get("acucares_adicionados_vd", 0.0),
            proteinas_100g=valores_entradas.get("proteinas_100g", 0.0),
            proteinas_vd=valores_entradas.get("proteinas_vd", 0.0),
            gorduras_totais_100g=valores_entradas.get("gorduras_totais_100g", 0.0),
            gorduras_totais_vd=valores_entradas.get("gorduras_totais_vd", 0.0),
            gorduras_saturadas_100g=valores_entradas.get("gorduras_saturadas_100g", 0.0),
            gorduras_saturadas_vd=valores_entradas.get("gorduras_saturadas_vd", 0.0),
            gorduras_trans_100g=valores_entradas.get("gorduras_trans_100g", 0.0),
            gorduras_trans_vd=valores_entradas.get("gorduras_trans_vd", 0.0),
            fibra_alimentar_100g=valores_entradas.get("fibra_alimentar_100g", 0.0),
            fibra_alimentar_vd=valores_entradas.get("fibra_alimentar_vd", 0.0),
            sodio_100g=valores_entradas.get("sodio_100g", 0.0),
            sodio_vd=valores_entradas.get("sodio_vd", 0.0),
            porcao_embalagem=valores_entradas.get("porcao_embalagem", ""),
            porcao=valores_entradas.get("porcao", ""),
            informacoes_adicionais=valores_entradas.get("informacoes_adicionais", "")
        )

    @staticmethod
    def obter_empresas():
        return Empresa.select()

    @staticmethod
    def obter_tipos():
        return Tipo.select()

    @staticmethod
    def obter_itens_nutricionais():
        return ItemNutricional.select()

    @staticmethod
    def obter_item_nutricional_por_id(item_id):
        return ItemNutricional.get_or_none(id=item_id)

    @staticmethod
    def atualizar_item_nutricional(item_id, valores_entradas):
        return ItemNutricional.update(**valores_entradas).where(ItemNutricional.id == item_id).execute()

    @staticmethod
    def excluir_item_nutricional(item_id):
        return ItemNutricional.delete().where(ItemNutricional.id == item_id).execute()
