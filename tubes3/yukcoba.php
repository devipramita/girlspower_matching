<!DOCTYPE html>
<html>
<head>
  <title>Spam Detector</title> <!-- Title -->
  <link rel="icon" href="winnie.jpg"> <!-- Favicon -->
   <link rel="stylesheet" href="style.css"> <!-- CSS -->
	<!-- Responsive -->
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link href="assets/css/bootstrap-responsive.css" rel="stylesheet">
</head>

<body>
<!-- title -->
<div class="title">
  My Spam Detection App
</div>
<?php
$key= $_POST['keyword'];
$type=$_POST['dropdown'];
require_once('TwitterAPIExchange.php');

/** Set access tokens here - see: https://dev.twitter.com/apps/ **/
$settings = array(
    'oauth_access_token' => "2343232429-9PjgW9HPOGuRAWSGrQ9DY12L6JdbHhUa4aeKqSx",
    'oauth_access_token_secret' => "BAiGojRpb7qDtyd2T1StiZNeyCxd8jG0JgM3CyaOO6B0g",
    'consumer_key' => "YYbxgecbUr76qxUMeNSS9MHWE",
    'consumer_secret' => "bH0aRJH1okVj9ctl4Q4iURNW8S0NlorGf6t3jSocNIGd1rMDcz"
);
 
$url = "https://api.twitter.com/1.1/statuses/home_timeline.json";
$requestMethod = "GET";
if (isset($_GET['user']))  {$user = $_GET['user'];}  else {$user  = "devipram";}
if (isset($_GET['count'])) {$count = $_GET['count'];} else {$count = 25;}
$getfield = "?screen_name=$user&count=$count";
$twitter = new TwitterAPIExchange($settings);
$string = json_decode($twitter->setGetfield($getfield)
		->buildOauth($url, $requestMethod)
		->performRequest(),$assoc = TRUE);
/*if($string["errors"][0]["message"] != "") {echo "<h3>Sorry, there was a problem.</h3><p>Twitter returned the following error message:</p><p><em>".$string["errors"][0]["message"]."</em></p>";exit();}*/
$temp = array();
foreach($string as $items)
{
    /*echo "Time and Date of Tweet: ".$items['created_at']."<br />";*/
    /*echo "Tweet: ". $items['text']."<br />";/*
    echo "Tweeted by: ". $items['user']['name']."<br />";
    echo "Screen name: ". $items['user']['screen_name']."<br />";
    echo "Followers: ". $items['user']['followers_count']."<br />";
    echo "Friends: ". $items['user']['friends_count']."<br />";
    echo "Listed: ". $items['user']['listed_count']."<br /><hr />";*/
    array_push($temp, $items['text']);
}
/*foreach ($temp as $print) {
	echo $print."<br/>";
}*/
$info = implode("$", $temp);
$info = str_replace("\n", " ", $info);
/*echo $info;*/
// Execute the python script with the JSON data
$command = escapeshellcmd('python loadJson.py ');
$result = shell_exec($command. escapeshellarg($info)." ".escapeshellarg($key)." ".escapeshellarg($type));
#echo $result;
$resultData = explode("SPLIT", $result);

/*<!-- twit -->*/
foreach($resultData as $items){
	echo "<p> $items </p>";
}
?>
<!-- about us -->
<center><a href="about_us.html">About Us</a></center>
<br>
</body>
</html>