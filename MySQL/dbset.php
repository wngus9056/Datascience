<?
$connect=mysql_connect('localhost','kim','1234'); // �ּ� ó��
mysql_select_db('kim_db',$connect);   /* �ּ� ������

��������
��������
*/

//echo " �հ� $tot, ���� $kor, ���� $eng, ���� $math<br>";

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
    echo "���ڵ� ���ԿϷ�!";
else
    echo "���ڵ� ���� ����! ���� Ȯ�� ���!";

mysql_close($connect);
?>