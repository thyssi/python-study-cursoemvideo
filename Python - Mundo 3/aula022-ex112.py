 # Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada
 # leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas
 # valores que sejam monetários.

 from CursoemVideo.modulos import dado, moeda

 valor = dado.leiadinheiro('Qual o valor? ')
moeda.resumo(valor, 25, 15)