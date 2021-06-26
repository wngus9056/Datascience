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
  7  constraint sawon_sasex_ck check(sasex in('남자', '여자'))
  8  );

Table created.

SQL> insert into sawontable values(1, '홍길동', 10, '회장', 5000, '1980/01/01', '남자', null);

1 row created.

SQL> insert into sawontable values(2, '한국남', 20, '부장', 3000, '1988/11/01', '남자', 1);

1 row created.

SQL> insert into sawontable values(3, '이순신', 20, '과장', 3500, '1985/03/01', '남자', 2);

1 row created.

SQL> insert into sawontable values(5, '이순라', 20, '사원', 1200, '1990/05/01', '여자', 3);

1 row created.

SQL> insert into sawontable values(7, '놀기만', 20, '과장', 2300, '1996/06/01', '중성', 2);
insert into sawontable values(7, '놀기만', 20, '과장', 2300, '1996/06/01', '중성', 2)
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
         1 홍길동                       10 회장                       5000 80/01/01 남자                                                                                                                
         2 한국남                       20 부장                       3000 88/11/01 남자                  1                                                                                             
         3 이순신                       20 과장                       3500 85/03/01 남자                  2                                                                                             
         5 이순라                       20 사원                       1200 90/05/01 여자                  3                                                                                             

SQL> show user
USER is "SCOTT"
SQL> spool off
