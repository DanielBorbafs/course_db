create table clientes (
   id              int primary key,
   nome            varchar2(40),
   email           varchar2(80),
   data_nascimento date,
   sexo            char(1),
   uf              char(2),
   data_cadastro   date
);


create table log_acesso (
   log_id       int primary key,
   cliente_id   int,
   data_acesso  timestamp,
   canal_acesso varchar2(30),
   ip           varchar2(30),
   localizacao  varchar2(30),
   constraint fk_cliente foreign key ( cliente_id )
      references clientes ( id )
);

create table vendedores (
   id            int primary key,
   nome_vendedor varchar2(40),
   tipo_loja     varchar2(20),
   uf            char(2),
   data_entrada  date
);

alter table vendedores drop column tipo_loja

create table produtos (
   id            int primary key,
   nome_produto  varchar2(30),
   categoria     varchar2(20),
   marca         varchar2(20),
   preco         number(10,2),
   custo         number(10,2),
   estoque_atual int
);


create table campanhas (
   id          int primary key,
   canal       varchar2(20),
   inicio      date,
   fim         date,
   custo_total number(10,2)
);

create table fornecedores (
   id                int primary key,
   nome              varchar2(20),
   categoria_produto varchar2(20),
   data_contrato     date
);

/*--------------------------- */

create table reposicao_estoque (
   id             int primary key,
   produto_id     int,
   fornecedor_id  int,
   data_reposicao date,
   quantidade     int,
   preco_unitario number(10,2),
   constraint fk_produto foreign key ( produto_id )
      references produtos ( id ),
   constraint fk_fornecedor foreign key ( fornecedor_id )
      references fornecedores ( id )
);


create table cliques_campanha (
   id          int primary key,
   cliente_id  int,
   campanha_id int,
   data_clique date,
   produto_id  int,
   constraint fk_cliente_campanha foreign key ( cliente_id )
      references clientes ( id ),
   constraint fk_campanha foreign key ( campanha_id )
      references campanhas ( id ),
   constraint fk_produtos_campanha foreign key ( produto_id )
      references produtos ( id )
);


create table pedidos (
   id            int primary key,
   cliente_id    int,
   vendedor_id   int,
   data_pedido   date,
   canal_venda   varchar2(20),
   status_pedido varchar2(20),
   constraint fk_cliente_pedido foreign key ( cliente_id )
      references clientes ( id ),
   constraint fk_vendedor_id foreign key ( vendedor_id )
      references vendedores ( id )
);


create table pagamentos (
   id              int primary key,
   pedido_id       int,
   forma_pagamento varchar2(20),
   valor_pago      number(10,2),
   data_pagamento  date,
   parcelado       char(1),
   constraint fk_pedido_pagamento foreign key ( pedido_id )
      references pedidos ( id )
);


create table entregas (
   id             int primary key,
   pedido_id      int,
   data_envio     date,
   data_entrega   date,
   transportadora varchar2(20),
   frete          number(10,2),
   status_entrega varchar2(20),
   constraint fk_pedido_entrega foreign key ( pedido_id )
      references pedidos ( id )
);


create table devolucoes (
   id               int primary key,
   pedido_id        int,
   data_devolucao   date,
   motivo_devolucao clob,
   constraint fk_pedido_devolucao foreign key ( pedido_id )
      references pedidos ( id )
);



create table suporte (
   id            int primary key,
   cliente_id    int,
   pedido_id     int,
   data_ticket   date,
   tipo_problema clob,
   resolvido     char(1),
   constraint fk_cliente_suporte foreign key ( cliente_id )
      references clientes ( id ),
   constraint fk_pedido_suporte foreign key ( pedido_id )
      references pedidos ( id )
);


create table itens_pedido (
   id             int primary key,
   pedido_id      int,
   produto_id     int,
   quantidade     int,
   preco_unitario number(10,2),
   desconto       number(10,2),
   constraint fk_pedido_item foreign key ( pedido_id )
      references pedidos ( id ),
   constraint fk_produto_pedido foreign key ( produto_id )
      references produtos ( id )
);