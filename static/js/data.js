var select = d3.select("select")
var data_tables = ["","Dens","1985-2016","2009-2016","Climate"]
data_tables.forEach( d =>{
    var opt = select.append("option");
    opt.property("value",d);
    opt.text(d);

});



select.on("change",runEnter)
var columns = []

function runEnter(){
    var dropdownMenu = d3.select("select");
        // Assign the value of the dropdown menu option to a variable
    var option = dropdownMenu.property("value");

    if (option === "Dens"){
        dens()
        columns = ['record','denid','spring_year','data_source','discovery_method','latitude','longitude','confirmation','substrate','position_method','horizontal_error']
    }
    else if (option === "1985-2016"){
        eightyfivesixteen()
        columns = ['BearID_rsf','DateTimeUTC_rsf','latitude_rsf','longitude_rsf','season','period','lc94_rsf','eaInterval_rsf']
    }
    else if (option === "2009-2016"){
        ninesixteen()
        columns = ['BearId','GmtDate','GmtTime','longitude','latitude','Raw_Act','Standard_act','Active_Den','Habitat']
    }
    else if(option === "Climate"){
        climate()
        columns = ['Year_Month','Land_Avg_Temp','Land_Max_Temp','Land_Min_Temp','Land_Ocean_Avg_Temp',
        'North_Min_Temp_Anomoly', 'North_Max_Temp_Anomoly','North_Mean_Temp_Anomoly']
    };
    
};

var theads =  d3.select('thead')
var tbody =  d3.select('tbody')

function createTables(data, columns){
    console.log(data.results)

    d3.selectAll("td").remove()
    d3.selectAll("tr").remove()
        

    var tr = theads.append("tr")
    columns.forEach(c =>{        
        var td=tr.append("td")
        td.text(c)
    });
    var results = data.results

    var rows = tbody.selectAll("tr").data(results).enter().append("tr");

    // create a cell in each row for each column
    var cells = rows
        .selectAll("td")
        .data(function (row) {
        return columns.map(function (column) {
            return { column: column, value: row[column] };
        });
        })
        .enter()
        .append("td")
        .text(function (d) {
        return d.value;
        });

}

function dens(){
    d3.json("/api/dens")
    .then((data) => {
        createTables(data,columns)
    });

};

function climate(){
    d3.json("/api/climate")
    .then((data)=>{
        createTables(data,columns)
    });

};

function ninesixteen(){
    d3.json('/api/bears_2009_2016')
    .then((data)=>{
        createTables(data,columns)
    });

};

function eightyfivesixteen(){
    d3.json('/api/bears_1985_2016')
    .then((data)=>{
        createTables(data,columns)
     
    });

};