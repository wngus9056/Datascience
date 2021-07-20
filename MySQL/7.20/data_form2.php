<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=euc-kr" />
    </head>
    
    <body>
        <h2>▶ 데이터수집</h2>
        <form name="mem_form" method="post" action="mysql_fetch_row.php">
        <input type="hidden" name="title" value="회원 가입 양식"> 
        <table border="1" width="640" cellspacing="1" cellpadding="4">
            <tr>
                <td align="right">* 일련번호 :</td>
                <td><input type="text" size="15" maxlength="12" name="num"></td>
            </tr>
            <tr>
                <td align="right">* 아이디 :</td>
                <td><input type="text" size="15" maxlength="12" name="id" value="guest"></td>
            </tr>
            <tr>
                <td align="right" > * 이름 :</td>
                <td><input type="text" size="15" maxlength="12" name="name"></td>
            </tr>
            <tr>
                <td align="right"> * 우편번호  :</td>
                <td><input type="text" size="15" maxlength="10" name="num_post"></td>
            </tr>

            <tr>
                <td align="right">주 소 :</td>
                <td><input type="text" size="50" name="address"></td>
            </tr>

            <tr>
                <td align="right">tel :</td>
                <td><input type="text" size="50" name="tel"></td>
            </tr>

            <tr>
                <td align="right">나이 :</td>
                <td><input type="text" size="15" name="age"></td>
            </tr>
        </table>
    <br>
        <table border="0" width="640">
            <tr><td align="center">
            <input type="submit" value="확인">
            <input type="reset" value="다시작성"></td>
            </tr>
        </table>
        </form>
    </body>
</html>
