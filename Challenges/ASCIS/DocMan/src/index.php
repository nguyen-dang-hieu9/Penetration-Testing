<?php
	date_default_timezone_set('Asia/Ho_Chi_Minh');
	session_start();
	/*
		Rate limiter by Roger Stringer (@freekrai)
		https://gist.github.com/freekrai/cdcd6ebb29d84b9dc244282e64caf5fe
	*/
	include("ratelimiter.php");
	$rateLimiter = new RateLimiter($_SERVER["REMOTE_ADDR"]);
	$limit = 10;
	$minutes = 1;
	try {
		$rateLimiter->limitRequestsInMinutes($limit, $minutes);
	} catch (RateExceededException $e) {
		header("HTTP/1.1 429 Too Many Requests");
		die (json_encode([
			"err" => "Rate Limit Exceeded. ". sprintf("Please retry after %d seconds.", floor($minutes * 60)), 
			"givenName" => ""
		]));
	}
	/// end rate limiter
	///////////////////////////////////////////////////////////
	/*
		DocMan by the authors of ASCIS 2024.	
	*/
	require_once("router.php");
	require_once("action.php");
	$ret = Router::proc();
	echo $ret['action']($ret['parameters']);