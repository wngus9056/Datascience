SQL> create table deptTable (deptno number(3), dname varchar2(10), loc varchar2(10));

Table created.

SQL> insert into depttable values('10', '醚公何', '辑匡')
  2  ;

1 row created.

SQL> insert into depttable values('10', '醚公何1', '辑匡')
  2  ;

1 row created.

SQL> select * from depttable;

    DEPTNO DNAME                LOC                                                                                                                                                                     
---------- -------------------- --------------------                                                                                                                                                    
        10 醚公何               辑匡                                                                                                                                                                    
        10 醚公何1              辑匡                                                                                                                                                                    

SQL> spool off
