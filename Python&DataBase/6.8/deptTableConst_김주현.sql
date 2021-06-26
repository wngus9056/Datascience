drop table depttable;

create table deptTable (deptno number(3), 
dname varchar2(10) constraint dept_dname_uq unique, 
loc varchar2(10),
constraint dept_deptno_pk primary key (deptno)
);