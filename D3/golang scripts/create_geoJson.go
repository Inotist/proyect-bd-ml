package main

import (
	"database/sql"
	_ "github.com/lib/pq"
	"postgres"
	"fmt"
	"strings"
	"encoding/json"
	"os"
)

type dynamic map[string]interface{}

func appendRow(geoJson dynamic, neightbourhood string, latitude, longitude float64, bedrooms, price int64, cartodb_id int) ([]dynamic, int) {
	if neightbourhood != "" && latitude != 0 && longitude != 0 && bedrooms != 0 && price != 0 {
		neightbourhood = strings.ToLower(neightbourhood)

		for _, feature := range geoJson["features"].([]dynamic) {
			if feature["properties"].(dynamic)["name"] == neightbourhood {
				feature["properties"].(dynamic)["properties"] = append(feature["properties"].(dynamic)["properties"].([]dynamic), dynamic{
					"bedrooms": bedrooms,
					"price": price})

				newLen := len(feature["properties"].(dynamic)["properties"].([]dynamic))
				lonlat := make([][2]float64, newLen)
				for ix, coord := range feature["geometry"].(dynamic)["coordinates"].([][2]float64) {
					lonlat[ix] = coord
				}
				lonlat[newLen-1][0] = longitude
				lonlat[newLen-1][1] = latitude
				feature["geometry"].(dynamic)["coordinates"] = lonlat
				
				return geoJson["features"].([]dynamic), cartodb_id
			}
		}

		lonlat := make([][2]float64, 1)
		lonlat[0][0] = longitude
		lonlat[0][1] = latitude

		feature := dynamic{
			"type": "Feature",
			"properties": dynamic{
				"name": neightbourhood,
				"cartodb_id": cartodb_id,
				"avgprice": 0,
				"properties": append([]dynamic{}, dynamic{
					"bedrooms": bedrooms,
					"price": price})},
			"geometry": dynamic{
				"type": "MultiPolygon",
				"coordinates": lonlat}}

		cartodb_id++
		return append(geoJson["features"].([]dynamic), feature), cartodb_id
	}

	return geoJson["features"].([]dynamic), cartodb_id
}

func calculateAvgPrices(geoJson dynamic) (dynamic) {
	for _, feature := range geoJson["features"].([]dynamic) {
		var price int64
		var count int64
		for _, properties := range feature["properties"].(dynamic)["properties"].([]dynamic) {
			price += properties["price"].(int64)
			count++
		}
		feature["properties"].(dynamic)["avgprice"] = price/count
	}
	return geoJson
}

func main() {
	geoJson := make(dynamic)
	geoJson["type"] = "FeatureCollection"
	geoJson["features"] = []dynamic{}
	cartodb_id := 1

	psqlInfo := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable",
		postgres.Host, postgres.Port, postgres.User, postgres.Password, postgres.Dbname)

	db, err := sql.Open("postgres", psqlInfo)
	if err != nil {fmt.Printf("Could not connect to DB. %s \n", err)}
	defer db.Close()

	rows, err := db.Query("SELECT Neighbourhood, Latitude, Longitude, Bedrooms, Price FROM airbnb WHERE City LIKE '%adrid%'")
	if err != nil {fmt.Printf("SQL error. %s \n", err)}
	defer rows.Close()

	for rows.Next() {
		var neightbourhood sql.NullString
		var latitude, longitude sql.NullFloat64
		var bedrooms, price sql.NullInt64

		err = rows.Scan(&neightbourhood, &latitude, &longitude, &bedrooms, &price)
		if err != nil {fmt.Printf("Could not get row. %s \n", err)}

		geoJson["features"], cartodb_id = appendRow(geoJson, neightbourhood.String, latitude.Float64, longitude.Float64, bedrooms.Int64, price.Int64, cartodb_id)
	}

	geoJson = calculateAvgPrices(geoJson)

	geo, err := json.Marshal(geoJson)
	if err != nil {fmt.Printf("Can't convert to json. %s \n", err)}
	fmt.Println(string(geo))

	file, err := os.Create("geoJson.json")
	if err != nil {fmt.Printf("Can't create file. %s \n", err)}

	_, err = file.WriteString(string(geo))
	if err != nil {fmt.Printf("Can't write to file. %s \n", err)}
	err = file.Close()
	if err != nil {fmt.Printf("Can't close file. %s \n", err)}
}