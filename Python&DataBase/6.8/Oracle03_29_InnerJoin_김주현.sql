SQL> show user;
USER is "SCOTT"
SQL> select sabun �����ȣ, saname �����, goname ����, gotel ����ȭ
  2  from sawontable, gogektable
  3  where sabun = godam;

  �����ȣ �����               ����               ����ȭ                                                                                                                                           
---------- -------------------- -------------------- ----------------------------------------                                                                                                           
         2 �ѱ���               ����                 1343-1455                                                                                                                                          
         3 �̼���               ���                 123-1674                                                                                                                                           
         7 ��⸸               ����                 176-7677                                                                                                                                           
        13 ����ȭ               ȫ��                 767-1234                                                                                                                                           
         4 �̶̹�               �ȳ�                 767-1677                                                                                                                                           
         4 �̶̹�               ö��                 673-1674                                                                                                                                           
         9 ����ȭ               �赹                 673-6774                                                                                                                                           

7 rows selected.

SQL> spool off
