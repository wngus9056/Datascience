SQL> drop table depttable;

Table dropped.

SQL> create table deptTable (deptno number(3), dname varchar2(10), loc varchar2(10));

Table created.

SQL> insert into depttable(dname, loc) values('醚公何', '辑匡')
  2  ;

1 row created.

SQL> select * from depttable;

    DEPTNO DNAME                LOC                                                                                                                                                                     
---------- -------------------- --------------------                                                                                                                                                    
           醚公何               辑匡                                                                                                                                                                    

SQL> drop table depttable;

Table dropped.

SQL> create table deptTable (deptno number(3) not null, dname varchar2(10), loc varchar2(10));

Table created.

SQL> insert into depttable(dname, loc) values('醚公何', '辑匡')
  2  ;
insert into depttable(dname, loc) values('醚公何', '辑匡')
*
ERROR at line 1:
ORA-01400: cannot insert NULL into ("SCOTT"."DEPTTABLE"."DEPTNO") 


SQL> insert into depttable values('10', '醚公何', '辑匡')
  2  ;

1 row created.

SQL> select * from depttable;

    DEPTNO DNAME                LOC                                                                                                                                                                     
---------- -------------------- --------------------                                                                                                                                                    
        10 醚公何               辑匡                                                                                                                                                                    

SQL> spool off
