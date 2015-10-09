

jQuery("#webcam").webcam({

    width: 320,
    height: 240,
    mode: "callback",
    swffile: "static/jquery-webcam/jscam_canvas_only.swf", // canvas only doesn't implement a jpeg encoder, so the file is much smaller

    onTick: function(remain) {

        if (0 == remain) {
            jQuery("#status").text("Cheese!");
        } else {
            jQuery("#status").text(remain + " seconds remaining...");
        }
    },

    onSave: function(data) {

        var col = data.split(";");
    // Work with the picture. Picture-data is encoded as an array of arrays... Not really nice, though =/
    },

    onCapture: function () {
        webcam.save();


      // Show a flash for example
    },

    debug: function (type, string) {
        // Write debug information to console.log() or a div, ...
    },

    onLoad: function () {
    // Page load
        var cams = webcam.getCameraList();
        for(var i in cams) {
            jQuery("#cams").append("<li>" + cams[i] + "</li>");
        }

    }
});