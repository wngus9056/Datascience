SQL> insert into depttable values('10', '醚公何', '辑匡');

1 row created.

SQL> insert into depttable values('10', '醚公何', '辑匡');

1 row created.

SQL> insert into depttable(dname, loc) values('醚公何', '辑匡')
  2  ;

1 row created.

SQL> select * from depttable;

    DEPTNO DNAME                LOC                                                                                                                                                                     
---------- -------------------- --------------------                                                                                                                                                    
        10 醚公何               辑匡                                                                                                                                                                    
        10 醚公何               辑匡                                                                                                                                                                    
            醚公何               辑匡	

SQL> delete depttable;

3 rows deleted.

SQL> select * from depttable;

no rows selected

SQL> spool off
