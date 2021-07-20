<?
if($num1 > $num2){
    if(num1 > $num3){
        $max1 = $a;
        if($num2 > $num3){
            $max2 = $num2;
            $max3 = $num3;}
        else{
            $max2 = $num3;
            $max3 = $num2;}}
    else{
        $max1 = $num3;
        $max2 = $num1;
        $max3 = $num2;}}
else{
    if($num1 > $num3){
        $max1 = $num2;
        $max2 = $num1;
        $max3 = $num3;}
    else{
        if($num2 > $num3){
            $max1 = $num2;
            $max2 = $num3;
            $max3 = $num1;}
        else{
            $max1 = $num3;
            $max2 = $num2;
            $max3 = $num1;}}}
    echo "입력된 세 정수 : $num1 $num2 $num3<br>";
    echo "입력된 정수를 큰 순서대로 배열 : $max1 $max2 $max3<br>";
?>