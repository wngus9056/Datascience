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

echo "오늘 날짜 : $now_year 년 $now_month 월 $now_day 일<br>";
echo "출생 연월일 : $year 년 $month 월 $day 일생<br>";
echo "만 나이 : $age 세";
?>