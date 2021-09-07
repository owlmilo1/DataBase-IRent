import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password =''
)

cursor = banco.cursor()

cursor.execute("CREATE DATABASE python_db")

print("Banco Criado")

banco.close()

print("Conexão Desligada")

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password ='',
    database = 'python_db'
)

cursor = banco.cursor()

cursor.execute('CREATE TABLE cliente(id_cliente int UNSIGNED NOT NULL auto_increment primary key,' 
               'nome varchar(30) not null, cpf varchar(11) not null UNIQUE, e_mail varchar(30) not null UNIQUE,' 
               'senha varchar(20) not null, nascimento date not null) ENGINE = InnoDB, DEFAULT CHARSET = utf8,' 
               'AUTO_INCREMENT = 0;')

print('Tabela Cliente Criada')

cursor.execute('CREATE TABLE metodo_pagamento(id_cartao int UNSIGNED not null auto_increment primary key,' 
               'id_cliente int UNSIGNED, n_cartao varchar(16) not null, nome_titular varchar(30) not null,' 
               'cpf_titular varchar(11) not null, validade varchar(5) not null, cvc varchar(3) not null,' 
               'constraint fk_id_cliente foreign key (id_cliente) references cliente(id_cliente)' 
               'ON DELETE CASCADE ON UPDATE CASCADE) ENGINE = InnoDB, DEFAULT CHARSET = utf8, AUTO_INCREMENT = 0;')

print('Tabela Método de Pagamento Criada')

cursor.execute('CREATE TABLE dados_contato(id_cliente_dados int UNSIGNED, telefone varchar(15),' 
               'constraint fk_id_cliente_dados FOREIGN KEY (id_cliente_dados) REFERENCES cliente(id_cliente)' 
               'ON DELETE CASCADE ON UPDATE CASCADE) DEFAULT CHARSET = utf8, ENGINE = InnoDB;')

print('Tabela Dados de Contato criada')

cursor.execute('CREATE TABLE suporte_funcao ( id_funcao int UNSIGNED not null auto_increment,' 
               'descricao varchar(180) not null, salario double not null, PRIMARY KEY (id_funcao))' 
               'ENGINE = InnoDB, DEFAULT CHARSET = utf8, AUTO_INCREMENT = 0;')

print('Tabela Suporte Função Criada')

cursor.execute('CREATE TABLE funcionario (id_funcionario int UNSIGNED not null auto_increment primary key,' 
               'nome varchar(30) not null, id_funcao int UNSIGNED, constraint fk_id_funcao foreign key (id_funcao)' 
               'references suporte_funcao(id_funcao) ON DELETE CASCADE ON UPDATE CASCADE)' 
               'ENGINE = InnoDB, DEFAULT CHARSET = utf8, AUTO_INCREMENT = 0;')

print('Tabela Funcionário Criada')

cursor.execute('CREATE TABLE estacao ( cod_est int UNSIGNED not null auto_increment primary key,' 
               'endereco text not null, nome varchar(30))' 
               'ENGINE = InnoDB, DEFAULT CHARSET = utf8, AUTO_INCREMENT = 0;')

print('Tabela Estação Criada')

cursor.execute ('CREATE TABLE tipo_modal ( tipo_modal int UNSIGNED not null auto_increment primary key,' 
                'nome_modal varchar(30) not null, valor_hora double)' 
                'ENGINE = InnoDB, DEFAULT CHARSET = utf8, AUTO_INCREMENT = 0;')

print('Tabela Tipo Modal Criada')

cursor.execute ('CREATE TABLE modal (id_modal int UNSIGNED not null auto_increment primary key,' 
                'tipo_modal int UNSIGNED, modelo VARCHAR(30) not null, marca varchar(20) not null,' 
                'constraint fk_tipo_modal foreign key (tipo_modal) references tipo_modal(tipo_modal)' 
                'ON DELETE CASCADE ON UPDATE CASCADE) ENGINE = InnoDB, DEFAULT CHARSET = utf8, AUTO_INCREMENT = 0;')

print('Tabela Modal Criada')

cursor.execute('CREATE TABLE suporte (os int UNSIGNED not null auto_increment primary key,' 
               'id_cliente_suporte int UNSIGNED, id_modal int UNSIGNED, cod_est int UNSIGNED,' 
               'descicao_suporte TEXT not null, status_os int UNSIGNED not null, data_abertura date,' 
               'hora_abertura time, data_fechamento date, hora_fechamento time,' 
               'constraint fk_id_cliente_suporte foreign key (id_cliente_suporte) references cliente(id_cliente)' 
               'ON DELETE CASCADE ON UPDATE CASCADE,' 
               'constraint fk_id_modal foreign key (id_modal) references modal(id_modal)' 
               'ON DELETE CASCADE ON UPDATE CASCADE,' 
               'constraint fk_cod_est foreign key (cod_est) references estacao(cod_est)' 
               'ON DELETE CASCADE ON UPDATE CASCADE ) ENGINE = InnoDB, DEFAULT CHARSET = utf8, AUTO_INCREMENT = 0;')

print('Tabela Suporte Criada')

cursor.execute('CREATE TABLE funcionarios_suporte ( os int UNSIGNED, id_funcionario int UNSIGNED,' 
               'constraint fk_os foreign key (os) references suporte(os) ON DELETE CASCADE ON UPDATE CASCADE,' 
               'constraint fk_id_func foreign key (id_funcionario) references funcionario(id_funcionario)' 
               'ON DELETE CASCADE ON UPDATE CASCADE ) ENGINE = InnoDB, DEFAULT CHARSET = utf8, AUTO_INCREMENT = 0;')

print('Tabela Funcionários do Suporte Criada')

cursor.execute('CREATE TABLE corrida ( cod_corrida int UNSIGNED not null auto_increment primary key, valor double,' 
               'dataT date, h_retirada time, h_devolucao time, cod_est_ret int UNSIGNED, cod_est_dev int UNSIGNED,' 
               'id_modal_corrida int UNSIGNED, constraint fk_id_modal_corrida foreign key (id_modal_corrida)' 
               'references modal (id_modal) ON DELETE CASCADE ON UPDATE CASCADE,' 
               'constraint fk_cod_est_ret foreign key (cod_est_ret) references estacao(cod_est)' 
               'ON DELETE CASCADE ON UPDATE CASCADE, constraint fk_cod_est_dev foreign key (cod_est_dev)' 
               'references estacao(cod_est) ON DELETE CASCADE ON UPDATE CASCADE)' 
               'ENGINE = InnoDB, DEFAULT CHARSET = utf8, AUTO_INCREMENT = 0;')

print('Tabela Corrida Criada')

cursor.execute('CREATE TABLE faturamento ( id_cartao int UNSIGNED, id_cliente_faturamento int UNSIGNED,' 
               'cod_corrida int UNSIGNED, dataT date, status_os int UNSIGNED,' 
               'constraint fk_id_cartao foreign key (id_cartao) references metodo_pagamento(id_cartao)' 
               'ON DELETE CASCADE ON UPDATE CASCADE,' 
               'constraint fk_id_cliente_faturamento foreign key (id_cliente_faturamento)' 
               'references cliente(id_cliente) ON DELETE CASCADE ON UPDATE CASCADE,' 
               'constraint fk_cod_corrida foreign key (cod_corrida) references corrida(cod_corrida)' 
               'ON DELETE CASCADE ON UPDATE CASCADE) ENGINE = InnoDB, DEFAULT CHARSET = utf8, AUTO_INCREMENT = 0;')

print('Tabela Faturamento Criada')