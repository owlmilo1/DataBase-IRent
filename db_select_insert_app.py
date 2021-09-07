#MENU PRINCIPAL
def MenuPrincipal():
    print('''
[1] Adicionar Dados
[2] Consultar Dados
[0] Sair do programa''')
    opcao = int(input("Selecione a opção que você deseja realizar no Banco de Dados: "))

    if opcao == 1:
        adicionar()

    if opcao == 2:
        consultar()

    if opcao == 0:
        cursor.close()
        banco.close()
        print("")
        print("Programa finalizado")

# CONSULTAR DADOS
# Fução Consultar
def consultar():
    print('''\n[1] Cliente
[2] Funcionário
[3] Modal
[4] Estaçã
[0] Voltar ao Menu\n''')
    opcao = int(input('Insira o código do que você deseja consultar: '))

    if opcao == 1:
        consultacliente()

    if opcao == 2:
        consultafuncionario()

    if opcao == 3:
        consultamodal()

    if opcao == 4:
        consultaestacao()

    if opcao == 0:
        MenuPrincipal()

# Função Cliente
def consultacorridas(a):
    consultacorrida_sql = '''SELECT a.cod_corrida, a.valor, a.dataT, a.h_retirada, a.h_devolucao, a.cod_est_ret,
     a.cod_est_dev, a.id_modal_corrida, b.id_cartao FROM corrida a, faturamento b WHERE
     a.cod_corrida = b.cod_corrida AND b.id_cliente_faturamento = %d''' % a
    cursor.execute(consultacorrida_sql)
    linhascorrida = cursor.fetchall()
    for linha in linhascorrida:
        print('Código da Corrida: ', linha[0])
        print('Valor: R$', linha[1])
        print('Cartão: ', linha[2])
        print('Data: ', linha[3])
        print('Horário da retirada: ', linha[4])
        print('Horário da devolução: ', linha[5])
        print('Código da Estação de retirada: ', linha[6])
        print('Código da Estação de devolução: ', linha[7])
        print('Modal: ', linha[8], '\n')

    print('Deseja retornar?')
    c = int(input('Digite [0] para retornar: '))
    if c == 0:
        consultaclienteopcoes(a)

def consultadados(a):
    consultadados_sql = 'SELECT id_cliente, nome, cpf, e_mail, nascimento FROM cliente WHERE id_cliente = %d' % a
    cursor.execute(consultadados_sql)
    linhasdados = cursor.fetchall()
    for linha in linhasdados:
        print('\nid: ', linha[0])
        print('Nome: ', linha[1])
        print('CPF: ', linha[2])
        print('E-mail: ', linha[3])
        print('Nascimento: ', linha[4], '\n')

    consultacontato_sql = 'SELECT telefone FROM dados_contato WHERE id_cliente_dados = %d' % a
    cursor.execute(consultacontato_sql)
    linhascontato = cursor.fetchall()
    for linha in linhascontato:
        print('Contato Salvo: ', linha[0], '\n')

    consultacartao_sql = 'SELECT n_cartao, validade FROM metodo_pagamento WHERE id_cliente = %d' % a
    cursor.execute(consultacartao_sql)
    linhascartao = cursor.fetchall()
    for linha in linhascartao:
        print('N° do Cartão: ', linha[0])
        print('Validade: ', linha[1], '\n')

    print('Deseja retornar?')
    c = int(input('Digite [0] para retornar: '))
    if c == 0:
        consultaclienteopcoes(a)

def consultasuporte(a):
    consultasuporte_sql = '''SELECT os, id_modal, cod_est, descicao_suporte, data_abertura, hora_abertura, 
    data_fechamento, hora_fechamento FROM suporte WHERE id_cliente_suporte = %d''' % a
    cursor.execute(consultasuporte_sql)
    linhassuporte = cursor.fetchall()
    for linha in linhassuporte:
        print('id da OS:', linha[0])
        print('Modal Notificado: ', linha[1])
        print('Estação Notificada: ', linha[2])
        print('Descrição da Solicitação: ', linha[3])
        print('Data de abertura da solicitação: ', linha[4])
        print('Hora de abertura da solicitação: ', linha[5])
        print('Data de fechamento da solicitação: ', linha[6])
        print('Hora de fechamento da solicitação: ', linha[7], '\n')

    print('Deseja retornar?')
    c = int(input('Digite [0] para retornar: '))
    if c == 0:
        consultaclienteopcoes(a)

# Função Cliente Principal
def consultacliente():
    print('\nConsulte um Cliente')
    a = int(input('Insira o ID do usuário: '))
    consultaclienteopcoes(a)

def consultaclienteopcoes(a):
    print("\nO que deseja consultar?")
    print('''[1] Dados Pessoais
[2] Corridas
[3] Solicitações de Suporte
[0] Voltar ao Menu''')
    b = int(input('\nDigite o código: '))
    if b == 1:
        consultadados(a)

    if b == 2:
        consultacorridas(a)

    if b == 3:
        consultasuporte(a)

    if b == 0:
        consultar()

# Função Funcionário
def consultadadosf(a):
    consultadadosf_sql = '''SELECT a.id_funcionario, a.nome, b.descricao FROM funcionario a, suporte_funcao b 
    WHERE a.id_funcao = b.id_funcao AND a.id_funcionario = %d''' % a
    cursor.execute(consultadadosf_sql)
    linhasdadosf = cursor.fetchall()
    for linha in linhasdadosf:
        print('id do Funcionário: ', linha[0])
        print('Nome: ', linha[1])
        print('Função: ', linha[2], '\n')

    print('Deseja retornar?')
    c = int(input('Digite [0] para retornar: '))
    if c == 0:
        consultafuncionarioopcoes(a)

def consultasuportef(a):
    consultasuportef_sql = '''SELECT a.os, a.id_modal, a.cod_est, a.descicao_suporte, a.data_abertura, 
    a.hora_abertura, a.data_fechamento, a.hora_fechamento FROM suporte a, funcionario b, funcionarios_suporte c 
    WHERE a.os = c.os AND c.id_funcionario = b.id_funcionario AND c.id_funcionario = %d''' % a
    cursor.execute(consultasuportef_sql)
    linhassuportef = cursor.fetchall()
    for linha in linhassuportef:
        print('id da OS: ', linha[0])
        print('Modal Notificado: ', linha[1])
        print('Estação Notificada: ', linha[2])
        print('Descrição da Solicitação: ', linha[3])
        print('Data de abertura da solicitação: ', linha[4])
        print('Hora de abertura da solicitação: ', linha[5])
        print('Data de fechamento da solicitação: ', linha[6])
        print('Hora de fechamento da solicitação: ', linha[7], '\n')

    print('Deseja retornar?')
    c = int(input('Digite [0] para retornar: '))
    if c == 0:
        consultafuncionarioopcoes(a)

# Função Funcionário Principal
def consultafuncionario():
    print('\nConsulte um Funcionário')
    a = int(input('Insira o ID do funcionário: '))
    consultafuncionarioopcoes(a)

def consultafuncionarioopcoes(a):
    print('\nO que deseja consultar?')
    print('''[1] Dados
[2] Solicitações de Suporte Atendidas
[0] Voltar ao Menu''')
    b = int(input('\nDigite o código: '))
    if b == 1:
        consultadadosf(a)

    if b == 2:
        consultasuportef(a)

    if b == 0:
        consultar()

# Função Modal
def consultadadosmodal(a):
    consultadadomodal_sql = '''SELECT a.id_modal, a.modelo, a.marca, b.nome_modal FROM modal a, tipo_modal b 
    WHERE a.tipo_modal = b.tipo_modal AND a.id_modal = %d''' % a
    cursor.execute(consultadadomodal_sql)
    linhasdadosmodal = cursor.fetchall()
    for linha in linhasdadosmodal:
        print('id do Modal: ', linha[0])
        print('Modelo: ', linha[1])
        print('Marca: ', linha[2])
        print('Tipo: ', linha[3], '\n')

    print('Deseja retornar?')
    c = int(input('Digite [0] para retornar: '))
    if c == 0:
        consultamodalopcoes(a)

def consultacorridasmodal(a):
    consultacorridasmodal_sql = '''SELECT a.cod_corrida, a.dataT, a.h_retirada, 
    a.h_devolucao, a.cod_est_ret, a.cod_est_dev FROM corrida a, modal b 
    WHERE a.id_modal_corrida = b.id_modal AND a.id_modal_corrida = %d''' % a
    cursor.execute(consultacorridasmodal_sql)
    linhascorridasmodal = cursor.fetchall()
    for linha in linhascorridasmodal:
        print('Código da Corrida: ', linha[0])
        print('Data: ', linha[1])
        print('Horário da retirada: ', linha[2])
        print('Horário da devolução: ', linha[3])
        print('Código da Estação de retirada: ', linha[4])
        print('Código da Estação de devolução: ', linha[5], '\n')

    print('Deseja retornar?')
    c = int(input('Digite [0] para retornar: '))
    if c == 0:
        consultamodalopcoes(a)

def consultasuportemodal(a):
    consultasuportemodal_sql = '''SELECT a.os, a.descicao_suporte, a.data_abertura, a.hora_abertura, 
    a.data_fechamento, a.hora_fechamento FROM suporte a, modal b WHERE a.id_modal = b.id_modal 
    AND a.id_modal = %d''' % a
    cursor.execute(consultasuportemodal_sql)
    linhasuportemodal = cursor.fetchall()
    for linha in linhasuportemodal:
        print('id da OS: ', linha[0])
        print('Descrição da Solicitação: ', linha[1])
        print('Data de abertura da solicitação: ', linha[2])
        print('Hora de abertura da solicitação: ', linha[3])
        print('Data de fechamento da solicitação: ', linha[4])
        print('Hora de fechamento da solicitação: ', linha[5], '\n')

    print('Deseja retornar?')
    c = int(input('Digite [0] para retornar: '))
    if c == 0:
        consultamodalopcoes(a)

# Função Modal Principal
def consultamodal():
    print('\nConsulte um Modal')
    a = int(input('Insira o ID do modal: '))
    consultamodalopcoes(a)

def consultamodalopcoes(a):
    print('\nO que deseja consultar?')
    print('''[1] Dados do Modal
[2] Corridas
[3] Solicitações de Suporte
[0] Voltar ao Menu''')
    b = int(input('\nDigite o código: '))
    if b == 1:
        consultadadosmodal(a)

    if b == 2:
        consultacorridasmodal(a)

    if b == 3:
        consultasuportemodal(a)

    if b == 0:
        consultar()

# Função Estação
def consultadadosestacao(a):
    consultadadosestacao_sql = '''SELECT cod_est, nome, endereco FROM estacao WHERE cod_est = %d''' % a
    cursor.execute(consultadadosestacao_sql)
    linhasdadosestacao = cursor.fetchall()
    for linha in linhasdadosestacao:
        print('id da Estação: ', linha[0])
        print('Nome: ', linha[1])
        print('Endereço: ', linha[2], '\n')

    print('Deseja retornar?')
    c = int(input('Digite [0] para retornar: '))
    if c == 0:
        consultaestacaoopcoes(a)

def consultacorridasestacaoret(a):
    consultacorridasestacaoret_sql = '''SELECT a.cod_corrida, a.dataT, a.h_retirada, a.id_modal_corrida 
    FROM corrida a, estacao b WHERE a.cod_est_ret = b.cod_est AND a.cod_est_ret = %d''' % a
    cursor.execute(consultacorridasestacaoret_sql)
    linhascorridasestacaoret = cursor.fetchall()
    for linha in linhascorridasestacaoret:
        print('Código da Corrida: ', linha[0])
        print('Data: ', linha[1])
        print('Horário da retirada: ', linha[2])
        print('Código do Modal: ', linha[3], '\n')

    print('Deseja retornar?')
    c = int(input('Digite [0] para retornar: '))
    if c == 0:
        consultaestacaoopcoes(a)

def consultacorridasestacaodev(a):
    consultacorridasestacaodev_sql = '''SELECT a.cod_corrida, a.dataT, a.h_devolucao, a.id_modal_corrida 
	FROM corrida a, estacao b WHERE a.cod_est_dev = b.cod_est AND a.cod_est_dev = %d''' % a
    cursor.execute(consultacorridasestacaodev_sql)
    linhascorridasestacaodev = cursor.fetchall()
    for linha in linhascorridasestacaodev:
        print('Código da Corrida: ', linha[0])
        print('Data: ', linha[1])
        print('Horário da devolução: ', linha[2])
        print('Código do Modal: ', linha[3], '\n')

    print('Deseja retornar?')
    c = int(input('Digite [0] para retornar: '))
    if c == 0:
        consultaestacaoopcoes(a)

def consultasuporteestacao(a):
    consultasuporteestacao_sql = '''SELECT a.os, a.descicao_suporte, a.data_abertura, a.hora_abertura, 
    a.data_fechamento, a.hora_fechamento FROM suporte a, estacao b WHERE a.cod_est = b.cod_est 
    AND a.cod_est = %d''' % a
    cursor.execute(consultasuporteestacao_sql)
    linhassuporteestacao = cursor.fetchall()
    for linha in linhassuporteestacao:
        print('id da OS: ', linha[0])
        print('Descrição da Solicitação: ', linha[1])
        print('Data de abertura da solicitação: ', linha[2])
        print('Hora de abertura da solicitação: ', linha[3])
        print('Data de fechamento da solicitação: ', linha[4])
        print('Hora de fechamento da solicitação: ', linha[5], '\n')

    print('Deseja retornar?')
    c = int(input('Digite [0] para retornar: '))
    if c == 0:
        consultaestacaoopcoes(a)

# Função Estação Principal
def consultaestacao():
    print('\nConsulte uma Estação')
    a = int(input('Insira o ID da estação: '))
    consultaestacaoopcoes(a)

def consultaestacaoopcoes(a):
    print('\nO que deseja consultar?')
    print('''[1] Dados da Estação
[2] Corridas Retirada
[3] Corridas Devolução
[4] Solicitações de Suporte
[0] Voltar ao Menu''')
    b = int(input('\nDigite o código: '))
    if b == 1:
        consultadadosestacao(a)

    if b == 2:
        consultacorridasestacaoret(a)

    if b == 3:
        consultacorridasestacaodev(a)

    if b == 4:
        consultasuporteestacao(a)

    if b == 0:
        consultar()


# ADICIONAR DADOS
# Função Adicionar
def adicionar():
    print('''\n[1] Cliente
[2] Funcionário
[3] Estação
[4] Modal
[5] Sistema\n''')
    opcao = int(input('Insira o opção do que você deseja adicionar: '))

    if opcao == 1:
        adicionarcliente()

    if opcao == 2:
        adicionarfuncionario()

    if opcao == 3:
        adicionarestacao()

    if opcao == 4:
        adicionarmodal()

    if opcao == 5:
        adicionarsistema()

# Função Adicionar Cliente
def adicionarclientenovo():
    print("")
    v1 = str(input("Insira o nome: "))
    v2 = str(input("Insira o CPF: "))
    v3 = str(input("Insira o E-mail: "))
    v31 = str(input("Insira a Senha: "))
    v4 = str(input("Insira a data de nascimento (aaaa-mm-dd): "))
    print("\nMétodos de pagamento:")
    v5 = str(input("Insira o n° de um cartão: "))
    v6 = str(input("Insira o nome do titular: "))
    v7 = str(input("Insira o CPF do titular: "))
    v8 = str(input("Insira a Validade: "))
    v9 = str(input("Insira o CVC: "))
    print("\nContato:")
    v10 = str(input("Insira o n° de um telefone: "))

    print('''Deseja Salvar?
[1] Salvar
[2] Cancelar''')
    a = int(input("Selecione a opção: "))

    if a == 1:
        comando_SQL1 = "INSERT INTO cliente (nome, cpf, e_mail, nascimento, senha) VALUES(%s, %s, %s, %s, %s)"
        dados1 = (v1, v2, v3, v4, v31)
        cursor.execute(comando_SQL1, dados1)
        comando_SQL2 = '''INSERT INTO metodo_pagamento (id_cliente, n_cartao, nome_titular, cpf_titular, validade, cvc) 
        VALUES(LAST_INSERT_ID(), %s, %s, %s, %s, %s)'''
        dados2 = (v5, v6, v7, v8, v9)
        cursor.execute(comando_SQL2, dados2)
        comando_SQL3 = "INSERT INTO dados_contato (id_cliente_dados, telefone) VALUES (LAST_INSERT_ID(), '%s')" % v10
        cursor.execute(comando_SQL3)
        banco.commit()
        print("")
        print("Dados adicionados!")
        print("Voltando para a tela de adicionar")
        adicionarcliente()

    if a == 2:
        print("")
        print("Voltando para a tela de adicionar")
        adicionarcliente()

def adicionarclientecartao():
    print("")
    v1 = int(input("Insira o id do cliente: "))
    v2 = str(input("Insira o n° de um cartão: "))
    v3 = str(input("Insira o nome do titular: "))
    v4 = str(input("Insira o CPF do titular: "))
    v5 = str(input("Insira a Validade: "))
    v6 = str(input("Insira o CVC: "))

    print('''Deseja Salvar?
[1] Salvar
[2] Cancelar''')
    a = int(input("Selecione a opção: "))

    if a == 1:
        comando_SQL = '''INSERT INTO metodo_pagamento (id_cliente, n_cartao, nome_titular, cpf_titular, validade, cvc) 
        VALUES(%s, %s, %s, %s, %s, %s)'''
        dados = (v1, v2, v3, v4, v5, v6)
        cursor.execute(comando_SQL, dados)
        banco.commit()
        print("")
        print("Dados adicionados!")
        print("Voltando para a tela de adicionar")
        adicionarcliente()

    if a == 2:
        print("")
        print("Voltando para a tela de adicionar")
        adicionarcliente()

def adicionarclientecontato():
    print("")
    v1 = str(input("Insira o id do cliente: "))
    v2 = str(input("Insira o n° de um telefone: "))

    print('''Deseja Salvar?
[1] Salvar
[2] Cancelar''')
    a = int(input("Selecione a opção: "))

    if a == 1:
        comando_SQL = "INSERT INTO dados_contato (id_cliente_dados, telefone) VALUES (%s, %s)"
        dados = (v1, v2)
        cursor.execute(comando_SQL, dados)
        banco.commit()
        print("")
        print("Dados adicionados!")
        print("Voltando para a tela de adicionar")
        adicionarcliente()

    if a == 2:
        print("")
        print("Voltando para a tela de adicionar")
        adicionarcliente()

# Função Cliente Principal
def adicionarcliente():
    print('''[1] Adicionar Cliente Novo
[2] Adicionar Cartão
[3] Adicionar Contato
[0] Voltar ao Menu''')
    a = int(input("Insira o código: "))

    if a == 1:
        adicionarclientenovo()

    if a == 2:
        adicionarclientecartao()

    if a == 3:
        adicionarclientecontato()

    if a == 0:
        adicionar()

# Função Adicionar Funcionário
def adicionarfuncionariofuncao():
    print("")
    v1 = str(input("Insira o a Àrea: "))
    v2 = str(input("Insira o Salario: "))

    print('''Deseja Salvar?
[1] Salvar
[2] Cancelar''')
    a = int(input("Selecione a opção: "))

    if a == 1:
        comando_SQL = "INSERT INTO suporte_funcao (descricao, salario) VALUES (%s, %s)"
        dados = (v1, v2)
        cursor.execute(comando_SQL, dados)
        banco.commit()
        print("")
        print("Dados adicionados!")
        print("Voltando para a tela de adicionar")
        adicionarfuncionario()

    if a == 2:
        print("")
        print("Voltando para a tela de adicionar")
        adicionarfuncionario()

def adicionarfuncionarionovo():
    print("")
    v1 = str(input("Insira o nome: "))
    v2 = str(input("Insira o id da Função: "))

    print('''Deseja Salvar?
[1] Salvar
[2] Cancelar''')
    a = int(input("Selecione a opção: "))

    if a == 1:
        comando_SQL = "INSERT INTO funcionario (nome, id_funcao) VALUES (%s, %s)"
        dados = (v1, v2)
        cursor.execute(comando_SQL, dados)
        banco.commit()
        print("")
        print("Dados adicionados!")
        print("Voltando para a tela de adicionar")
        adicionarfuncionario()

    if a == 2:
        print("")
        print("Voltando para a tela de adicionar")
        adicionarfuncionario()

# Função Funcionário Principal
def adicionarfuncionario():
    print('''[1] Adicionar Nova Função
[2] Adicionar Funcionário Novo
[0] Voltar ao Menu''')
    a = int(input("Insira o código: "))

    if a == 1:
        adicionarfuncionariofuncao()

    if a == 2:
        adicionarfuncionarionovo()

    if a == 0:
        adicionar()

# Função Estação Principal
def adicionarestacao():
    print("")
    v1 = str(input("Insira o nome da estação: "))
    v2 = str(input("Insira o endereço da estação: "))

    print('''Deseja Salvar?
[1] Salvar
[2] Cancelar''')
    a = int(input("Selecione a opção: "))

    if a == 1:
        comando_SQL = "INSERT INTO estacao (nome, endereco) VALUES (%s, %s)"
        dados = (v1, v2)
        cursor.execute(comando_SQL, dados)
        banco.commit()
        print("")
        print("Dados adicionados!")
        print("Voltando para a tela de adicionar")
        adicionar()

    if a == 2:
        print("")
        print("Voltando para a tela de adicionar")
        adicionar()

# Função Modal
def adicionarmodaltipo():
    print("")
    v1 = str(input("Insira o Tipo de modal: "))
    v2 = str(input("Insira o valor da hora: "))

    print('''Deseja Salvar?
[1] Salvar
[2] Cancelar''')
    a = int(input("Selecione a opção: "))

    if a == 1:
        comando_SQL = "INSERT INTO tipo_modal (nome_modal, valor_hora) VALUES (%s, %s)"
        dados = (v1, v2)
        cursor.execute(comando_SQL, dados)
        banco.commit()
        print("")
        print("Dados adicionados!")
        print("Voltando para a tela de adicionar")
        adicionarmodal()

    if a == 2:
        print("")
        print("Voltando para a tela de adicionar")
        adicionarmodal()

def adicionarmodalnovo():
    print("")
    v1 = str(input("Insira o Tipo: "))
    v2 = str(input("Insira o Modelo: "))
    v3 = str(input("Insira a Marca: "))

    print('''Deseja Salvar?
[1] Salvar
[2] Cancelar''')
    a = int(input("Selecione a opção: "))

    if a == 1:
        comando_SQL = "INSERT INTO modal (tipo_modal, modelo, marca) VALUES (%s, %s, %s)"
        dados = (v1, v2, v3)
        cursor.execute(comando_SQL, dados)
        banco.commit()
        print("")
        print("Dados adicionados!")
        print("Voltando para a tela de adicionar")
        adicionarmodal()

    if a == 2:
        print("")
        print("Voltando para a tela de adicionar")
        adicionarmodal()

# Função Modal Principal
def adicionarmodal():
    print('''[1] Adicionar Novo Tipo de Modal
[2] Adicionar Modal
[0] Voltar ao Menu''')
    a = int(input("Insira o código: "))

    if a == 1:
        adicionarmodaltipo()

    if a == 2:
        adicionarmodalnovo()

    if a == 0:
        adicionar()

# Função Sistema
def adicionarsistemasuporte():
    print("")
    v1 = str(input("Insira o id do cliente: "))
    v2 = str(input("Insira o id do Modal (caso não tenha pressione Enter): "))
    v3 = str(input("Insira o id da Estação (caso não tenha pressione Enter): "))
    v4 = str(input("Descreva a Solicitação: "))
    v5 = str(input("Status da Solicitação: "))
    v6 = str(input("Data de abertura: "))
    v7 = str(input("Hora de abertura: "))
    v8 = str(input("Data de fechamento: "))
    v9 = str(input("Hora de fechamento: "))

    print('''Deseja Salvar?
[1] Salvar
[2] Cancelar''')
    m = int(input("Insira o código: "))

    if m == 1:
        if v2 != '' and v3 != '':
            comando_SQL = '''INSERT INTO suporte (id_cliente_suporte, id_modal, cod_est, descicao_suporte, status_os, 
            data_abertura, hora_abertura, data_fechamento, hora_fechamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
            dados = (v1, v2, v3, v4, v5, v6, v7, v8, v9)
            cursor.execute(comando_SQL, dados)
            banco.commit()

            adicionarsistemasuportefunc()

        if v2 == '' and v3 == '':
            comando_SQL = '''INSERT INTO suporte (id_cliente_suporte, descicao_suporte, status_os, 
            data_abertura, hora_abertura, data_fechamento, hora_fechamento) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            dados = (v1, v4, v5, v6, v7, v8, v9)
            cursor.execute(comando_SQL, dados)
            banco.commit()

            adicionarsistemasuportefunc()

        if v2 == '':
            comando_SQL = '''INSERT INTO suporte (id_cliente_suporte, cod_est, descicao_suporte, status_os, 
            data_abertura, hora_abertura, data_fechamento, hora_fechamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
            dados = (v1, v3, v4, v5, v6, v7, v8, v9)
            cursor.execute(comando_SQL, dados)
            banco.commit()

            adicionarsistemasuportefunc()

        if v3 == '':
            comando_SQL = '''INSERT INTO suporte (id_cliente_suporte, id_modal, descicao_suporte, status_os, 
            data_abertura, hora_abertura, data_fechamento, hora_fechamento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'''
            dados = (v1, v2, v4, v5, v6, v7, v8, v9)
            cursor.execute(comando_SQL, dados)
            banco.commit()

            adicionarsistemasuportefunc()

    if m == 2:
        print("")
        print("Voltando para a tela de adicionar")
        adicionarsistema()

def adicionarsistemasuportefunc():
    a = 1
    while a == 1:
        print("Adicione os ids dos funcionários")
        z = str(input("Insira o id do funcionário: "))

        comando_SQL1 = '''INSERT INTO funcionarios_suporte (os, id_funcionario) VALUES (LAST_INSERT_ID(), '%s')''' % z
        cursor.execute(comando_SQL1)
        banco.commit()

        print('''Deseja adicionar mais um funcionário a ocorrência?
        [1] Adicionar mais funcionários
        [0] Finalizar''')
        a = int(input("Insira o código: "))

    print("")
    print("Dados adicionados!")
    print("Voltando para a tela de adicionar")
    adicionarsistema()

def adicionarsistemacorrida():
    print("")
    v1 = str(input("Insira o Valor da corrida: "))
    v2 = str(input("Insira a data da corrida (aaaa-mm-dd): "))
    v3 = str(input("Insira o horário de retirada do modal (hh:mm:ss): "))
    v4 = str(input("Insira o horário de devolução do modal (hh:mm:ss): "))
    v5 = str(input("Insira o código da Estação de retirada: "))
    v6 = str(input("Insira o código da Estação de devolução: "))
    v7 = str(input("Insira o código do Modal: "))
    v8 = str(input("Insira o id do Cliente: "))
    v9 = str(input("Insira o id do Cartão: "))
    v10 = str(input("Insira o Status da corrida: "))

    print('''Deseja Salvar?
[1] Salvar
[2] Cancelar''')
    a = int(input("Insira o código: "))

    if a == 1:
        comando_SQL1 = '''INSERT INTO corrida (valor, dataT, h_retirada, h_devolucao, cod_est_ret, cod_est_dev, 
        id_modal_corrida) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
        dados1 = (v1, v2, v3, v4, v5, v6, v7)
        cursor.execute(comando_SQL1, dados1)
        comando_SQL2 = '''INSERT INTO faturamento (cod_corrida, id_cliente_faturamento, id_cartao, status_os, dataT) 
        VALUES (LAST_INSERT_ID(), %s, %s, %s, %s)'''
        dados2 = (v8, v9, v10, v2)
        cursor.execute(comando_SQL2, dados2)
        banco.commit()
        print("")
        print("Dados adicionados!")
        print("Voltando para a tela de adicionar")
        adicionarsistema()

    if a == 2:
        print("")
        print("Voltando para a tela de adicionar")
        adicionarsistema()

# Função Sistema Principal
def adicionarsistema():
    print('''[1] Solicitação de Suporte
[2] Corridas e Faturamento
[0] Voltar ao Menu''')
    a = int(input("Insira o código: "))

    if a == 1:
        adicionarsistemasuporte()

    if a == 2:
        adicionarsistemacorrida()

    if a == 0:
        adicionar()

#PROGRAMA PRINCIPAL
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ='',
    database = 'python_db'
)

cursor = banco.cursor()

MenuPrincipal()

################################ FIM DO CÓDIGO ################################