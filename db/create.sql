-- CLIENTES
CREATE TABLE clientes (
  id           NUMBER PRIMARY KEY,
  nome         VARCHAR2(100),
  email        VARCHAR2(100)
);

-- VENDEDORES
CREATE TABLE vendedores (
  id           NUMBER PRIMARY KEY,
  nome         VARCHAR2(100),
  salario      NUMBER(10,2)
);

-- PRODUTOS
CREATE TABLE produtos (
  id           NUMBER PRIMARY KEY,
  nome         VARCHAR2(100),
  categoria    VARCHAR2(50),
  preco        NUMBER(10,2)
);

-- VENDAS
CREATE TABLE vendas (
  id           NUMBER PRIMARY KEY,
  id_cliente   NUMBER,
  id_vendedor  NUMBER,
  data_venda   DATE,
  CONSTRAINT fk_venda_cliente FOREIGN KEY(id_cliente) REFERENCES clientes(id),
  CONSTRAINT fk_venda_vendedor FOREIGN KEY(id_vendedor) REFERENCES vendedores(id)
);

-- ITENS_VENDA
CREATE TABLE itens_venda (
  id              NUMBER PRIMARY KEY,
  id_venda        NUMBER,
  id_produto      NUMBER,
  quantidade      NUMBER,
  valor_unitario  NUMBER(10,2),
  CONSTRAINT fk_item_venda FOREIGN KEY(id_venda) REFERENCES vendas(id),
  CONSTRAINT fk_item_produto FOREIGN KEY(id_produto) REFERENCES produtos(id)
);

-- PAGAMENTOS
CREATE TABLE pagamentos (
  id              NUMBER PRIMARY KEY,
  id_venda        NUMBER,
  tipo_pagamento  VARCHAR2(30),
  data_pagamento  DATE,
  valor           NUMBER(10,2),
  CONSTRAINT fk_pagamento_venda FOREIGN KEY(id_venda) REFERENCES vendas(id)
);
