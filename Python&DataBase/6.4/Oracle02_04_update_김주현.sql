SQL> 
SQL> show user;
USER is "SCOTT"
SQL> desc membert01;
 Name                                                                                                              Null?    Type
 ----------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------
 MEM_NAME                                                                                                                   VARCHAR2(20)
 MEM_ID                                                                                                                     VARCHAR2(20)
 MEM_PWD                                                                                                                    VARCHAR2(20)
 MEM_EMAIL                                                                                                                  VARCHAR2(20)
 MEM_PHONE                                                                                                                  VARCHAR2(20)
 MEM_ADDR                                                                                                                   VARCHAR2(20)

SQL> update membert01
  2  set mem_pwd = '4321'
  3  ;

5 rows updated.

SQL> select * from membert01;

MEM_NAME                                 MEM_ID                                   MEM_PWD                                  MEM_EMAIL                                                                    
---------------------------------------- ---------------------------------------- ---------------------------------------- ----------------------------------------                                     
MEM_PHONE                                MEM_ADDR                                                                                                                                                       
---------------------------------------- ----------------------------------------                                                                                                                       
??????                                   orange                                   4321                                     orange@test.com                                                              
032                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        
????                                     red                                      4321                                     red@test.com                                                                 
044                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        
??????                                   yellow                                   4321                                     yellow@test.com                                                              
032                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        
??????                                   green                                    4321                                     green@test.com                                                               
044                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        
????                                     blue                                     4321                                     blue@test.com                                                                
044                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        

SQL> update membert01
  2  set mem_pwd = '1234';

5 rows updated.

SQL> select * from membert01;

MEM_NAME                                 MEM_ID                                   MEM_PWD                                  MEM_EMAIL                                                                    
---------------------------------------- ---------------------------------------- ---------------------------------------- ----------------------------------------                                     
MEM_PHONE                                MEM_ADDR                                                                                                                                                       
---------------------------------------- ----------------------------------------                                                                                                                       
??????                                   orange                                   1234                                     orange@test.com                                                              
032                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        
????                                     red                                      1234                                     red@test.com                                                                 
044                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        
??????                                   yellow                                   1234                                     yellow@test.com                                                              
032                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        
??????                                   green                                    1234                                     green@test.com                                                               
044                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        
????                                     blue                                     1234                                     blue@test.com                                                                
044                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        

SQL> update membert01
  2  set mem_pwd = '4321'
  3  where mem_id = 'orange'
  4  ;

1 row updated.

SQL> select * from membert01;

MEM_NAME                                 MEM_ID                                   MEM_PWD                                  MEM_EMAIL                                                                    
---------------------------------------- ---------------------------------------- ---------------------------------------- ----------------------------------------                                     
MEM_PHONE                                MEM_ADDR                                                                                                                                                       
---------------------------------------- ----------------------------------------                                                                                                                       
??????                                   orange                                   4321                                     orange@test.com                                                              
032                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        
????                                     red                                      1234                                     red@test.com                                                                 
044                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        
??????                                   yellow                                   1234                                     yellow@test.com                                                              
032                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        
??????                                   green                                    1234                                     green@test.com                                                               
044                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        
????                                     blue                                     1234                                     blue@test.com                                                                
044                                      ??????????                                                                                                                                                     
                                                                                                                                                                                                        

SQL> spool off
