<?php

function dd($arr) {/*{{{*/
	$out=print_r($arr,1);
	echo $out;
}
/*}}}*/
$z=file_get_contents("cad.json");
$z=json_decode($z, 1);

array_walk_recursive($z,  function(&$v) {
	#if(is_numeric($v)) { 
		$v = $v * 0.01;
	#}
});

echo "Nie wiem kto wymyslil jawne klucze pieter 0, 1, 2... w aamksie, ale one sa bez sensu i json nie potrafi tego robic automatycznie.\n";
echo "W aamks.master json bedzie prostszy, a poki co klucze do pieter trzeba dodac recznie w wynikowym metres.cad.json.\n";
file_put_contents("metres.cad.json", json_encode($z));
echo "Zapisano metres.cad.json\n";
?>
