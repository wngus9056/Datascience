<?
$now_year=2021;
$now_month=7;
$now_day=19;
if($month < $now_month) 
    $age= $now_year - $year;
else 
    if($month == $now_month){ 
        if($day <= $now_day)
            $age= $now_year - $year;
        else
            $age= $now_year - $year-1;}
    else
        $age= $now_year - $year-1;

echo "���� ��¥ : $now_year �� $now_month �� $now_day ��<br>";
echo "��� ������ : $year �� $month �� $day �ϻ�<br>";
echo "�� ���� : $age ��";
?>