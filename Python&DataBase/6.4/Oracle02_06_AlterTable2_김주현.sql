SQL> show user
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

SQL> alter table membert01
  2  rename column mem_addr to mem_address
  3  ;

Table altered.

SQL> desc membert01;
 Name                                                                                                              Null?    Type
 ----------------------------------------------------------------------------------------------------------------- -------- ----------------------------------------------------------------------------
 MEM_NAME                                                                                                                   VARCHAR2(20)
 MEM_ID                                                                                                                     VARCHAR2(20)
 MEM_PWD                                                                                                                    VARCHAR2(20)
 MEM_EMAIL                                                                                                                  VARCHAR2(20)
 MEM_PHONE                                                                                                                  VARCHAR2(20)
 MEM_ADDRESS                                                                                                                VARCHAR2(20)

SQL> spool off
