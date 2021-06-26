SQL> show user
USER is "HR"
SQL> conn scott/happyday
Connected.
SQL> select owner, constraint_name, table_name from user_constraints;

OWNER
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CONSTRAINT_NAME                                              TABLE_NAME
------------------------------------------------------------ ------------------------------------------------------------
SCOTT
SYS_C006999                                                  DEPTTABLE


SQL> drop table depttable;

Table dropped.

SQL> drop table user_constraints;
drop table user_constraints
           *
ERROR at line 1:
ORA-00942: table or view does not exist


SQL> create table deptTable (deptno number(3) constraint dept_deptno_nn, dname varchar2(10), loc varchar2(10));
create table deptTable (deptno number(3) constraint dept_deptno_nn, dname varchar2(10), loc varchar2(10))
                                         *
ERROR at line 1:
ORA-02253: constraint specification not allowed here


SQL> create table deptTable (deptno number(3)constraint dept_deptno_nn, dname varchar2(10), loc varchar2(10));
create table deptTable (deptno number(3)constraint dept_deptno_nn, dname varchar2(10), loc varchar2(10))
                                        *
ERROR at line 1:
ORA-02253: constraint specification not allowed here


SQL> create table deptTable (deptno number(3) constraint dept_deptno_nn not null, dname varchar2(10), loc varchar2(10));

Table created.

SQL> select owner, constraint_name, table_name from user_constraints;

OWNER
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
CONSTRAINT_NAME                                              TABLE_NAME
------------------------------------------------------------ ------------------------------------------------------------
SCOTT
DEPT_DEPTNO_NN                                               DEPTTABLE