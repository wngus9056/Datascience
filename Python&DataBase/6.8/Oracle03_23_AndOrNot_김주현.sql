SQL> show user;
USER is "SCOTT"
SQL> select saname ����̸�, deptno �μ���ȣ from sawontable where deptno = 10 or deptno = 20;

����̸�               �μ���ȣ                                                                                                                                                                         
-------------------- ----------                                                                                                                                                                         
ȫ�浿                       10                                                                                                                                                                         
�ѱ���                       20                                                                                                                                                                         
�̼���                       20                                                                                                                                                                         
�̼���                       20                                                                                                                                                                         
��⸸                       20                                                                                                                                                                         
�亰��                       20                                                                                                                                                                         
ä�ö�                       20                                                                                                                                                                         
����ȭ                       10                                                                                                                                                                         
�Ӳ���                       20                                                                                                                                                                         
������                       10                                                                                                                                                                         
�����                       10                                                                                                                                                                         
����ȭ                       10                                                                                                                                                                         
������                       10                                                                                                                                                                         

13 rows selected.

SQL> select saname ����̸�, deptno �μ���ȣ, sajob ���� from sawontable where deptno = 10 and sajob ='���';

����̸�               �μ���ȣ ����                                                                                                                                                                    
-------------------- ---------- --------------------                                                                                                                                                    
����ȭ                       10 ���                                                                                                                                                                    
������                       10 ���                                                                                                                                                                    

SQL> select saname ����̸�, deptno �μ���ȣ, sajob ���� from sawontable where not deptno = 10;

����̸�               �μ���ȣ ����                                                                                                                                                                    
-------------------- ---------- --------------------                                                                                                                                                    
�ѱ���                       20 ����                                                                                                                                                                    
�̼���                       20 ����                                                                                                                                                                    
�̼���                       20 ���                                                                                                                                                                    
��⸸                       20 ����                                                                                                                                                                    
�亰��                       20 ����                                                                                                                                                                    
ä�ö�                       20 ���                                                                                                                                                                    
�̼���                       30 ����                                                                                                                                                                    
�Ӳ���                       20 ���                                                                                                                                                                    
���θ�                       30 ����                                                                                                                                                                    
ä��ȭ                       30 �븮                                                                                                                                                                    
�̶̹�                       30 �븮                                                                                                                                                                    
������                       30 ���                                                                                                                                                                    
������                       30 ���                                                                                                                                                                    
������                       30 ���                                                                                                                                                                    

14 rows selected.

SQL> spool off
