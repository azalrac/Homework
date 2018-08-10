// from data.js
var tableData = data;

var table = d3.select("table");


function renderTable(tableData){
    table = d3.select("#table-area");
    var tbody = table.select("tbody");
    d3.select('tbody').html('')
    console.log(tableData);
    console.log(tableData.length);
    for(var i=0; i<tableData.length; i++){
        tr = tbody.append("tr");
        tr.append("td").text(tableData[i].datetime);
        tr.append("td").text(tableData[i].city);
        tr.append("td").text(tableData[i].state);
        tr.append("td").text(tableData[i].country);
        tr.append("td").text(tableData[i].shape);
        tr.append("td").text(tableData[i].durationMinutes);
        tr.append("td").text(tableData[i].comments);
    }

}

var filter = d3.select("#filter-btn");
filter.on("click", function() {
    d3.event.preventDefault();
    var datePicked = d3.select("#datetime").node().value;
    var finalData = [];
    if(datePicked){
        finalData =  dateChosen(datePicked);
    }
    renderTable(finalData);
});

function dateChosen(datePicked){
    console.log(datePicked);
    return tableData.filter(element => element.datetime === datePicked);
}
