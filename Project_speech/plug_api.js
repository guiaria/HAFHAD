const Hs100Api = require('/usr/local/lib/node_modules/hs100-api'); 
const client = new Hs100Api.Client();
const plug = client.getDevice({host: '192.168.1.7'}).then((device)=>{
  device.getSysInfo().then(console.log);
  device.setPowerState(true);
});


