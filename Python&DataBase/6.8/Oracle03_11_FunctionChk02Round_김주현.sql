SQL> show user;
USER is "SCOTT"
SQL> select round(777.777, 2) as "+���� ��" from dual;

  +���� ��                                                                                                                                                                                              
----------                                                                                                                                                                                              
    777.78                                                                                                                                                                                              

SQL> select round(777.777, 0) as "0�̳� Default ���� ��" from dual;

0�̳� Default ���� ��                                                                                                                                                                                   
---------------------                                                                                                                                                                                   
                  778                                                                                                                                                                                   

SQL> select round(777.777, -2) as "-���� ��" from dual;

  -���� ��                                                                                                                                                                                              
----------                                                                                                                                                                                              
       800                                                                                                                                                                                              

SQL> spool off
