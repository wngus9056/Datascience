<?
 $connect = mysql_connect("localhost","kim","1234");
 mysql_select_db("kim_db", $connect);
 
 // 필드 num이 $num값을 가지는 레코드 삭제
 $sql = "delete from stud_score where num = $num"; 
 mysql_query($sql, $connect);
 
 mysql_close($connect);
 
 // score_list.php로 돌아감
 Header("Location:score_list.php"); 
 ?>