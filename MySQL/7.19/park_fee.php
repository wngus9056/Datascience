<?
if ($age < 3) // ����� ����
    $fee = "����";
elseif (($age >= 3 && $age <= 13) || ($after_1710 == "yes")) 
    $fee = "4,000��";
elseif (($age >= 14 && $age <= 18) || ($age >= 70) || ($welfare == "yes") || ($youkong == "yes")) 
    $fee = "8,000�� ";
else
    $fee = "10,000��";
echo "����ī�� ���� : $welfare<br>";
echo "������������ ���� : $youkong<br>"; 
echo "17�� 10�� ���� ���� : $after_1710<br>";
echo "���� : $age ��<br><br>";
echo "����� : $fee"; 
?>