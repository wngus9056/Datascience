<?
 echo "<html> 
  <body>
  <h3>$a �� ������ǥ �����</h3>
  <table border='1' width='100'>";
 $b=1; 
 while ($b<=9){
  $c = $a * $b;
  echo "<tr><td align='center'>$a x $b = $c</td></tr>"; 
  $b++;}
 echo "</table>
 </body>
 </html>";
?>