const map = L.map('map');

map.createPane('labels');

L.tileLayer('https://{s}.tile.openstreetmap.se/hydda/base/{z}/{x}/{y}.png', {
	attribution: 'Tiles courtesy of <a href="http://openstreetmap.se/" target="_blank">OpenStreetMap Sweden</a> &mdash; Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.tileLayer('https://{s}.basemaps.cartocdn.com/light_only_labels/{z}/{x}/{y}.png', {
    attribution: '©OpenStreetMap, ©CartoDB',
    pane: 'labels'
}).addTo(map);

d3.json('https://gist.githubusercontent.com/miguepiscy/2d431ec3bc101ef62ff8ddd0e476177f/raw/2482274db871e60195b7196c602700226bdd3a44/practica.json')
	.then(drawMap); // geoJson proporcionado por el profesor para realizar la práctica

/*d3.json('https://gist.githubusercontent.com/Inotist/a0b7f73d5e8b6eea4a880d605cc52647/raw/d73d2d16c4f04fa4f5e11a58dcfec31f6ca17e20/geoJsonAirbnbv2.json')
	.then(drawMap);*/ // geoJson generado a partir de los datos que tengo en mi cloud sql del dataset de aribnb.

function drawMap(featureCollection) {
	const chartSVG = createChartSVG()

	const geojson = L.geoJson(featureCollection).addTo(map);

	var layers = [];
	geojson.eachLayer(function (layer) {
		layers.push(layer);
		layer.options.opacity = opacity;
		layer.options.fillOpacity = fillOpacity;
		layer.options.color = defaultColor;

		layer.on('click', d => {
			drawChart(d.target, chartSVG);
		});
	});

	setColor(layers);
	drawLegend();

	map.fitBounds(geojson.getBounds());
}

function createChartSVG() {
	return d3.select("#chart").append("svg")
    	.attr("width", chartWidth + margin.left + margin.right)
    	.attr("height", chartHeight + margin.top + margin.bottom)
  		.append("g")
    	.attr("transform", `translate(${margin.left}, ${margin.top})`);
}

function drawChart(target, svg) {
	svg.selectAll("*").remove();
	const dataProp = getData(target.feature.properties.properties);
	const maxProperties = d3.max(Object.values(dataProp[1]));
	const maxBedrooms = d3.max(Object.keys(dataProp[1]));

	var x = d3.scaleLinear().range([0, chartWidth]);
	var y = d3.scaleBand().rangeRound([0, chartHeight]).paddingInner(0.1);

	var xAxis = d3.axisBottom(x)
    	.ticks(maxProperties);
	var yAxis = d3.axisLeft(y)
    	.ticks(maxBedrooms);
	
  	x.domain([0, d3.max(dataProp[0], d => d.properties)]);
  	y.domain(dataProp[0].map(d => d.bedrooms));

  	svg.append("g")
    	.attr("transform", `translate(0, ${chartHeight})`)
    	.call(xAxis);

    svg.append("text")             
      .attr("transform", `translate(${chartWidth / 2} ,${chartHeight + margin.top + 20})`)
      .style("text-anchor", "middle")
      .text("Properties");

  	svg.append("g")
    	.call(yAxis);

    svg.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 0 - margin.left)
      .attr("x", 0 - (chartHeight / 2))
      .attr("dy", "1em")
      .style("text-anchor", "middle")
      .text("Bedrooms");

  	svg.selectAll("bar")
    	.data(dataProp[0])
    	.enter()
    	.append("rect")
    	.style("fill", barColor)
    	.attr("y", d => y(d.bedrooms))
    	.attr("height", y.bandwidth())
    	.attr("width", d => x(d.properties));
}

function setColor(layers) {
	var prices = [];
	layers.forEach (layer => {
		prices.push(layer.feature.properties.avgprice);
	});
	const max = d3.max(prices);
	const min = d3.min(prices);
	const scale = ((max-min)/gradient.length)+outlier;

	layers.forEach (layer => {
		const price = layer.feature.properties.avgprice;

		var count = 1;
		gradient.forEach(color => {
			if ((price <= min+scale*count && layer.options.color == defaultColor) || (count == gradient.length && price >= min+scale*count)) {
				layer.options.color = color;
				return;
			};
			count += 1;
		});

		if (layer.options.color == defaultColor) {
			layer.options.opacity = defaultOpacity;
			layer.options.fillOpacity = defaultOpacity;
		};
	});
}

function drawLegend() {
  	const svg = d3.select('#legend')
		.append('svg');
	svg.attr('width', legendWidth)
		.attr('height', legendHeight);

	const color = d3.scaleOrdinal(gradient);
	const legend = svg.append('g').attr('class', 'legend')

	const scaleLegend = d3.scaleLinear()
		.domain([0, gradient.length])
		.range([0, legendWidth])

	for (let index=0; index < gradient.length; index += 1) {
		const posX = scaleLegend(index);

		const legendGroup = legend
			.append('g')
			.attr('transform', `translate(${posX}, 0)`);

		const rectColor = legendGroup.append('rect');
		const widthRect = (legendWidth / gradient.length) - legendSeparation;
		rectColor.attr('width', widthRect).attr('height', legendHeight).attr('fill', color(index));
	}
}

function getData(source) {
	var data = [];
	var properties = {};
	source.forEach (property => {
		if (properties.hasOwnProperty(property["bedrooms"])) {
			properties[property["bedrooms"]]++;
		} else if (property.hasOwnProperty("bedrooms")) {
			properties[property["bedrooms"]] = 1;
		}
	});
	Object.keys(properties).forEach (bedrooms => {
		data.push({
			'bedrooms': parseInt(bedrooms),
			'properties': properties[bedrooms]
		});
	});
	data.sort((a,b) => {
		return a.properties-b.properties
	})
	return [data, properties];
}