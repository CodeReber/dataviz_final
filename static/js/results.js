var tempRange = d3.select("#tempRange");
var oceanRange = d3.select("#oceanRange");
var co2Range = d3.select("#co2Range");
var iceRange = d3.select("#iceRange");
var tempspan =  d3.select("#tempspan");
var oceanspan=d3.select("#oceanspan");
var co2span= d3.select("#co2span");
var icespan=d3.select("#icespan");


tempRange.on("change", ()=>{
    tempspan.text(Math.round(parseFloat(tempRange.property('value'))*19+1)) 
});

oceanRange.on("change", ()=>{
    oceanspan.text(Math.round((parseFloat(oceanRange.property('value'))*200+300))) 
});
co2Range.on("change", ()=>{
    co2span.text(Math.round(parseFloat(co2Range.property('value'))*19+1)) 
});
iceRange.on("change", ()=>{
    icespan.text(Math.round(parseFloat(iceRange.property('value'))*19+1)) 
});

$(function () { objectFitImages() });

