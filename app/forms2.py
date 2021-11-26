from django.forms import ModelForm
from app.models import Empresas, Produtos

# Create the form class.
class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'nascimento', 'telefone', 'email', 'nivel', 'semana', 'obervacao', 'pagamento', 'horario']

class EmpresasForm(ModelForm):
    class Meta:
        model = Empresas
        fields = ['cnpj', 'razaoSocial', 'email', 'cidade', 'estado']