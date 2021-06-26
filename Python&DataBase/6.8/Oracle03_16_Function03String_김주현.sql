SQL> show user;
USER is "SCOTT"
SQL> select upper('Korea') from dual;

UPPER('KOR                                                                                                                                                                                              
----------                                                                                                                                                                                              
KOREA                                                                                                                                                                                                   

SQL> select lower('Korea') from dual;

LOWER('KOR                                                                                                                                                                                              
----------                                                                                                                                                                                              
korea                                                                                                                                                                                                   

SQL> select initcap('Korea') from dual;

INITCAP('K                                                                                                                                                                                              
----------                                                                                                                                                                                              
Korea                                                                                                                                                                                                   

SQL> select initcap('Korea of of oof fj') from dual;

INITCAP('KOREAOFOFOOFFJ')                                                                                                                                                                               
------------------------------------                                                                                                                                                                    
Korea Of Of Oof Fj                                                                                                                                                                                      

SQL> select length('Korea of of oof fj') from dual;

LENGTH('KOREAOFOFOOFFJ')                                                                                                                                                                                
------------------------                                                                                                                                                                                
                      18                                                                                                                                                                                

SQL> spool off
