SQL> create table deptTable (deptno number(3), dname varchar2(10), loc varchar2(10));

Table created.

SQL> insert into depttable values('10', '�ѹ���', '����')
  2  ;

1 row created.

SQL> insert into depttable values('10', '�ѹ���1', '����')
  2  ;

1 row created.

SQL> select * from depttable;

    DEPTNO DNAME                LOC                                                                                                                                                                     
---------- -------------------- --------------------                                                                                                                                                    
        10 �ѹ���               ����                                                                                                                                                                    
        10 �ѹ���1              ����                                                                                                                                                                    

SQL> spool off
