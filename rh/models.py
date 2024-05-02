from django.db import models

class Funcionario(models.Model):
    # Informações pessoais
    nome_completo = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=14) 
    cnpj = models.CharField(max_length=18, blank=True, default='--/--')  # CNPJ é opcional e tem um valor padrão
    
    # Tipo de contrato
    TIPO_CONTRATO_CHOICES = [
        ('Estágio', 'Estágio'),
        ('CLT', 'CLT'),
        ('PJ', 'PJ'),
    ]
    tipo_contrato = models.CharField(max_length=10, choices=TIPO_CONTRATO_CHOICES)
    
    # Duração do contrato
    TEMPO_CONTRATO_CHOICES = [
        ('6 Meses', '6 Meses'),
        ('1 Ano', '1 Ano'),
        ('2 Anos', '2 Anos'),
        ('Indeterminado', 'Indeterminado'),
    ]
    tempo_contrato = models.CharField(max_length=15, choices=TEMPO_CONTRATO_CHOICES)

    # Detalhes do horário de trabalho
    TURNO_CHOICES = [
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
        ('Integral', 'Integral'),
    ]
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES, null=True)  # Pode ser nulo se não aplicável
    
    HORARIO_DIARIO_CHOICES = [
        ('6 Horas', '6 Horas'),
        ('9 Horas', '9 Horas'),
    ]
    horario_diario = models.CharField(max_length=8, choices=HORARIO_DIARIO_CHOICES, null=True)  # Pode ser nulo se não aplicável

    # Remuneração e benefícios
    salario = models.DecimalField(max_digits=10, decimal_places=2)  
    vr_ativo = models.BooleanField(default=False)
    vr_valor_diario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Valor diário do VR, pode ser nulo
    vt_ativo = models.BooleanField(default=False)
    vt_valor_diario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Valor diário do VT, pode ser nulo

    # Departamento e empresa
    SETOR_CHOICES = [
        ('Atendimento POA', 'Atendimento POA'),
        ('Atendimento SM', 'Atendimento SM'),
        ('Atendimento SLE', 'Atendimento SLE'),
        ('SIAPE', 'SIAPE'),
        ('INSS', 'INSS'),
        ('TI', 'TI'),
        ('Marketing', 'Marketing'),
        ('Operacional', 'Operacional'),
        ('Outros', 'Outros'),
    ]
    setor = models.CharField(max_length=20, choices=SETOR_CHOICES)
    
    EMPRESAS_CHOICES = [
        ('BOREAL', 'BOREAL'),
        ('MONEY', 'MONEY'),
        ('PARK GUAIBA', 'PARK GUAIBA'),
    ]
    empresas = models.CharField(max_length=20, choices=EMPRESAS_CHOICES, null=True)  # Acho que aqui deve ser EMPRESAS_CHOICES

    # Status do funcionário
    STATUS_ATIVIDADE_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]
    status_atividade = models.CharField(max_length=7, choices=STATUS_ATIVIDADE_CHOICES)
    
    # Data de cadastro automaticamente adicionada
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo
