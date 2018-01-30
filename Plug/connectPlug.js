
function findIPfromMAC (plugMAClo, callback) {

	const { exec } = require('child_process');
	var plugIP;

	console.log('Find Plug IP...');

	exec("nmap -sP 192.168.1.0/24 >/dev/null && arp -an | grep "+plugMAClo+" | awk '{print $2}' | sed 's/[()]//g'", (err, stdout, stderr) => {
		if (err) {
			console.log('IP NOT FOUND!');
		}
		else{
			plugIP = stdout;
			callback(plugIP);
		}
	});
}

function connectToWiFi(piWifi,mySSID, myPass)
{
	piWifi.connect(mySSID, myPass, function(err) 
	{
		if (!err) { //Network created correctly
			console.log('Connect to WIFI...');
			setTimeout(function () {
				piWifi.check(mySSID, function (err, status) 
				{
					if (!err && status.connected) 
					{

					} else 
					{

					}
				});
			}, 3000);
		} 
		else 
		{

		}
	});
}

function connectPlug(){

	const TIMEOUT = 6000;

	const { Client } 	= require('tplink-smarthome-api');
	const client 			= new Client();
	const { spawn } 	= require('child_process');
	const { exec } 		= require('child_process');
	const piWifi 			= require('pi-wifi');

	var mySSID 	= 'Powerpuff';
	var myPass 	= 'cpe28kmutt';
	var myALIAS = 'ห้องนอน';

	var plugINFO;
	var plugMAC;
	var plugMAClo;
	var plugIP;
	
	const iwlist = spawn('iwlist', ['wlan0','scan']);					// CMD for command 'iwlist wlan0 scan'
	iwlist.stdout.on('data', (chunk) => {
		var plugSSID = '';
		var ssid;
		var data = `${chunk}`;
		var lines = data.split(/\r?\n/);
		var status = 0;

		lines.forEach(function(line)
		{
			if(line.includes('ESSID:')){
				ssid = line.replace('ESSID:"','');
				ssid = ssid.replace('"','');
				ssid = ssid.trim();

				if(ssid.includes('TP-LINK'))
				{
					plugSSID = ssid;
					console.log(plugSSID);

				
						setTimeout(function () {
							piWifi.connectOpen(plugSSID,  function(err)
							{
								if (!err) {
									console.log('Connect to PLUG...');
									setTimeout(function () {
										piWifi.check(plugSSID, function (err, status)
										{
											if (!err && status.connected)
											{
												console.log('SUCCESS');
												status = 1;
												setTimeout(function () {
													console.log('status:'+status);
													if(status == 1) 
													{
														client.getDevice({host: '192.168.0.1'}).then((tempD) => {		// CONNECT PLUG
															
															plugINFO = tempD.sysInfo;
															plugMAC = tempD.mac;
															plugMAClo = plugMAC.toLowerCase();
															console.log(plugINFO);
															tempD.setPowerState(true);

															tempD.send({"netif":{"set_stainfo":{"ssid":mySSID, "password":myPass, "key_type":3} } });	// SET PLUG TO CONNECT WIFI

															setTimeout(function () {
																	if (err) {
																		return console.error(err.message);
																	}
																	piWifi.connect(mySSID, myPass, function(err) 
																	{
																		if (!err) { //Network created correctly
																			console.log('Connect to WIFI...');
																			setTimeout(function () {
																				piWifi.check(mySSID, function (err, status) 
																				{
																					if (!err && status.connected) 
																					{

																						setTimeout(function () {

																							findIPfromMAC(plugMAClo, function(plugIP) {
																								if(plugIP != '') {

																									console.log('FOUND IP ' + plugIP);											// GET PLUG IP FROM MAC.
																												
																									var n = 'Cool Plug';
																									console.log('Connect to Plug...');
																									const plug = client.getDevice({host: plugIP}).then((device)=>{
                                                  	device.setPowerState(false);
																										console.log('Current Plug name: ' + device.name);
																										console.log('Change to: ' + n);
																										device.setAlias(n).then(function(){
                                                    	console.log('Current Plug name: ' + device.name);
                                                      	device.getSysInfo().then(console.log);
																										    
																										});
																										
																									});
																								}
																							});
																						},2000);
																					}
																				});
																			}, 6000);	// TIMEOUT - connect back to wifi

																		} 
																	});

															}, 6000);
					
														});

													}
												}, 10000);
											} 
											else
											{
												console.log('FAIL');
												connectToWiFi(piWifi, mySSID, myPass);
											}	
										});
									}, 6000);
								} 
								else
								{
									console.log('Unable to create the network ' + plugSSID + '.');
									connectToWiFi(piWifi, mySSID, myPass);
								}

							});
						}, 1000);
				
				}
				else
				{

				}
			}
		});
		
	});

	iwlist.on('close', (code) => {
		
	});
	
}

connectPlug();
