SQL> show user;
USER is "SCOTT"
SQL> select round(777.777, 2) as "+값일 때" from dual;

  +값일 때                                                                                                                                                                                              
----------                                                                                                                                                                                              
    777.78                                                                                                                                                                                              

SQL> select round(777.777, 0) as "0이나 Default 값일 때" from dual;

0이나 Default 값일 때                                                                                                                                                                                   
---------------------                                                                                                                                                                                   
                  778                                                                                                                                                                                   

SQL> select round(777.777, -2) as "-값일 때" from dual;

  -값일 때                                                                                                                                                                                              
----------                                                                                                                                                                                              
       800                                                                                                                                                                                              

SQL> spool off
