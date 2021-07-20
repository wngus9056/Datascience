<?
$connect =mysql_connect("localhost","kim","1234");
mysql_select_db("kim_db",$connect);

$tot = $kor + $eng + $math;
$avg = $tot/3;

$sql ="insert into sungjuk values ($kor,$eng,$math,$tot,$avg)";
$result = mysql_query($sql);
if($result)
   echo "레코드 삽입완료!";
else
   echo "레코드 삽입 실패! 에러확인요망!";
mysql_close($connect);
?>