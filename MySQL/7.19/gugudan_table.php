<html>
<body>
<center><h3> -> ������ ǥ</h3></center>
<table border="1" width="600">
<tr bgcolor="#ccccc" align="center">
  <td>2��</td>
  <td>3��</td>
  <td>4��</td>
  <td>5��</td>
  <td>6��</td>
  <td>7��</td>
  <td>8��</td>
  <td>9��</td>
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