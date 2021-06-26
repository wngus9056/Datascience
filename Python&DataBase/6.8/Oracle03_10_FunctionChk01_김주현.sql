SQL> show user;
USER is "SCOTT"
SQL> select abs(-10) as "absChk01", abs(10) as "absChk02" from dual;

  absChk01   absChk02                                                                                                                                                                                   
---------- ----------                                                                                                                                                                                   
        10         10                                                                                                                                                                                   

SQL> select ceil(3.7) as "ceilChk01", ceil(3.3) as "ceilChk02" from dual;

 ceilChk01  ceilChk02                                                                                                                                                                                   
---------- ----------                                                                                                                                                                                   
         4         4                                                                                                                                                                                   

SQL> select floor(3.7) as "floorChk01", floor(3.3) as "floorChk02" from dual;

floorChk01 floorChk02                                                                                                                                                                                   
---------- ----------                                                                                                                                                                                   
         3         3                                                                                                                                                                                   

SQL> select round(3.7) as "roundChk01", round(3.3) as "roundChk02" from dual;

roundChk01 roundChk02                                                                                                                                                                                   
---------- ----------                                                                                                                                                                                   
         4         3                                                                                                                                                                                   

SQL> spool off
