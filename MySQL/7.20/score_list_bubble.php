<?
$connect = mysql_connect("localhost", "kim", "1234");
mysql_select_db("kim_db", $connect);

if ($mode == "insert")
{
  $sum = $sub1 + $sub2 + $sub3 + $sub4 + $sub5;
  $avg = $sum/5;
  
  $sql = "insert into stud_score (name, sub1, sub2, sub3, sub4, sub5, sum, avg) values";
  $sql.= "('$name', $sub1, $sub2, $sub3, $sub4, $sub5, $sum, $avg)";
  $result = mysql_query($sql);
}
?>

<meta http-equiv="Content-Type" content="text/html; charset=euc-kr" />
<h3>1) 성적 입력 하기</h3>

<form action="score_list_bubble.php?mode=insert" method='post'>
<table width="850" border="1" cellpadding="5">
<tr><td> 이름 : <input type="text" size="6" name="name">&nbsp;
  과목1 : <input type="text" size="3" name="sub1">&nbsp;
  과목2 : <input type="text" size="3" name="sub2">&nbsp;
  과목3 : <input type="text" size="3" name="sub3">&nbsp;
  과목4 : <input type="text" size="3" name="sub4">&nbsp;
  과목5 : <input type="text" size="3" name="sub5">
  </td>
  <td align="center">
  <input type="submit" value="입력하기">
  </td>
</tr>
</table>
</form>

<p>
<h3>2) 성적 출력 하기</h3> 
<p><a href ="score_list_bubble.php?mode=big_first">[성적순 정렬]</a> 
<a href ="score_list_bubble.php?mode=small_first">[성적역순 정렬]</a></p>
<p>
<!-- 제목 표시 시작 -->
<table width="720" border="1" cellpadding="5">
<tr align="center" bgcolor="#eeeeee">
  <td>번호</td>
  <td>이름</td>
  <td>과목1</td>
  <td>과목2</td>
  <td>과목3</td>
  <td>과목4</td>
  <td>과목5</td>
  <td>합계</td>
  <td>평균</td>
  <td>순위</td>
  <td>&nbsp;</td>
</tr>

<!-- 제목 표시 끝 -->

<?
// select 명령 저장
if ($mode == "big_first") // 성적순 정렬(내림차순)
  $sql = "select * from stud_score order by sum desc";
else if ($mode == "small_first") // 성적순 정렬(오름차순)
  $sql = "select * from stud_score order by sum";
else 
  $sql = "select * from stud_score";
$result = mysql_query($sql); 
$count = 1; // 성적 출력하기의 번호
// 데이터베이스 데이터 출력 시작
while ($row = mysql_fetch_array($result))
{ 
  $avg = round($row[avg], 1);
  $num = $row[num];
  echo ("<tr align='center'>
    <td> $count </td>
    <td> $row[name] </td>
    <td> $row[sub1] </td>
    <td> $row[sub2] </td>
    <td> $row[sub3] </td>
    <td> $row[sub4] </td>
    <td> $row[sub5] </td>
    <td> $row[sum] </td>
    <td> $avg </td>
    <td> $count </td>
    <td> <a href='score_delete.php?num=$num'>[삭제]</a></td>
  </tr>");
  $count++;}
// 데이터베이스 데이터 출력 완료
mysql_close(); // 데이터베이스와의 접속 종료
?>
</table>