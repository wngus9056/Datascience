SQL> show user;
USER is "SCOTT"

SQL> select deptno,
  2  decode(deptno, 10, '�����', 20, '������', 30, '������', 40, '�ѹ���', 'Ȯ�� ��') as �ӽúμ� from depttable;

    DEPTNO �ӽúμ�                                                                                                                                                                                     
---------- --------------------                                                                                                                                                                         
        20 ������                                                                                                                                                                                       
        30 ������                                                                                                                                                                                       
        40 �ѹ���                                                                                                                                                                                       
        10 �����                                                                                                                                                                                       

SQL> spool off
