SQL> show user;
USER is "SCOTT"
SQL> select trunc(777.777, 2) as "+���� ��" from dual;

  +���� ��                                                                                                                                                                                              
----------                                                                                                                                                                                              
    777.77                                                                                                                                                                                              

SQL> select trunc(777.777, 0) as "0�̳� Default ���� ��" from dual;

0�̳� Default ���� ��                                                                                                                                                                                   
---------------------                                                                                                                                                                                   
                  777                                                                                                                                                                                   

SQL> select trunc(777.777, -2) as "-���� ��" from dual;

  -���� ��                                                                                                                                                                                              
----------                                                                                                                                                                                              
       700                                                                                                                                                                                              

SQL> sppool off
SP2-0042: unknown command "sppool off" - rest of line ignored.
SQL> spool off
