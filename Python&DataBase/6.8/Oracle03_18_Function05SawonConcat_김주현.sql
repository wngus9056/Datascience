SQL> show user;
USER is "SCOTT"
SQL> select saname || ' 사원의 급여는' || to_char(sapay, '999,999,999') || ' 입니다.' 사원급여 from sawontable;

사원급여                                                                                                                                                                                                
----------------------------------------------------------------------------------------------------------                                                                                              
홍길동 사원의 급여는       5,000 입니다.                                                                                                                                                                
한국남 사원의 급여는       3,000 입니다.                                                                                                                                                                
이순신 사원의 급여는       3,500 입니다.                                                                                                                                                                
이순라 사원의 급여는       1,200 입니다.                                                                                                                                                                
놀기만 사원의 급여는       2,300 입니다.                                                                                                                                                                
뷰별나 사원의 급여는       1,600 입니다.                                                                                                                                                                
채시라 사원의 급여는       3,400 입니다.                                                                                                                                                                
이성계 사원의 급여는       2,803 입니다.                                                                                                                                                                
무궁화 사원의 급여는       3,000 입니다.                                                                                                                                                                
임꺽정 사원의 급여는       2,200 입니다.                                                                                                                                                                
깨똥이 사원의 급여는       4,500 입니다.                                                                                                                                                                
공부만 사원의 급여는       4,003 입니다.                                                                                                                                                                
채송화 사원의 급여는       1,703 입니다.                                                                                                                                                                
이미라 사원의 급여는       2,503 입니다.                                                                                                                                                                
공부해 사원의 급여는       1,303 입니다.                                                                                                                                                                
뷰명한 사원의 급여는       1,800 입니다.                                                                                                                                                                
무궁화 사원의 급여는       1,100 입니다.                                                                                                                                                                
최진실 사원의 급여는       2,000 입니다.                                                                                                                                                                
김유신 사원의 급여는         400 입니다.                                                                                                                                                                
강감찬 사원의 급여는       1,003 입니다.                                                                                                                                                                

20 rows selected.

SQL> spool off
