SQL> show user;
USER is "SCOTT"
SQL> select count(saname) �����, avg(sapay) �޿����, max(sapay) �ְ�޿�, min(sapay) �����޿�, sum(sapay) �޿���
  2  from sawontable;

    �����   �޿����   �ְ�޿�   �����޿�     �޿���                                                                                                                                                  
---------- ---------- ---------- ---------- ----------                                                                                                                                                  
        20     2415.9       5000        400      48318                                                                                                                                                  

SQL> spool off
