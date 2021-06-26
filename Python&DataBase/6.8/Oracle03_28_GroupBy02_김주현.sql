SQL> show user;
USER is "SCOTT"
SQL> select deptno, count(saname) 사원수, avg(sapay) 급여평균, max(sapay) 최고급여, min(sapay) 최저급여, sum(sapay) 급여합
  2  from sawontable
  3  group by deptno;

    DEPTNO     사원수   급여평균   최고급여   최저급여     급여합                                                                                                                                       
---------- ---------- ---------- ---------- ---------- ----------                                                                                                                                       
        30          7 1959.71429       4003        400      13718                                                                                                                                       
        20          7 2457.14286       3500       1200      17200                                                                                                                                       
        10          6       2900       5000       1100      17400                                                                                                                                       

SQL> spool off
