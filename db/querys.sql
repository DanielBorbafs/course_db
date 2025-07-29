-- 🔹 Query 1: Liste o nome de cada cliente, a data da venda e o nome do vendedor responsável.
select c.nome,
       d.data_venda,
       v.nome
  from clientes c
  join vendas d
on d.id_cliente = c.id
  join vendedores v
on d.id_vendedor = v.id;


-- 🔹 Query 2: Liste os nomes dos produtos vendidos, a quantidade e o valor total de cada item (quantidade × valor_unitario).
select p.nome,
       sum(i.quantidade) as total_qtd,
       sum(i.quantidade * i.valor_unitario) as total_vendido
  from produtos p
  join itens_venda i
on i.id_produto = p.id
 group by p.nome
 order by total_vendido desc;

-- 🔹 Query 3: Liste o nome do cliente, o tipo de pagamento e o valor pago, ordenado pelo valor decrescente.
select c.nome,
       p.tipo_pagamento,
       p.valor
  from clientes c
  join vendas v
on v.id_cliente = c.id
  join pagamentos p
on p.id_venda = v.id
 order by p.valor desc;


-- 🔹 Query 4: Liste os vendedores que já venderam mais de R$ 10.000 no total.
select vendedores.nome,
       sum(itens_venda.quantidade * itens_venda.valor_unitario) as total_vendido
  from vendedores
  join vendas v
on v.id_vendedor = vendedores.id
  join itens_venda
on itens_venda.id_venda = v.id
 group by vendedores.nome
having sum(itens_venda.quantidade * itens_venda.valor_unitario) > 10000;


-- 🔹 Query 5: Mostre o nome e o valor da maior venda feita por cada cliente.
select nome_cliente,
       max(valor_total_venda) as maior_venda
  from (
   select c.nome as nome_cliente,
          v.id as id_venda,
          sum(i.quantidade * i.valor_unitario) as valor_total_venda
     from clientes c
     join vendas v
   on v.id_cliente = c.id
     join itens_venda i
   on i.id_venda = v.id
    group by c.nome,
             v.id
)
 group by nome_cliente
 order by maior_venda desc;