<html>
<body>
<center><h3> -> 구구단 표</h3></center>
<table border="1" width="600">
<tr bgcolor="#ccccc" align="center">
  <td>2단</td>
  <td>3단</td>
  <td>4단</td>
  <td>5단</td>
  <td>6단</td>
  <td>7단</td>
  <td>8단</td>
  <td>9단</td>
  </tr>
<?
for($a=1; $a<=9; $a++){
  echo "<tr align='center'>";
  for($b=2; $b<=9; $b++){
    $c = $a * $b;
    echo "<td>{$b}X{$a}=$c</td>";}
  echo "</tr>";}
?>"
</table>
</body>
</html>