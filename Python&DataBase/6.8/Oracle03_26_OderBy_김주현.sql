SQL> show user;
USER is "SCOTT"
SQL> select sabun, saname
  2  from sawontable;

     SABUN SANAME                                                                                                                                                                                       
---------- --------------------                                                                                                                                                                         
         1 ȫ�浿                                                                                                                                                                                       
         2 �ѱ���                                                                                                                                                                                       
         3 �̼���                                                                                                                                                                                       
         5 �̼���                                                                                                                                                                                       
         7 ��⸸                                                                                                                                                                                       
        11 �亰��                                                                                                                                                                                       
        14 ä�ö�                                                                                                                                                                                       
        17 �̼���                                                                                                                                                                                       
        13 ����ȭ                                                                                                                                                                                       
        19 �Ӳ���                                                                                                                                                                                       
        20 ������                                                                                                                                                                                       
         6 ���θ�                                                                                                                                                                                       
         8 ä��ȭ                                                                                                                                                                                       
         4 �̶̹�                                                                                                                                                                                       
        10 ������                                                                                                                                                                                       
        12 �����                                                                                                                                                                                       
         9 ����ȭ                                                                                                                                                                                       
        15 ������                                                                                                                                                                                       
        16 ������                                                                                                                                                                                       
        18 ������                                                                                                                                                                                       

20 rows selected.

SQL> select sabun, saname
  2  from sawontable
  3  order by sabun;

     SABUN SANAME                                                                                                                                                                                       
---------- --------------------                                                                                                                                                                         
         1 ȫ�浿                                                                                                                                                                                       
         2 �ѱ���                                                                                                                                                                                       
         3 �̼���                                                                                                                                                                                       
         4 �̶̹�                                                                                                                                                                                       
         5 �̼���                                                                                                                                                                                       
         6 ���θ�                                                                                                                                                                                       
         7 ��⸸                                                                                                                                                                                       
         8 ä��ȭ                                                                                                                                                                                       
         9 ����ȭ                                                                                                                                                                                       
        10 ������                                                                                                                                                                                       
        11 �亰��                                                                                                                                                                                       
        12 �����                                                                                                                                                                                       
        13 ����ȭ                                                                                                                                                                                       
        14 ä�ö�                                                                                                                                                                                       
        15 ������                                                                                                                                                                                       
        16 ������                                                                                                                                                                                       
        17 �̼���                                                                                                                                                                                       
        18 ������                                                                                                                                                                                       
        19 �Ӳ���                                                                                                                                                                                       
        20 ������                                                                                                                                                                                       

20 rows selected.

SQL> 
SQL> select sabun, saname
  2  from sawontable
  3  order by sabun desc;

     SABUN SANAME                                                                                                                                                                                       
---------- --------------------                                                                                                                                                                         
        20 ������                                                                                                                                                                                       
        19 �Ӳ���                                                                                                                                                                                       
        18 ������                                                                                                                                                                                       
        17 �̼���                                                                                                                                                                                       
        16 ������                                                                                                                                                                                       
        15 ������                                                                                                                                                                                       
        14 ä�ö�                                                                                                                                                                                       
        13 ����ȭ                                                                                                                                                                                       
        12 �����                                                                                                                                                                                       
        11 �亰��                                                                                                                                                                                       
        10 ������                                                                                                                                                                                       
         9 ����ȭ                                                                                                                                                                                       
         8 ä��ȭ                                                                                                                                                                                       
         7 ��⸸                                                                                                                                                                                       
         6 ���θ�                                                                                                                                                                                       
         5 �̼���                                                                                                                                                                                       
         4 �̶̹�                                                                                                                                                                                       
         3 �̼���                                                                                                                                                                                       
         2 �ѱ���                                                                                                                                                                                       
         1 ȫ�浿                                                                                                                                                                                       

20 rows selected.

SQL> spool off
