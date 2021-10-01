/*UTF-8 file*/
drop view if exists date_pos;
drop view if exists date;
drop view if exists pos;
drop view if exists sum;
CREATE VIEW date as select distinct APPLICATION_DT Date from data order by APPLICATION_DT;
CREATE VIEW pos as select distinct INTERNAL_ORG_ORIGINAL_RK as Pos from data order by INTERNAL_ORG_ORIGINAL_RK;
create view date_pos as select * from date,pos;
CREATE VIEW sum as select APPLICATION_DT as date, INTERNAL_ORG_ORIGINAL_RK as pos, sum(LOAN_AMOUNT) as Сумма_выдач from data group by date, pos;
select date_pos.Date, date_pos.Pos, coalesce(Сумма_выдач,0) from date_pos left join sum on date_pos.date=sum.date and date_pos.pos=sum.pos;
