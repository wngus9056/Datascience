SQL> start C:\Study\TableMember.sql
SP2-0310: unable to open file "C:\Study\TableMember.sql"
SQL> start C:\Study\TableMember.sql

Table dropped.

select mem_name as "회원이름", mem_id as "아이디", mem_pwd as "비밀번호", mem_email as "이메일", mem_phone as "전화번호", mem_addr as "주소" from membert01
                                                                                                                                                          *
ERROR at line 1:
ORA-00942: table or view does not exist 



no rows selected

SQL> start C:\Study\TableMember.sql
drop table membert01
           *
ERROR at line 1:
ORA-00942: table or view does not exist 


select mem_name as "회원이름", mem_id as "아이디", mem_pwd as "비밀번호", mem_email as "이메일", mem_phone as "전화번호", mem_addr as "주소" from membert01
                                                                                                                                                          *
ERROR at line 1:
ORA-00942: table or view does not exist 



no rows selected

SQL> start C:\Study\TableMember.sql
drop table membert01
           *
ERROR at line 1:
ORA-00942: table or view does not exist 


select mem_name as "회원이름", mem_id as "아이디", mem_pwd as "비밀번호", mem_email as "이메일", mem_phone as "전화번호", mem_addr as "주소" from membert01
                                                                                                                                                          *
ERROR at line 1:
ORA-00942: table or view does not exist 



no rows selected

SQL> start C:\Study\TableMember.sql
drop table membert01
           *
ERROR at line 1:
ORA-00942: table or view does not exist 



Table created.


TNAME                                                        TABTYPE         CLUSTERID                                                                                                                  
------------------------------------------------------------ -------------- ----------                                                                                                                  
MEMBERT01                                                    TABLE                                                                                                                                      

SQL> spool off
