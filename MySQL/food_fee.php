<?
/* 초등학교 급식비를 계산하는 프로그램
1학년 : 3만원
2학년 : 3만 5천원
3학년 : 4만원
4학년 : 4만 5천원
5학년 : 5만원
6학년 : 5만 5천원
*/
 
switch ($a){
    case 1 :
        echo "$a 학년 급식비 : 3만원";
        break;
    case 2 :
        echo "$a 학년 급식비 : 3만 5천원";
        break;
    case 3 :
        echo "$a 학년 급식비 : 4만원";
        break;
    case 4 :
        echo "$a 학년 급식비 : 4만 5천원";
        break;
    case 5 :
        echo "$a 학년 급식비 : 5만원";
        break;
    case 6 :
        echo "$a 학년 급식비 : 5만 5천원";
        break;
    default :
        echo "학년을 잘못 입력했어요!!!";
        break;}
?>