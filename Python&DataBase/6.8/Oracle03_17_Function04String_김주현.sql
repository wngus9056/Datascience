SQL> show user;
USER is "SCOTT"
SQL> select concat('Nice ', 'Day') CONCAT from dual;

CONCAT                                                                                                                                                                                                  
----------------                                                                                                                                                                                        
Nice Day                                                                                                                                                                                                

SQL> select concat('Nice ', 'Day','!!!') CONCAT from dual;
select concat('Nice ', 'Day','!!!') CONCAT from dual
       *
ERROR at line 1:
ORA-00909: invalid number of arguments 


SQL> select 'Nice ' || 'Day' || '!!!' CONCATC from dual;

CONCATC                                                                                                                                                                                                 
----------------------                                                                                                                                                                                  
Nice Day!!!                                                                                                                                                                                             

SQL> spool off
