SQL> show user;
USER is "SCOTT"
SQL> select substr('Happyday',3 ,3) from dual;

SUBSTR                                                                                                                                                                                                  
------                                                                                                                                                                                                  
ppy                                                                                                                                                                                                     

SQL> select instr('Happyday','ppy') from dual;

INSTR('HAPPYDAY','PPY')                                                                                                                                                                                 
-----------------------                                                                                                                                                                                 
                      3                                                                                                                                                                                 

SQL> select replace('Happyday', 'ppy', 'qqy') from dual;

REPLACE('HAPPYDA                                                                                                                                                                                        
----------------                                                                                                                                                                                        
Haqqyday                                                                                                                                                                                                

SQL> spool off
