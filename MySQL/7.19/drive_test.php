<?
$test1_cut = 70; //�ʱ� ���� ����
$test2_cut = 80; //�Ǳ� ���� ����
$test3_cut = 90; //�������� ���� ����

echo "�������� ���� �հ� ������<br>";
echo "�ʱ� ���� $test1_cut �� �̻�,<br>";
echo "�Ǳ� ���� $test2_cut �� �̻�,<br>";
echo "�������� ���� $test3_cut �� �̻�,<br>";
echo "ȹ���� �ʱ� ���� : $test1 ��, �Ǳ� ���� : $test2 ��, �������� ���� : $test3 ��<br><br>";

if (($test1 >= $test1_cut) && ($test2 >= $test2_cut) && ($test3 >= $test3_cut))
    echo "�հ��ϼ̽��ϴ�!!!";
else
    echo "���հ��Դϴ�!!!";
?>