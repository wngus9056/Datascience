SQL> show user
USER is "SCOTT"
SQL> select mem_addr from membert01;

MEM_ADDR                                                                                                                                                                                                
----------------------------------------                                                                                                                                                                
재능대학교                                                                                                                                                                                              
홍익대학교                                                                                                                                                                                              
재능대학교                                                                                                                                                                                              
홍익대학교                                                                                                                                                                                              
홍익대학교                                                                                                                                                                                              

SQL> select distinct mem_addr from membert01;

MEM_ADDR                                                                                                                                                                                                
----------------------------------------                                                                                                                                                                
재능대학교                                                                                                                                                                                              
홍익대학교                                                                                                                                                                                              

SQL> spool off
