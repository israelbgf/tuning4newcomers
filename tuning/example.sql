use tuning;


# Consulta problemática com ordenação e distinct:
EXPLAIN SELECT DISTINCT pedido.id,
       pedido.vendedor_id,
       pedido.total,
       pedido.status,
       pedido.numero,
       vendedor.id,
       vendedor.nome
FROM tuning_pedido pedido
       JOIN tuning_vendedor vendedor ON (pedido.vendedor_id = vendedor.id)
       JOIN tuning_item item ON (pedido.id = item.pedido_id)
WHERE
      pedido.status IN ('1', '2')
      AND (pedido.vendedor_id IN (576, 577) OR item.percentual_desconto > 0.2)
      AND pedido.empresa_id = 44
ORDER BY pedido.data_emissao DESC, pedido.numero DESC;









alter table tuning_pedido add index idx_bala_de_prata(empresa_id, status, data_emissao, numero);
alter table tuning_pedido drop index idx_bala_de_prata;
































-- Consulta Fixada... Ou não?
SET profiling = 1;

EXPLAIN SELECT pedido.id,
               pedido.vendedor_id,
               pedido.total,
               pedido.status,
               pedido.numero,
               vendedor.id,
               vendedor.nome
        FROM tuning_pedido pedido
               JOIN tuning_vendedor vendedor ON (pedido.vendedor_id = vendedor.id)
        WHERE (pedido.status IN ('1', '2') AND
               (pedido.vendedor_id IN (576, 577) OR exists(select id
                                                     from tuning_item
                                                     where percentual_desconto > 0.2
                                                       and tuning_item.pedido_id = pedido.id
                                                     limit 1)) AND
               pedido.empresa_id = 44)
        ORDER BY pedido.data_emissao DESC, pedido.numero DESC;

SET profiling = 0;
SHOW profiles;
SHOW PROFILE ALL FOR QUERY 245;

















alter table tuning_item add index idx_bala_de_prata(pedido_id, percentual_desconto);
alter table tuning_item drop index idx_bala_de_prata;






























