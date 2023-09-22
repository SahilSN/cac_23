// removes the outer html tags of a string -- EX: "<div> <p>text</p> </div>"" --> "<p>text</p>"
function removeOuterTags(string) {
    var frontGt = string.indexOf('>');
    reversedString = string.split("").reverse().join("");
    var backLt = string.length - (reversedString.indexOf('<') + 1);

    var newString = string.substring(frontGt + 1, backLt).trim();
    return newString;
}

// processses the plotly html string and isolates the div and script
function processGraph(graph) {
    var graphDec = he.decode(graph);

    console.log(graphDec);
    // removes the outer div tags
    var graphDecTrim = removeOuterTags(graphDec);

    // isolates the graph div using regex
    var graphDiv = graphDecTrim.match(/<div(.*)>(.*)<\/div>/g)[0];

    // isolates the graph script using regex, then removes the script tags
    var graphScript = graphDecTrim.match(/<script(.*)>(.*)<\/script>/g)[0];
    var graphScript = removeOuterTags(graphScript);

    return { "div": graphDiv, "script": graphScript };
}

// takes an inputted plotly html string and attaches the graph to a pre-existing DOM element specified by inputted id
function createGraph(graph, divId) {
    // isolates the graph and saves the div and script
    var pGraph = processGraph(graph);
    var graphDiv = pGraph["div"];
    var graphScript = pGraph["script"];

    // attaches the separate div and script to predefined html elements -- can also be changed to create new html elements instead
    document.getElementById(divId).innerHTML = graphDiv;
    const script = document.createElement('script');
    script.type = "text/javascript";
    script.text = graphScript;
    document.body.appendChild(script);
};