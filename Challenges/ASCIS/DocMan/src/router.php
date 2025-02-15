<?php
    require_once("routes.inc");
       
    class Router {
        public static function proc() {
        	global $routes;
        	
			$ret = array();
	
			$ret["action"]  = "fallback";	
			$ret["parameters"]  = array();
			
			$requestURI = explode('/', strtolower($_SERVER['REQUEST_URI']));
			$scriptName = explode('/', strtolower($_SERVER['SCRIPT_NAME']));
			$commandArray = array_diff_assoc($requestURI, $scriptName);
			$commandArray = array_values($commandArray);
			
			$c = count($commandArray);
			
			foreach ($routes as $v) {
				if (strtoupper($v[0]) == $_SERVER["REQUEST_METHOD"]) {
					$uri = explode('/', strtolower($v[1]));
					array_shift($uri);
					if (count($uri) == $c) {
						$i = 0;
						$p = array();
						for (; $i < $c; $i++) {
							if ($commandArray[$i] == $uri[$i]) {
							} else if (preg_match('/^{.*}$/', $uri[$i])) {
								$p[] = $commandArray[$i];
							} else { 
								break;
							}
						}
						if ($i == $c) {
							$ret["action"]  = $v[2];
							$ret["parameters"]  = $p;		
							break;
						}
					}
				}
			}		
			return $ret;
        }
    }