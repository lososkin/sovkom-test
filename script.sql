/*UTF-8 file*/
drop table if exists data cascade;
create table data(ACCOUNT_RK int,INTERNAL_ORG_ORIGINAL_RK int, LOAN_AMOUNT decimal(20,2), APPLICATION_DT timestamp);
copy data from '/home/losos/sovkom-test/data.csv' delimiter ';' csv header;
