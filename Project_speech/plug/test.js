
var roomSSID 	= 'CAGD R_Lab';
var roomPass 	= 'rabbit999';
var myALIAS     = 'ห้องนอน';

var firebaseController = require("./firebaseController.js");
var plugSetting = require("./connectPlug.js")

plugSetting.settingDevice( roomSSID, roomPass, myALIAS, function( status ){
    console.log('status:' + status);
});

//firebaseController.updateDeviceStateFromMac( 1, '50:c7:bf:98:fb:d5', true)
//firebaseController.writeDeviceData( 1, 'ห้องครัว', '50:c7:bf:98:fb:d5', '192.168.1.85', 'false' );
//  firebaseController.readDeviceDataFromAlias( 1, 'ห้องนอน1', function( result ) {
//      console.log( result );
//  });