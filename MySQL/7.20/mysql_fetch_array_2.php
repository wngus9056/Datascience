<meta http-equiv="Content-Type" content="text/html; charset=euc-kr" />
<?
    $connect = mysql_connect("localhost","kim","1234");
    $db_con = mysql_select_db("kim_db", $connect);
    
    $sql="insert into membership values ($num, '$name','$id', $num_post, '$address', '$tel', $age)";
    $result=mysql_query($sql);
    
    if ($result)
        echo "레코드 삽입 완료!";
    else
        echo "레코드 삽입 실패! 에러 확인 요망";

    $sql = "select * from membership;";
    $result = mysql_query($sql, $connect);
    
?>
    <h2>▶ mysql_fetch_array()를 이용한 데이터 읽기</h2>
    <table width= "800" border="1" cellpadding="10">
        <tr align="center">
            <td bgcolor="#cccccc">일련번호</td>
            <td bgcolor="#cccccc">아이디</td>
            <td bgcolor="#cccccc">이름</td>
            <td bgcolor="#cccccc">우편번호</td>
            <td bgcolor="#cccccc">주소</td>
            <td bgcolor="#cccccc">전화번호</td>
            <td bgcolor="#cccccc">나이</td>
        </tr>
<?
    while ($row = mysql_fetch_array($result)) 
    {
        echo ("
        <tr>
        <td>  $row[num] </td>
        <td> $row[id] </td>
        <td> $row[name] </td>
        <td> $row[num_post] </td>
        <td> $row[address] </td>
        <td> $row[tel] </td>
        <td> $row[age] </td>
        </tr>
        ");
    }
    
mysql_close();    
?>
    </table>
