SQL> show user
USER is "SCOTT"
SQL> drop table sawontable;

Table dropped.

SQL> create table sawonTable (sabun number(3),
  2  saname varchar2(10), deptno number(3),
  3  sajob varchar2(10), sapay number(10),
  4  sahire date,
  5  sasex varchar2(6),
  6  samgr number(3),
  7  constraint sawon_sasex_ck check(sasex in('����', '����'))
  8  );

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
insert into sawontable values(7, '��⸸', 20, '����', 2300, '1996/06/01', '�߼�', 2)
*
ERROR at line 1:
ORA-02290: check constraint (SCOTT.SAWON_SASEX_CK) violated 


SQL> select owner, constraint_name, table_name
  2  from user_constraints;

OWNER                                                                                                                                                                                                   
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CONSTRAINT_NAME                                              TABLE_NAME                                                                                                                                 
------------------------------------------------------------ ------------------------------------------------------------                                                                               
SCOTT                                                                                                                                                                                                   
SAWON_SASEX_CK                                               SAWONTABLE                                                                                                                                 
                                                                                                                                                                                                        

SQL> select * from sawontable;

     SABUN SANAME                   DEPTNO SAJOB                     SAPAY SAHIRE   SASEX             SAMGR                                                                                             
---------- -------------------- ---------- -------------------- ---------- -------- ------------ ----------                                                                                             
         1 ȫ�浿                       10 ȸ��                       5000 80/01/01 ����                                                                                                                
         2 �ѱ���                       20 ����                       3000 88/11/01 ����                  1                                                                                             
         3 �̼���                       20 ����                       3500 85/03/01 ����                  2                                                                                             
         5 �̼���                       20 ���                       1200 90/05/01 ����                  3                                                                                             

SQL> show user
USER is "SCOTT"
SQL> spool off
