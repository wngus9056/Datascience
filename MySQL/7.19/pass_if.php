<?
if($pilgi >= 70 && $silgi >= 80 )
{
    $result = "합격";
}
else{
    $result = "불합격";
}
echo "필기 점수 : $pilgi, 실기 점수 : $silgi<br>";
echo "결과 : $result";
?>