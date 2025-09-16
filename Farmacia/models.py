from django.db import models


class Fornecedora(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)  
    telefone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    fornecedora = models.ForeignKey(
        "Fornecedora",
        on_delete=models.CASCADE,
        related_name="medicamentos",
        null=True,  
        blank=True   
    )

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    medicamento = models.ManyToManyField(
        to=Medicamento,
        related_name='clientes',
        through='ClienteMedicamento',
        through_fields=('cliente', 'medicamento'),
    )

    def __str__(self):
        return self.nome


class ClienteMedicamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cliente.nome} - {self.medicamento.nome}"



class Post(models.Model):
    autor = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to="posts/", blank=True, null=True)
    mensagem = models.TextField()
    aprovado = models.BooleanField(default = False)
   

