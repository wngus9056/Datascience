<?
$num = array($kor, $eng, $math);
$count=3;
echo "���ĵǱ� �� : ";
for($a=0; $a<10; $a++)
  echo $num[$a]." ";
echo "<br>";

for($i=$count-1; $i>=0; $i--){
  for($j=0; $j<=$i; $j++){
    if($num[$j]>$num[$j+1]){
      $tmp=$num[$j];
      $num[$j]=$num[$j+1];
      $num[$j+1]=$tmp;}}}
echo "�������� ����(��������) : ";
for($a=0;$a<10;$a++)
  echo $num[$a]." ";
?>