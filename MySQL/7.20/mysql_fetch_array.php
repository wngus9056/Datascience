<?
 $connect = mysql_connect("localhost","kim","1234");
 $db_con = mysql_select_db("kim_db", $connect);
 
 $sql = "select * from membership;";
 $result = mysql_query($sql, $connect);
 
 $number = 1;
?>
 <h2>�� mysql_fetch_array()�� �̿��� ������ �б�</h2>
 <table width= "800" border="1" cellpadding="10">
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
 while ( $row = mysql_fetch_array($result)) 
 {
 echo "
 <tr>
 <td> $number </td>
 <td> $row[id] </td>
 <td> $row[name] </td>
 <td> $row[num_post] </td>
 <td> $row[address] </td>
 <td> $row[tel] </td>
 <td> $row[age] </td>
 </tr>
 ";
 $number++;
}
 
 mysql_close();
?>
 </table>