<meta http-equiv="Content-Type" content="text/html; charset=euc-kr" />
<?
$connect = mysql_connect("localhost","kim","1234");
$dbconn = mysql_select_db("kim_db", $connect);
$sql = "create table stud_score ( ";
$sql .= "num int not null auto_increment, ";
$sql .= "name varchar(12), ";
$sql .= "sub1 int, ";
$sql .= "sub2 int, ";
$sql .= "sub3 int, ";
$sql .= "sub4 int, ";
$sql .= "sub5 int, ";
$sql .= "sum int, ";
$sql .= "avg float, "; 
$sql .= "primary key(num) )";

$result = mysql_query($sql, $connect);
if ($result)
echo "�����ͺ��̽� ���̺� 'stud_score'�� �����Ǿ����ϴ�!";
else
echo "�����ͺ��̽� ���̺� ���� ����!!!";

mysql_close();
?>