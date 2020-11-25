var tempRange = d3.select("#tempRange");
var oceanRange = d3.select("#oceanRange");
var co2Range = d3.select("#co2Range");
var iceRange = d3.select("#iceRange");
var tempspan =  d3.select("#tempspan");
var oceanspan=d3.select("#oceanspan");
var co2span= d3.select("#co2span");
var icespan=d3.select("#icespan");


tempRange.on("change", ()=>{
    tempspan.text(tempRange.property('value')) 
});

oceanRange.on("change", ()=>{
    oceanspan.text(oceanRange.property('value')) 
});
co2Range.on("change", ()=>{
    co2span.text(co2Range.property('value')) 
});
iceRange.on("change", ()=>{
    icespan.text(iceRange.property('value')) 
});



