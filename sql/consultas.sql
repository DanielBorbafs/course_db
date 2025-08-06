-- QUERY QUE TRAZ O VALOR TOTAL R$ DE LUCRO BRUTO COM PEDIDOS FINALIZADOS
select sum(valor) as valor_final
  from (
   select ( quantidade * preco_unitario ) as valor
     from itens_pedido
     join pedidos
   on itens_pedido.pedido_id = pedidos.id
    where pedidos.status_pedido = 'Finalizado'
);

-- VALOR TOTAL DE CUSTO COM TODAS AS CAMPANHAS
select sum(custo_total) as valor_gasto
  from campanhas;

-- VALOR GASTO POR CANAL DE CAMPANHAS
select canal,
       sum(custo_total) as custo_total
  from campanhas
 group by canal
 order by custo_total desc;


 -- CANAL DE CAMPANHA COM MAIS CLIQUES
select c.canal,
       count(k.campanha_id) as cliques_totais
  from campanhas c
  join cliques_campanha k
on c.id = k.campanha_id
 group by c.canal
 order by cliques_totais desc;


 -- QUANTIDADE DE CLIENTES 
select count(id) as quantidade_cliente
  from clientes;

-- QUANTIDADE DE CLIENTES AGRUPADO POR SEXO
select sexo,
       count(id) as quantidade_cliente
  from clientes
 group by sexo;

-- DISTRIBUIÇÃO DEMOGRÁFICA
select uf,
       count(id) as quantidade_clientes
  from clientes
 group by uf
 order by quantidade_clientes desc;

 -- QUANTIDADE TOTAL DE DEVOLUCOES
select count(id) as contagem
  from devolucoes;