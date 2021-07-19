<?
$num = array($kor, $eng, $math);
$count=3;
echo "정렬되기 전 : ";
for($a=0; $a<10; $a++)
  echo $num[$a]." ";
echo "<br>";

for($i=$count-1; $i>=0; $i--){
  for($j=0; $j<=$i; $j++){
    if($num[$j]>$num[$j+1]){
      $tmp=$num[$j];
      $num[$j]=$num[$j+1];
      $num[$j+1]=$tmp;}}}
echo "오름차순 정렬(버블정렬) : ";
for($a=0;$a<10;$a++)
  echo $num[$a]." ";
?>