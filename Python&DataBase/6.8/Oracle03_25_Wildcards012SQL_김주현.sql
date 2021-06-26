SQL> show user;
USER is "SCOTT"
SQL> select saname from sawontable
  2  where saname like '±è%';

SANAME                                                                                                                                                                                                  
--------------------                                                                                                                                                                                    
±èÀ¯½Å                                                                                                                                                                                                  

SQL> select saname from sawontable
  2  where saname like '_¹Ì%';

SANAME                                                                                                                                                                                                  
--------------------                                                                                                                                                                                    
ÀÌ¹Ì¶ó                                                                                                                                                                                                  

SQL> select goname from gogektable
  2  where goname like '__';

GONAME                                                                                                                                                                                                  
--------------------                                                                                                                                                                                    
¿µÈñ                                                                                                                                                                                                    
Äµµð                                                                                                                                                                                                    
°­¹Î                                                                                                                                                                                                    
Ã¶ÀÌ                                                                                                                                                                                                    
ºä¿Ï                                                                                                                                                                                                    
¶ÊÀÌ                                                                                                                                                                                                    
¼èµ¹                                                                                                                                                                                                    
È«ÀÌ                                                                                                                                                                                                    
¾È³ª                                                                                                                                                                                                    

9 rows selected.

SQL> select saname from sawontable
  2  where saname like '%¼ø%';

SANAME                                                                                                                                                                                                  
--------------------                                                                                                                                                                                    
ÀÌ¼ø½Å                                                                                                                                                                                                  
ÀÌ¼ø¶ó                                                                                                                                                                                                  

SQL> select saname from sawontable
  2  where saname like '%¸¸';

SANAME                                                                                                                                                                                                  
--------------------                                                                                                                                                                                    
³î±â¸¸                                                                                                                                                                                                  
°øºÎ¸¸                                                                                                                                                                                                  

SQL> spool off
