SQL> show user;
USER is "SCOTT"

SQL> select deptno,
  2  decode(deptno, 10, '전산부', 20, '영업부', 30, '관리부', 40, '총무부', '확인 중') as 임시부서 from depttable;

    DEPTNO 임시부서                                                                                                                                                                                     
---------- --------------------                                                                                                                                                                         
        20 영업부                                                                                                                                                                                       
        30 관리부                                                                                                                                                                                       
        40 총무부                                                                                                                                                                                       
        10 전산부                                                                                                                                                                                       

SQL> spool off
