use tuning;

# ALL = Full Table Scan | Nem sempre é algo ruim (mas 99% das vezes é).
# Rows = Quantos registros serão retornados (estimativa no caso do InnoDB)
explain select * from tuning_pedido;

# Ref = A coluna que foi utiliza para utilizar o índice.
# type = descreve como tabelas são "joinadas"
explain select * from tuning_pedido where empresa_id = 27;




























# Lendo a estimativa de rows e ordem de execução.
explain select empresa.nome, colaborador.nome
        from tuning_empresa empresa
               join tuning_colaborador colaborador on empresa.id = colaborador.empresa_id
        where empresa.id between 20 and 70;

















# Removendo o custo de Ordenação e do Distinct. Consulta problemática:
EXPLAIN SELECT  `tuning_pedido`.`id`,
       `tuning_pedido`.`criador_id`,
       `tuning_pedido`.`total`,
       `tuning_pedido`.`status`,
       `tuning_pedido`.`numero`,
       `tuning_colaborador`.`id`,
       `tuning_colaborador`.`nome`
FROM `tuning_pedido` use index(`idx_empresa_id_data_emissao_numero`)
       INNER JOIN `tuning_colaborador` ON (`tuning_pedido`.`criador_id` = `tuning_colaborador`.`id`)
       LEFT OUTER JOIN `tuning_parcelacomissao` ON (`tuning_pedido`.`id` = `tuning_parcelacomissao`.`pedido_id`)
WHERE
      `tuning_pedido`.`status` IN ('1', '2')
      AND (`tuning_pedido`.`criador_id` IN (51) OR `tuning_parcelacomissao`.`colaborador_id` = 50)
      AND `tuning_pedido`.`empresa_id` = 100
ORDER BY `tuning_pedido`.`data_emissao` DESC, `tuning_pedido`.`numero` DESC; -- Ordenação, é um problema?


-- Vendo os indices
show indexes from tuning_pedido;

-- EXPLAIN é só estimativas! Nem tudo é o que parece.
select count(*) from tuning_pedido where empresa_id = 100;
select * from tuning_parcelacomissao where pedido_id = 7;









-- Consulta Fixada
EXPLAIN SELECT `tuning_pedido`.`id`,
       `tuning_pedido`.`criador_id`,
       `tuning_pedido`.`total`,
       `tuning_pedido`.`status`,
       `tuning_pedido`.`numero`,
       `tuning_colaborador`.`id`,
       `tuning_colaborador`.`nome`
FROM `tuning_pedido` FORCE INDEX (idx_empresa_id_data_emissao_numero)
       INNER JOIN `tuning_colaborador` ON (`tuning_pedido`.`criador_id` = `tuning_colaborador`.`id`)
WHERE (`tuning_pedido`.`status` IN ('1', '2') AND
       (`tuning_pedido`.`criador_id` IN (51) OR exists(select id
                                                           from tuning_parcelacomissao
                                                           where colaborador_id = 50
                                                             and `tuning_parcelacomissao`.pedido_id = `tuning_pedido`.id
                                                           limit 1)) AND
       `tuning_pedido`.`empresa_id` = 100)
ORDER BY `tuning_pedido`.`data_emissao` DESC, `tuning_pedido`.`numero` DESC;


























-- Consulta utilizando coalesce (ou qualquer função que gere algo dinâmico)
explain SELECT (coalesce(data_emissao, '2018-11-05 00:14:18.805381')) AS `data_emissao_sem_null`,
       `tuning_pedido`.`id`,
       `tuning_pedido`.`criador_id`,
       `tuning_pedido`.`total`,
       `tuning_pedido`.`status`,
       `tuning_pedido`.`numero`,
       `tuning_colaborador`.`id`,
       `tuning_colaborador`.`nome`
FROM `tuning_pedido` use index (idx_empresa_id_data_emissao_numero)
       INNER JOIN `tuning_colaborador` ON (`tuning_pedido`.`criador_id` = `tuning_colaborador`.`id`)
WHERE (`tuning_pedido`.`status` IN ('1', '2') AND `tuning_pedido`.`empresa_id` = 100)
ORDER BY `data_emissao_sem_null` DESC, `tuning_pedido`.`numero` DESC;









-- Cuidado com Likes!
explain select *
        from tuning_empresa
        where email like '%angela%';













-- Respeite a ordem e cuide de sua projeção!
SET profiling = 1;
explain select empresa_id, data_emissao, numero from tuning_pedido where empresa_id = 100 order by data_emissao, numero;
SET profiling = 0;
SHOW PROFILES;
SHOW PROFILE ALL FOR QUERY 92;
