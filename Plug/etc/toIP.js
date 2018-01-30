const { spawn } = require('child_process');
const child = spawn('arp', ['-a']);

child.stdout.on('data', (chunk) => {
	var ssid;
	var data = `${chunk}`;
    var lines = data.split(/\r?\n/);
    lines.forEach(function(line){
        var elem = line.split(' ');
        if(elem.length > 3) {
            var mac = elem[3];
            var ip = elem[1];
            console.log('mac='+mac+'  ip='+ip);
        }
            
	});
	
});
