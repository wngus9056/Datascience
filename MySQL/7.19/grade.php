<?
if ($score>=95) 
    $grade = "A+";
elseif ($score>=90)
    $grade = "A";
elseif ($score>=85)
    $grade = "B+";
elseif ($score>=80)
    $grade = "B";
elseif ($score>=75)
    $grade = "C+";
elseif ($score>=70)
    $grade = "C";
elseif ($score>=65)
    $grade = "D+";
elseif ($score>=60)
    $grade = "D";
else 
    $grade = "F";
echo "�Էµ� ���� : $score ��<br> ��� : $grade";
?>