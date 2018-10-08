// from data.js
var tableData = data;

// YOUR CODE HERE!
var tbody = d3.select("tbody");

// Step 5: Use d3 to update each cell's text with
// UFO report values (datetime, city, state, country, shape, durationMinutes, comments)


tableData.forEach(function(UFOreport) {
  //console.log(UFOreport);
  var row = tbody.append("tr");
  Object.entries(UFOreport).forEach(function([key, value]) {
    //console.log(key, value);
    // Append a cell to the row for each value
    // in the UFO report object
    var cell = tbody.append("td");
    cell.text(value);
  });
});

var submit = d3.select("#filter-btn");

submit.on("click", function() {
    tbody.empty();                //How to make it update the page correctly?
    //d3.event.preventDefault();
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");

    // Get the value property of the input element
    var inputValue = inputElement.property("value");

    console.log(inputValue);

    var filteredData = tableData.filter(info => info.datetime === inputValue);

    filteredData.forEach(function(UFOreport) {

        
        //console.log(UFOreport);
        var row = tbody.append("tr");
        Object.entries(UFOreport).forEach(function([key, value]) {
          //console.log(key, value);
          // Append a cell to the row for each value
          // in the UFO report object
          var cell = tbody.append("td");
          cell.text(value);
        });
      });
    console.log(filteredData);
    d3.event.preventDefault();
});


