<html>
<body>
<h3>�� �Խ��� ��Ϻ���</h3>
<table border='1' width='600'>
<tr bgcolor='#ccccc' align='center'><td>��ȣ</td><td>����</td><td>�۾���</td><td>��¥</td></tr>
<?
$num = 1;
$name = "ȫ�浿";
$date = "2013/03/10";
 
for($i=1; $i<=10; $i++){
    $title = "�Խ��� ���� ".$num;
    echo ("<tr><td width='50' align='center'>$num</td><td>$title</td><td width='50'>$name</td><td width='80'>$date</td></tr>");
    $num++;}
?>
</table>
</body>
</html>