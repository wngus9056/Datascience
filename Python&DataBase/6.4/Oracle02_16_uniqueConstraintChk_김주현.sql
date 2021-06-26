SQL> drop table depttable;

Table dropped.

SQL> show user
USER is "SCOTT"
SQL> create table deptTable (deptno number(3) constraint dept_deptno_uq unique, dname varchar2(10), loc varchar2(10));

Table created.

SQL> insert into depttable values('10', '�ѹ���', '����')
  2  ;

1 row created.

SQL> insert into depttable values('10', '�ѹ���1', '����');
insert into depttable values('10', '�ѹ���1', '����')
*
ERROR at line 1:
ORA-00001: unique constraint (SCOTT.DEPT_DEPTNO_UQ) violated 


SQL> select * from depttable;

    DEPTNO DNAME                LOC                                                                                                                                                                     
---------- -------------------- --------------------                                                                                                                                                    
        10 �ѹ���               ����                                                                                                                                                                    

SQL> spool off
