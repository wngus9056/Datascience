<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=euc-kr" />
    </head>
    
    <body>
        <h2>�� �����ͼ���</h2>
        <form name="mem_form" method="post" action="mysql_fetch_row.php">
        <input type="hidden" name="title" value="ȸ�� ���� ���"> 
        <table border="1" width="640" cellspacing="1" cellpadding="4">
            <tr>
                <td align="right">* �Ϸù�ȣ :</td>
                <td><input type="text" size="15" maxlength="12" name="num"></td>
            </tr>
            <tr>
                <td align="right">* ���̵� :</td>
                <td><input type="text" size="15" maxlength="12" name="id" value="guest"></td>
            </tr>
            <tr>
                <td align="right" > * �̸� :</td>
                <td><input type="text" size="15" maxlength="12" name="name"></td>
            </tr>
            <tr>
                <td align="right"> * �����ȣ  :</td>
                <td><input type="text" size="15" maxlength="10" name="num_post"></td>
            </tr>

            <tr>
                <td align="right">�� �� :</td>
                <td><input type="text" size="50" name="address"></td>
            </tr>

            <tr>
                <td align="right">tel :</td>
                <td><input type="text" size="50" name="tel"></td>
            </tr>

            <tr>
                <td align="right">���� :</td>
                <td><input type="text" size="15" name="age"></td>
            </tr>
        </table>
    <br>
        <table border="0" width="640">
            <tr><td align="center">
            <input type="submit" value="Ȯ��">
            <input type="reset" value="�ٽ��ۼ�"></td>
            </tr>
        </table>
        </form>
    </body>
</html>
