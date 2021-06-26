SQL> show user;
USER is "SCOTT"
SQL> select * from tab;

TNAME                                                        TABTYPE         CLUSTERID                                                                                                                  
------------------------------------------------------------ -------------- ----------                                                                                                                  
MEMBERT01                                                    TABLE                                                                                                                                      

SQL> create table deptTable (deptno number(3),
  2  dname varchar2(10) constraint dept_dname_uq unique,
  3  loc varchar2(10),
  4  constraint dept_deptno_pk primary key (deptno) on delete cascade
  5  );
constraint dept_deptno_pk primary key (deptno) on delete cascade
                                               *
ERROR at line 4:
ORA-00907: missing right parenthesis 


SQL> create table deptTable (deptno number(3),
  2  dname varchar2(10) constraint dept_dname_uq unique,
  3  loc varchar2(10),
  4  constraint dept_deptno_pk primary key (deptno)
  5  );

Table created.

SQL> create table sawonTable (sabun number(3),
  2  saname varchar2(10), deptno number(3) not null,
  3  sajob varchar2(10), sapay number(10),
  4  sahire date default sysdate,
  5  sasex varchar2(6),
  6  samgr number(3),
  7  constraint sawon_sasex_ck check(sasex in('남자', '여자')),
  8  constraint sawon_sabun_pk primary key (sabun),
  9  constraint sawon_deptno_fk foreign key (deptno) references depttable(deptno) on delete cascade,
 10  constraint sawon_samgr_fk foreign key (samgr) references sawontable(sabun)
 11  );

Table created.

SQL> insert into depttable values('10', '총무부', '서울');

1 row created.

SQL> insert into depttable values('20', '영업부', '대전');

1 row created.

SQL> insert into sawontable values(1, '홍길동', 10, '회장', 5000, '1980/01/01', '남자', null);

1 row created.

SQL> insert into sawontable values(2, '한국남', 20, '부장', 3000, '1988/11/01', '남자', 1);

1 row created.

SQL> delete from dept where deptno = 10
  2  ;
delete from dept where deptno = 10
            *
ERROR at line 1:
ORA-00942: table or view does not exist 


SQL> delete from dept where deptno = 20
  2  ;
delete from dept where deptno = 20
            *
ERROR at line 1:
ORA-00942: table or view does not exist 


SQL> delete from depttable where doptno = 10
  2  ;
delete from depttable where doptno = 10
                            *
ERROR at line 1:
ORA-00904: "DOPTNO": invalid identifier 


SQL> delete from depttable where deptno = 10
  2  ;
delete from depttable where deptno = 10
*
ERROR at line 1:
ORA-02292: integrity constraint (SCOTT.SAWON_SAMGR_FK) violated - child record found 


SQL> delete from depttable where deptno = 20;

1 row deleted.

SQL> select * from depttable;

    DEPTNO DNAME                LOC                                                                                                                                                                     
---------- -------------------- --------------------                                                                                                                                                    
        10 총무부               서울                                                                                                                                                                    

SQL> select * from sawontable;

     SABUN SANAME                   DEPTNO SAJOB                     SAPAY SAHIRE   SASEX             SAMGR                                                                                             
---------- -------------------- ---------- -------------------- ---------- -------- ------------ ----------                                                                                             
         1 홍길동                       10 회장                       5000 80/01/01 남자                                                                                                                

SQL> spool off
