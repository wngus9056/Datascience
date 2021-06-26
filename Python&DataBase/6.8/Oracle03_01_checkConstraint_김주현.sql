SQL> 
SQL> show user
USER is "SCOTT"
SQL> select * from tab;

TNAME                                                        TABTYPE         CLUSTERID                                                                                                                  
------------------------------------------------------------ -------------- ----------                                                                                                                  
GOGEKTABLE                                                   TABLE                                                                                                                                      
MEMBERT01                                                    TABLE                                                                                                                                      

SQL> create table sawonTable (sabun number(3),
  2  saname varchar2(10), deptno number(3),
  3  sajob varchar2(10), sapay number(10),
  4  sahire date,
  5  sasex varchar2(6),
  6  samgr number(3));

Table created.

SQL> insert into sawontable values(1, 'ȫ�浿', 10, 'ȸ��', 5000, '1980/01/01', '����', null);

1 row created.

SQL> insert into sawontable values(2, '�ѱ���', 20, '����', 3000, '1988/11/01', '����', 1);

1 row created.

SQL> insert into sawontable values(3, '�̼���', 20, '����', 3500, '1985/03/01', '����', 2);

1 row created.

SQL> insert into sawontable values(5, '�̼���', 20, '���', 1200, '1990/05/01', '����', 3);

1 row created.

SQL> insert into sawontable values(7, '��⸸', 20, '����', 2300, '1996/06/01', '�߼�', 2);

1 row created.

SQL> insert into sawontable values(2, '�ѱ���', 20, '����', 3000, '1988/11/01', '����', 1);

1 row created.

SQL> select * sawontable;
select * sawontable
         *
ERROR at line 1:
ORA-00923: FROM keyword not found where expected 


SQL> select * from sawontable;

     SABUN SANAME                   DEPTNO SAJOB                     SAPAY SAHIRE   SASEX             SAMGR                                                                                             
---------- -------------------- ---------- -------------------- ---------- -------- ------------ ----------                                                                                             
         1 ȫ�浿                       10 ȸ��                       5000 80/01/01 ����                                                                                                                
         2 �ѱ���                       20 ����                       3000 88/11/01 ����                  1                                                                                             
         3 �̼���                       20 ����                       3500 85/03/01 ����                  2                                                                                             
         5 �̼���                       20 ���                       1200 90/05/01 ����                  3                                                                                             
         7 ��⸸                       20 ����                       2300 96/06/01 �߼�                  2                                                                                             
         2 �ѱ���                       20 ����                       3000 88/11/01 ����                  1                                                                                             

6 rows selected.

SQL> spool off
