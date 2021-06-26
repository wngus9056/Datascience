SQL> show user;
USER is "SCOTT"
SQL> drop table depttable;
drop table depttable
           *
ERROR at line 1:
ORA-00942: table or view does not exist 


SQL> create table gogekTable (gobun number(3),
  2  goname varchar2(10),
  3  gotel varchar2(20),
  4  gojumin varchar2(14),
  5  godam number(3),
  6  constraint dept_dept_deptno_pk primary key (deptno)
  7  );
constraint dept_dept_deptno_pk primary key (deptno)
                                            *
ERROR at line 6:
ORA-00904: "DEPTNO": invalid identifier 


SQL> create table gogekTable (gobun number(3),
  2  goname varchar2(10),
  3  gotel varchar2(20),
  4  gojumin varchar2(14),
  5  godam number(3),
  6  constraint dept_deptno_pk primary key (deptno)
  7  );
constraint dept_deptno_pk primary key (deptno)
                                       *
ERROR at line 6:
ORA-00904: "DEPTNO": invalid identifier 


SQL> drop table create table deptTable (deptno number(3),
  2  dname varchar2(10),
  3  loc varchar2(10),
  4  constraint dept_deptno_pk primary key (deptno)
  5  fdasf
  6  l;
drop table create table deptTable (deptno number(3),
           *
ERROR at line 1:
ORA-00903: invalid table name 


SQL> create table deptTable (deptno number(3),
  2  dname varchar2(10),
  3  loc varchar2(10),
  4  constraint dept_deptno_pk primary key (deptno)
  5  );

Table created.

SQL> insert into dept(dname) values('醚公何')
  2  ;
insert into dept(dname) values('醚公何')
            *
ERROR at line 1:
ORA-00942: table or view does not exist 


SQL> insert into depttable(dname) values('醚公何')
  2  ;
insert into depttable(dname) values('醚公何')
*
ERROR at line 1:
ORA-01400: cannot insert NULL into ("SCOTT"."DEPTTABLE"."DEPTNO") 


SQL> insert into depttable(deptno) values(10)
  2  ;

1 row created.

SQL> insert into depttable(deptno) values(10);
insert into depttable(deptno) values(10)
*
ERROR at line 1:
ORA-00001: unique constraint (SCOTT.DEPT_DEPTNO_PK) violated 


SQL> select * from depttable;

    DEPTNO DNAME                LOC                                                                                                                                                                     
---------- -------------------- --------------------                                                                                                                                                    
        10                                                                                                                                                                                              

SQL> spool off
