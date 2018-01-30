var firebase = require("firebase");
//var database = firebase.database();

var config = {
  apiKey: "AIzaSyBIzv-xxZNIlPv73EK8vy5PnyeTWXlSa70",
  authDomain: "plugdatabase.firebaseapp.com",
  databaseURL: "https://plugdatabase.firebaseio.com",
  projectId: "plugdatabase",
  storageBucket: "plugdatabase.appspot.com",
};
firebase.initializeApp(config);

  function readPlug(uid, alias){

      var ref = firebase.database().ref('/user-plugs/' + uid).once("value", function(snapshot) {
        console.log(snapshot.val());
    
        // var mac = (snapshot.val() && snapshot.val().mac) || 'Anonymous';
        // var ip = (snapshot.val() && snapshot.val().ip) || 'Anonymous';
        // console.log('mac=' + mac + '  ip=' + ip);
      }, function (error) {
        console.log("Error: " + error.code);
      });
    
  }
  
  function writePlug(uid, mac, JSONdata) {
    firebase.database().ref('user-plugs/' + uid + '/' + mac).set(JSONdata);
  }
  
  function writeNewPlug(uid, mac, JSONdata) {
    return firebase.database().ref('user-plugs/' + uid + '/' + mac).update(JSONdata);
  }


var uid = 1;
var alias = 'ห้องนอน';
var data = {
  mac: "50:c7:bf:98:fb:d0",
  alias: alias,
  state: 0,
  ip: "10.0.0.245"
};
writePlug(uid, "50:c7:bf:98:fb:d0", data);