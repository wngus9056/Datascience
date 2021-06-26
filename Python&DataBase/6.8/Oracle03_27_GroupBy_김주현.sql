SQL> show user;
USER is "SCOTT"
SQL> select count(saname) 사원수, avg(sapay) 급여평균, max(sapay) 최고급여, min(sapay) 최저급여, sum(sapay) 급여합
  2  from sawontable;

    사원수   급여평균   최고급여   최저급여     급여합                                                                                                                                                  
---------- ---------- ---------- ---------- ----------                                                                                                                                                  
        20     2415.9       5000        400      48318                                                                                                                                                  

SQL> spool off
