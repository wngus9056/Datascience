SQL> desc membert01;
 Name                                                                                                              Null?    Type
 ----------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------
 MEM_NAME                                                                                                                   VARCHAR2(20)
 MEM_ID                                                                                                                     VARCHAR2(20)
 MEM_PWD                                                                                                                    VARCHAR2(20)
 MEM_EMAIL                                                                                                                  VARCHAR2(20)
 MEM_PHONE                                                                                                                  VARCHAR2(20)
 MEM_ADDRESS                                                                                                                VARCHAR2(20)

SQL> column mem_name format a15;
SQL> column mem_id format a15;
SQL> column mem_pwd format a15;
SQL> column mem_email format a15;
SQL> column mem_phone format a15;
SQL> column mem_address format a15;
SQL> select * from membert01;

MEM_NAME        MEM_ID          MEM_PWD         MEM_EMAIL       MEM_PHONE       MEM_ADDRESS                                                                                                             
--------------- --------------- --------------- --------------- --------------- ---------------                                                                                                         
������          orange          4321            orange@test.com 032             ��ɴ��б�                                                                                                              
���            red             1234            red@test.com    044             ȫ�ʹ��б�                                                                                                              
������          yellow          1234            yellow@test.com 032             ��ɴ��б�                                                                                                              
�ҳ���          green           1234            green@test.com  044             ȫ�ʹ��б�                                                                                                              
�ٴ�            blue            1234            blue@test.com   044             ȫ�ʹ��б�                                                                                                              

SQL> spool off
