SQL> select * from tab;

TNAME                                                        TABTYPE         CLUSTERID                                                                                                                  
------------------------------------------------------------ -------------- ----------                                                                                                                  
DEPTTABLE                                                    TABLE                                                                                                                                      
GOGEKTABLE                                                   TABLE                                                                                                                                      
MEMBERT01                                                    TABLE                                                                                                                                      
SAWONTABLE                                                   TABLE                                                                                                                                      

SQL> drop table depttable;
drop table depttable
           *
ERROR at line 1:
ORA-02449: unique/primary keys in table referenced by foreign keys 


SQL> drop table gogektable;

Table dropped.

SQL> drop table sawontable;

Table dropped.

SQL> drop table depttable;

Table dropped.

SQL> select * from tab;

TNAME                                                        TABTYPE         CLUSTERID                                                                                                                  
------------------------------------------------------------ -------------- ----------                                                                                                                  
MEMBERT01                                                    TABLE                                                                                                                                      

SQL> show user
USER is "SCOTT"
SQL> spool off
