SQL> show user;
USER is "SCOTT"
SQL> select saname 사원이름, deptno 부서번호 from sawontable where deptno = 10 or deptno = 20;

사원이름               부서번호                                                                                                                                                                         
-------------------- ----------                                                                                                                                                                         
홍길동                       10                                                                                                                                                                         
한국남                       20                                                                                                                                                                         
이순신                       20                                                                                                                                                                         
이순라                       20                                                                                                                                                                         
놀기만                       20                                                                                                                                                                         
뷰별나                       20                                                                                                                                                                         
채시라                       20                                                                                                                                                                         
무궁화                       10                                                                                                                                                                         
임꺽정                       20                                                                                                                                                                         
깨똥이                       10                                                                                                                                                                         
뷰명한                       10                                                                                                                                                                         
무궁화                       10                                                                                                                                                                         
최진실                       10                                                                                                                                                                         

13 rows selected.

SQL> select saname 사원이름, deptno 부서번호, sajob 직위 from sawontable where deptno = 10 and sajob ='사원';

사원이름               부서번호 직위                                                                                                                                                                    
-------------------- ---------- --------------------                                                                                                                                                    
무궁화                       10 사원                                                                                                                                                                    
최진실                       10 사원                                                                                                                                                                    

SQL> select saname 사원이름, deptno 부서번호, sajob 직위 from sawontable where not deptno = 10;

사원이름               부서번호 직위                                                                                                                                                                    
-------------------- ---------- --------------------                                                                                                                                                    
한국남                       20 부장                                                                                                                                                                    
이순신                       20 과장                                                                                                                                                                    
이순라                       20 사원                                                                                                                                                                    
놀기만                       20 과장                                                                                                                                                                    
뷰별나                       20 과장                                                                                                                                                                    
채시라                       20 사원                                                                                                                                                                    
이성계                       30 부장                                                                                                                                                                    
임꺽정                       20 사원                                                                                                                                                                    
공부만                       30 과장                                                                                                                                                                    
채송화                       30 대리                                                                                                                                                                    
이미라                       30 대리                                                                                                                                                                    
공부해                       30 사원                                                                                                                                                                    
김유신                       30 사원                                                                                                                                                                    
강감찬                       30 사원                                                                                                                                                                    

14 rows selected.

SQL> spool off
