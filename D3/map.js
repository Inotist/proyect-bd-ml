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
	.then(drawMap);

function drawMap(featureCollection) {
	const svg = d3.select('#chart')
		.append('svg');
	svg
		.attr('width', chartWidth)
		.attr('height', chartHeight);

	const geojson = L.geoJson(featureCollection).addTo(map);

	var layers = [];
	geojson.eachLayer(function (layer) {
		layers.push(layer);
		layer.options.opacity = opacity;
		layer.options.fillOpacity = fillOpacity;
		layer.options.color = defaultColor;

		layer.on('click', d => {
			drawChart(d.target, svg);
		});
	});

	setColor(layers);
	drawLegend();

	map.fitBounds(geojson.getBounds());
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

function drawChart(target, svg) {
	svg.selectAll("*").remove();

	const dataProp = getData(target.feature.properties.properties);
	const maxInput = d3.max(Object.values(dataProp[1]));

	const rect = svg
		.selectAll('rect')
		.data(dataProp[0])
		.enter()
		.append('rect');

	rect.attr('x', 0)
		.attr('y', (d, index) => index * (thickness + 1))
		.attr('width', scale)
		.attr('height', thickness);

	function scale(d) {
		const scaleNum = chartWidth / maxInput;
		return scaleNum * d.properties;
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
	return [data, properties];
}