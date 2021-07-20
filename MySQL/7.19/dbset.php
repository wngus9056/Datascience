<?
$connect=mysql_connect('localhost','kim','1234'); // 주석 처리
mysql_select_db('kim_db',$connect);   /* 주석 여러줄

ㅁㄴㅇㄹ
ㅁㅁㄴㅇ
*/

//echo " 합계 $tot, 국어 $kor, 영어 $eng, 수학 $math<br>";

$tot=$kor + $eng + $math;
$avg=$tot/3;
if ($avg >= 90){
    $grade="A";
}
else if ($avg >= 80){
    $grade="B";
}
else if ($avg >= 70){
    $grade="C";
}
else if ($avg >= 60){
    $grade="D";
}
else{
    $grade="F";
}

$sql="insert into itban values ($num, '$name', $kor, $eng, $math, $tot, $avg, '$grade')";
$result=mysql_query($sql);

if($result)
    echo "레코드 삽입완료!";
else
    echo "레코드 삽입 실패! 에러 확인 요망!";

mysql_close($connect);
?>