var height = window.innerHeight;
var width = window.innerWidth;

if (width < 500){

   var bg = d3.select("smallscreenfont");
   bg.attr("font-size", `1.5rem`);
   console.log("Am I working")
}