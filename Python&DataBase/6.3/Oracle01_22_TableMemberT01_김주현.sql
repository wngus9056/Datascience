SQL> start C:\Study\TableMember.sql
SP2-0310: unable to open file "C:\Study\TableMember.sql"
SQL> start C:\Study\TableMember.sql

Table dropped.

select mem_name as "ȸ���̸�", mem_id as "���̵�", mem_pwd as "��й�ȣ", mem_email as "�̸���", mem_phone as "��ȭ��ȣ", mem_addr as "�ּ�" from membert01
                                                                                                                                                          *
ERROR at line 1:
ORA-00942: table or view does not exist 



no rows selected

SQL> start C:\Study\TableMember.sql
drop table membert01
           *
ERROR at line 1:
ORA-00942: table or view does not exist 


select mem_name as "ȸ���̸�", mem_id as "���̵�", mem_pwd as "��й�ȣ", mem_email as "�̸���", mem_phone as "��ȭ��ȣ", mem_addr as "�ּ�" from membert01
                                                                                                                                                          *
ERROR at line 1:
ORA-00942: table or view does not exist 



no rows selected

SQL> start C:\Study\TableMember.sql
drop table membert01
           *
ERROR at line 1:
ORA-00942: table or view does not exist 


select mem_name as "ȸ���̸�", mem_id as "���̵�", mem_pwd as "��й�ȣ", mem_email as "�̸���", mem_phone as "��ȭ��ȣ", mem_addr as "�ּ�" from membert01
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
