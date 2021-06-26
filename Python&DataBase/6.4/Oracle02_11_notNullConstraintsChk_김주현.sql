SQL> drop table depttable;

Table dropped.

SQL> create table deptTable (deptno number(3), dname varchar2(10), loc varchar2(10));

Table created.

SQL> insert into depttable(dname, loc) values('�ѹ���', '����')
  2  ;

1 row created.

SQL> select * from depttable;

    DEPTNO DNAME                LOC                                                                                                                                                                     
---------- -------------------- --------------------                                                                                                                                                    
           �ѹ���               ����                                                                                                                                                                    

SQL> drop table depttable;

Table dropped.

SQL> create table deptTable (deptno number(3) not null, dname varchar2(10), loc varchar2(10));

Table created.

SQL> insert into depttable(dname, loc) values('�ѹ���', '����')
  2  ;
insert into depttable(dname, loc) values('�ѹ���', '����')
*
ERROR at line 1:
ORA-01400: cannot insert NULL into ("SCOTT"."DEPTTABLE"."DEPTNO") 


SQL> insert into depttable values('10', '�ѹ���', '����')
  2  ;

1 row created.

SQL> select * from depttable;

    DEPTNO DNAME                LOC                                                                                                                                                                     
---------- -------------------- --------------------                                                                                                                                                    
        10 �ѹ���               ����                                                                                                                                                                    

SQL> spool off
