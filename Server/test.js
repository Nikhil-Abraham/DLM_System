// read Simulate.json file and print

var fs = require("fs");
var path = require("path");

var filePath = path.join(__dirname, "Simulation.json");

fs.readFile(filePath, "utf8", function (err, data) {
	if (err) {
		console.log(err);
	} else {
		const x = JSON.parse(data);
        console.log(x.length);
	}
});
