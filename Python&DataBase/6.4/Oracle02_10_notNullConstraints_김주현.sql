SQL> insert into depttable values('10', '�ѹ���', '����');

1 row created.

SQL> insert into depttable values('10', '�ѹ���', '����');

1 row created.

SQL> insert into depttable(dname, loc) values('�ѹ���', '����')
  2  ;

1 row created.

SQL> select * from depttable;

    DEPTNO DNAME                LOC                                                                                                                                                                     
---------- -------------------- --------------------                                                                                                                                                    
        10 �ѹ���               ����                                                                                                                                                                    
        10 �ѹ���               ����                                                                                                                                                                    
            �ѹ���               ����	

SQL> delete depttable;

3 rows deleted.

SQL> select * from depttable;

no rows selected

SQL> spool off
