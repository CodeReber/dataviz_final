
Skip to content
Pulls
Issues
Marketplace
Explore
@lilstarhunter
Learn Git and GitHub without any code!

Using the Hello World guide, you’ll start a branch, write comments, and open a pull request.
CodeReber /
dataviz_final

1
1

    0

Code
Issues
Pull requests 1
Actions
Projects
Wiki
Security

More
dataviz_final/static/js/slider.js /
Lauren Stein updte
Latest commit 455fbd8 3 minutes ago
History
0 contributors
20 lines (16 sloc) 870 Bytes
var temp_slider = document.getElementById("tempRange");
var temp_output = document.getElementById("temp");
output.innerHTML = slider.value; // Display the default slider value

// var ocean_slider = document.getElementById("oceanRange");
// var ocean_output = document.getElementById("ocean");
// output.innerHTML = slider.value; // Display the default slider value

// var co2_slider = document.getElementById("co2Range");
// var co2_output = document.getElementById("co2");
// output.innerHTML = slider.value; // Display the default slider value

// var ice_slider = document.getElementById("iceRange");
// var ice_output = document.getElementById("ice");
// output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
  output.innerHTML = this.value;
} 


