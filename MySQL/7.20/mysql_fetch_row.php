<meta http-equiv="Content-Type" content="text/html; charset=euc-kr" />
<?
$connect = mysql_connect("localhost","kim","1234");
$db_con = mysql_select_db("kim_db", $connect);

$sql="insert into membership values ($num, '$name','$id', $num_post, '$address', '$tel', $age)";
$result=mysql_query($sql);
    
if ($result)
    echo "���ڵ� ���� �Ϸ�!";
else
    echo "���ڵ� ���� ����! ���� Ȯ�� ���";
 
$sql = "select * from membership where address like '%����%' order by age;";
$result = mysql_query($sql);

$fields=mysql_num_fields($result);

?>

<h2>�� mysql_fetch_row()�� �̿��� ������ �б�</h2>
<table width= "800" border="1" cellspacing="0" cellpadding="5">
<tr align="center">
<td bgcolor="#cccccc">�Ϸù�ȣ</td>
<td bgcolor="#cccccc">���̵�</td>
<td bgcolor="#cccccc">�̸�</td>
<td bgcolor="#cccccc">�����ȣ</td>
<td bgcolor="#cccccc">�ּ�</td>
<td bgcolor="#cccccc">��ȭ��ȣ</td>
<td bgcolor="#cccccc">����</td>
</tr>

<?
while ( $row = mysql_fetch_row($result)) 
{
echo "<tr>";

for ($i=0; $i < $fields; $i++)
{
echo "<td> $row[$i] </td>";
}

echo "</tr>";
}

mysql_close();
?>
</table>