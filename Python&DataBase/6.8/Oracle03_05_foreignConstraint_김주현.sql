SQL> show user;
USER is "SCOTT"
SQL> select * from tab;

TNAME                                                        TABTYPE         CLUSTERID                                                                                                                  
------------------------------------------------------------ -------------- ----------                                                                                                                  
GOGEKTABLE                                                   TABLE                                                                                                                                      
MEMBERT01                                                    TABLE                                                                                                                                      

SQL> create table deptTable (deptno number(3),
  2  dname varchar2(10),
  3  loc varchar2(10),
  4  constraint dept_deptno_pk primary key (deptno)
  5  );

Table created.

SQL> create table sawonTable (sabun number(3),
  2  saname varchar2(10), deptno number(3),
  3  sajob varchar2(10), sapay number(10),
  4  sahire date default sysdate,
  5  sasex varchar2(6),
  6  samgr number(3),
  7  constraint sawon_sasex_ck check(sasex in('����', '����')),
  8  constraint sawon_deptno_fk foreign key (deptno) references depttable(deptno)
  9  );

Table created.

SQL> select owner, constraint_name, table_name
  2  from user_constraints;

OWNER                                                                                                                                                                                                   
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CONSTRAINT_NAME                                              TABLE_NAME                                                                                                                                 
------------------------------------------------------------ ------------------------------------------------------------                                                                               
SCOTT                                                                                                                                                                                                   
DEPT_DEPTNO_PK                                               DEPTTABLE                                                                                                                                  
                                                                                                                                                                                                        
SCOTT                                                                                                                                                                                                   
SAWON_SASEX_CK                                               SAWONTABLE                                                                                                                                 
                                                                                                                                                                                                        
SCOTT                                                                                                                                                                                                   
SAWON_DEPTNO_FK                                              SAWONTABLE                                                                                                                                 
                                                                                                                                                                                                        

SQL> select * from depttable;

no rows selected

SQL> insert into depttable values('10', '�ѹ���', '����');

1 row created.

SQL> insert into depttable values('20', '������', '����');

1 row created.

SQL> insert into sawontable values(2, '�ѱ���', 20, '����', 3000, '1988/11/01', '����', 1);

1 row created.

SQL> insert into sawontable values(3, '�̼���', 20, '����', 3500, '1985/03/01', '����', 2);

1 row created.

SQL> insert into sawontable values(17, '�̼���', 30, '����', 2803, '1984/05/01', '����', 1);
insert into sawontable values(17, '�̼���', 30, '����', 2803, '1984/05/01', '����', 1)
*
ERROR at line 1:
ORA-02291: integrity constraint (SCOTT.SAWON_DEPTNO_FK) violated - parent key not found 


SQL> insert into sawontable values(1, 'ȫ�浿', 10, 'ȸ��', 5000, '1980/01/01', '����', null);

1 row created.

SQL> select * from depttable;

    DEPTNO DNAME                LOC                                                                                                                                                                     
---------- -------------------- --------------------                                                                                                                                                    
        10 �ѹ���               ����                                                                                                                                                                    
        20 ������               ����                                                                                                                                                                    

SQL> select * from sawontable;

     SABUN SANAME                   DEPTNO SAJOB                     SAPAY SAHIRE   SASEX             SAMGR                                                                                             
---------- -------------------- ---------- -------------------- ---------- -------- ------------ ----------                                                                                             
         2 �ѱ���                       20 ����                       3000 88/11/01 ����                  1                                                                                             
         3 �̼���                       20 ����                       3500 85/03/01 ����                  2                                                                                             
         1 ȫ�浿                       10 ȸ��                       5000 80/01/01 ����                                                                                                                

SQL> show user;
USER is "SCOTT"
SQL> spool off
