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

    @classmethod
    def criar_tipo(cls, tipo):
        try:
            with db.atomic():
                # Certifique-se de substituir 'Tipo' pelo nome da sua classe modelo para tipos
                Tipo.create(tipo=tipo)
            print(f'Tipo "{tipo}" criado com sucesso!')
        except Exception as e:
            print(f'Erro ao criar tipo: {str(e)}')


    def salvar_produto(self,dados_produto):
        # Lógica para salvar o produto, por exemplo, em um banco de dados
        # Certifique-se de implementar essa lógica adequadamente
        print("Salvando produto:", dados_produto)

        try:
            with db.atomic():
                # Criar instância do modelo ItemNutricional
                item_nutricional = ItemNutricional.create(**dados_produto)
                print(f'Produto {item_nutricional.id} salvo com sucesso!')
        except Exception as e:
            print(f'Erro ao salvar produto: {str(e)}')
            

    @staticmethod
    def obter_empresas():
        return Empresa.select()

    @staticmethod
    def obter_tipos():
        tipos = Tipo.select().dicts()
        return [tipo['tipo'] for tipo in tipos]

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
