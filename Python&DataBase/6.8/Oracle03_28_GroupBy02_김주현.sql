SQL> show user;
USER is "SCOTT"
SQL> select deptno, count(saname) �����, avg(sapay) �޿����, max(sapay) �ְ�޿�, min(sapay) �����޿�, sum(sapay) �޿���
  2  from sawontable
  3  group by deptno;

    DEPTNO     �����   �޿����   �ְ�޿�   �����޿�     �޿���                                                                                                                                       
---------- ---------- ---------- ---------- ---------- ----------                                                                                                                                       
        30          7 1959.71429       4003        400      13718                                                                                                                                       
        20          7 2457.14286       3500       1200      17200                                                                                                                                       
        10          6       2900       5000       1100      17400                                                                                                                                       

SQL> spool off
