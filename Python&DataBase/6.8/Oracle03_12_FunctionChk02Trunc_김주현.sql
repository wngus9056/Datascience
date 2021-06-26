SQL> show user;
USER is "SCOTT"
SQL> select trunc(777.777, 2) as "+값일 때" from dual;

  +값일 때                                                                                                                                                                                              
----------                                                                                                                                                                                              
    777.77                                                                                                                                                                                              

SQL> select trunc(777.777, 0) as "0이나 Default 값일 때" from dual;

0이나 Default 값일 때                                                                                                                                                                                   
---------------------                                                                                                                                                                                   
                  777                                                                                                                                                                                   

SQL> select trunc(777.777, -2) as "-값일 때" from dual;

  -값일 때                                                                                                                                                                                              
----------                                                                                                                                                                                              
       700                                                                                                                                                                                              

SQL> sppool off
SP2-0042: unknown command "sppool off" - rest of line ignored.
SQL> spool off
