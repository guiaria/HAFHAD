// ################################################################# //
// ######	           USER VARIABLE CHANGE HERE!!!		        #### //
// ################################################################# //
var debugPlugIP = '192.168.1.84';
var userID = 1;

// ################################################################# //
// ######	                 REQUIRE MODULE   				    #### //
// ################################################################# //
const { Client } = require('tplink-smarthome-api');
var firebaseController = require("./firebaseController.js");

var command;
var device1 = '';
var device2 = '';



// ################################################################# //
// ######	                     FUNCTION                       #### //
// ################################################################# //


///
///		FUNCTION set device open/close with input <IP>
///		return N/A
function setStatePlug ( state, deviceIP ) {

	const plug = plugClient.getDevice({host: deviceIP}).then((device)=>{
		device.setPowerState(state);
		firebaseController.updateDeviceStateFromMac( userID, device.mac, device.relayState );
	});

}


// ################################################################# //
// ######	                 START HERE						    #### //
// ################################################################# //

const plugClient = new Client();

process.argv.forEach(function(index) {
	//index = 'close,ห้องนอน,ห้องครัว';
	var words = index.split(',');

	if ( words.length > 1 ){

		/*  check command open/close */
		if( words[0] == 'open' )
			command = true;
		else if( words[0] == 'close' )
			command = false;
		else
			return 0;

		/*  let device1 = name1 */
 		device1 = words[1];

		/* let device2 = name2 if exist */
		if ( words.length == 3 ){
			device2 = words[2];
		}
	}
	else {
		return 0;
	}

});

var status1;
var status2;

if( device1 != '' ) {
	firebaseController.readDeviceDataFromAlias( userID, device1, function( deviceJson ) {

		//console.log( deviceJson );
		if( deviceJson )
			setStatePlug ( command, deviceJson.ip );
		else
			status1 = 0;
	} )
	
}

if( device2 != '' ) {

	firebaseController.readDeviceDataFromAlias( userID, device2, function( deviceJson ) {

		//console.log( deviceJson );
		if( deviceJson )
			setStatePlug ( command, deviceJson.ip );
		else
			status2 = 0
	} )
	
}

var returnToPython = ''

if( status1 == 0 ) {
	returnToPython += 'ไม่มี'+ device1;
}

if(device2 != '') {
	if( status1 == 0 && status2 == 0)
		returnToPython += ' และ ไม่มี'+ device2;
}
console.log( returnToPython );