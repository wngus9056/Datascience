SQL> show user;
USER is "SCOTT"
SQL> select saname from sawontable
  2  where saname like '��%';

SANAME                                                                                                                                                                                                  
--------------------                                                                                                                                                                                    
������                                                                                                                                                                                                  

SQL> select saname from sawontable
  2  where saname like '_��%';

SANAME                                                                                                                                                                                                  
--------------------                                                                                                                                                                                    
�̶̹�                                                                                                                                                                                                  

SQL> select goname from gogektable
  2  where goname like '__';

GONAME                                                                                                                                                                                                  
--------------------                                                                                                                                                                                    
����                                                                                                                                                                                                    
ĵ��                                                                                                                                                                                                    
����                                                                                                                                                                                                    
ö��                                                                                                                                                                                                    
���                                                                                                                                                                                                    
����                                                                                                                                                                                                    
�赹                                                                                                                                                                                                    
ȫ��                                                                                                                                                                                                    
�ȳ�                                                                                                                                                                                                    

9 rows selected.

SQL> select saname from sawontable
  2  where saname like '%��%';

SANAME                                                                                                                                                                                                  
--------------------                                                                                                                                                                                    
�̼���                                                                                                                                                                                                  
�̼���                                                                                                                                                                                                  

SQL> select saname from sawontable
  2  where saname like '%��';

SANAME                                                                                                                                                                                                  
--------------------                                                                                                                                                                                    
��⸸                                                                                                                                                                                                  
���θ�                                                                                                                                                                                                  

SQL> spool off
