--- [ Perfil Geral dos Clientes] -----
/*
"um relatório com a quantidade total de clientes cadastrados, 
mostrando também quantos são homens e quantos são mulheres,
e a média de idade por grupo*/

-- QUANTIDADE TOTAL DE CLIENTES
select count(id) as qtd_clientes
  from clientes;

-- QUANTIDADE DE CLIENTES MASCULINOS E FEMININOS
select sexo,
       count(id) as qtd_clientes
  from clientes
 group by sexo;

-- MÉDIA DE IDADE POR GRUPO
select sexo,
       round(
          avg(trunc(months_between(
             sysdate,
             data_nascimento
          ) / 12)),
          2
       ) as media_idade
  from clientes
 group by sexo;


--- [ Comportamento de Acesso dos Clientes ] -----

/* Liste os 5 produtos mais clicados nas campanhas nos últimos 3 meses, 
e informe quantos cliques cada um recebeu."
*/
select p.nome_produto,
       count(c.produto_id) as qtd_cliques
  from cliques_campanha c
 inner join produtos p
on p.id = c.produto_id
 where c.data_clique >= sysdate - 90
 group by p.nome_produto
 order by qtd_cliques desc
 fetch first 5 rows only;



--- [ Vendas Gerais ] -----

/* Total de vendas e o valor total recebido por canal de venda, 
considerando apenas pedidos finalizados.
*/

select p.canal_venda,
       round(
          sum(i.quantidade *(i.preco_unitario - i.desconto)),
          2
       ) as valor_total
  from pedidos p
 inner join itens_pedido i
on i.pedido_id = p.id
 where p.status_pedido = 'Finalizado'
 group by p.canal_venda;


--- [ Análise de produtos ] -----

 -- 10 categorias de produtos que mais geraram receita no último ano, junto com o valor total vendido.
select p.categoria,
       sum(i.quantidade) as qtd_vendas,
       sum(i.quantidade *(i.preco_unitario - i.desconto)) as valor_total
  from produtos p
  join itens_pedido i
on i.produto_id = p.id
  join pedidos x
on i.pedido_id = x.id
 where x.data_pedido >= add_months(
   sysdate,
   -12
)
 group by p.categoria
 order by valor_total desc
 fetch first 10 rows only;

--- [ Fornecedores ] -----


-- Fornecedores que entregam produtos da categoria SOFTWARE e a data de contrato
select nome,
       trim(substr(
          categoria_produto,
          1,
          instr(
             categoria_produto,
             '-'
          ) - 1
       )) as produtos,
       data_contrato
  from fornecedores
 where categoria_produto like 'Software%'
 order by data_contrato desc;


--- [ Reposição de estoque ] -----

--- [ Campanha de marketing ] -----

--- [ Análise de pagamentos ] -----

--- [ Entregas ] -----

--- [ Devoluções ] -----

--- [ Suporte ao cliente ] -----

--- [ Análise Cruzada - Clientes e Pedidos ] -----

--- [ Análise Cruzada - Campanhas e Pedidos ] -----