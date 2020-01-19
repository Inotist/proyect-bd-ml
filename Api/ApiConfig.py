# Page Crawlers #

food = 'YelpFood'
yelp = [
    food
    ]


##### Jobs #####

CreateTableAirbnb = {
    "placement": {
        "cluster_name": "hive"
    },
    "reference": {
        "job_id": "CrearTablaAirbnb"
    },
    "hive_job": {
        "query_list": {
            "queries": [
              "CREATE TABLE airbnb (\nID INT,\nListing_Url STRING,\nScrape_ID INT,\nLast_Scraped STRING,\nName STRING,\nSummary STRING,\nSpace STRING,\nDescription STRING,\nExperiences_Offered STRING,\nNeighborhood_Overview STRING,\nNotes STRING,\nTransit STRING,\nAccess STRING,\nInteraction STRING,\nHouse_Rules STRING,\nThumbnail_Url STRING,\nMedium_Url STRING,\nPicture_Url STRING,\nXL_Picture_Url STRING,\nHost_ID INT,\nHost_URL STRING,\nHost_Name STRING,\nHost_Since STRING,\nHost_Location STRING,\nHost_About STRING,\nHost_Response_Time STRING,\nHost_Response_Rate STRING,\nHost_Acceptance_Rate STRING,\nHost_Thumbnail_Url STRING,\nHost_Picture_Url STRING,\nHost_Neighbourhood STRING,\nHost_Listings_Count STRING,\nHost_Total_Listings_Count STRING,\nHost_Verifications STRING,\nStreet STRING,\nNeighbourhood STRING,\nNeighbourhood_Cleansed STRING,\nNeighbourhood_Group_Cleansed STRING,\nCity STRING,\nState STRING,\nZipcode STRING,\nMarket STRING,\nSmart_Location STRING,\nCountry_Code STRING,\nCountry STRING,\nLatitude DOUBLE,\nLongitude DOUBLE,\nProperty_Type STRING,\nRoom_Type STRING,\nAccommodates STRING,\nBathrooms STRING,\nBedrooms STRING,\nBeds STRING,\nBed_Type STRING,\nAmenities STRING,\nSquare_Feet STRING,\nPrice STRING,\nWeekly_Price STRING,\nMonthly_Price STRING,\nSecurity_Deposit STRING,\nCleaning_Fee STRING,\nGuests_Included STRING,\nExtra_People STRING,\nMinimum_Nights STRING,\nMaximum_Nights STRING,\nCalendar_Updated STRING,\nHas_Availability STRING,\nAvailability_30 STRING,\nAvailability_60 STRING,\nAvailability_90 STRING,\nAvailability_365 STRING,\nCalendar_last_Scraped STRING,\nNumber_of_Reviews STRING,\nFirst_Review STRING,\nLast_Review STRING,\nReview_Scores_Rating STRING,\nReview_Scores_Accuracy STRING,\nReview_Scores_Cleanliness STRING,\nReview_Scores_Checkin STRING,\nReview_Scores_Communication STRING,\nReview_Scores_Location STRING,\nReview_Scores_Value STRING,\nLicense STRING,\nJurisdiction_Names STRING,\nCancellation_Policy STRING,\nCalculated_host_listings_count STRING,\nReviews_per_Month STRING,\nGeolocation STRING,\nFeatures STRING\n)\nROW FORMAT DELIMITED FIELDS TERMINATED BY ';';"
            ]
        }
    }
}

CreateTableYelpFood = {
    "placement": {
        "cluster_name": "hive"
    },
    "reference": {
        "job_id": "CrearTablaYelpFood"
    },
    "hive_job": {
        "query_list": {
            "queries": [
              "CREATE TABLE yelp_food (ID INT,\nURL STRING,\nName STRING,\nScore STRING,\nReviews STRING,\nPrice_Level STRING,\nCategory STRING,\nPhone STRING,\nAddress STRING,\nDistrict STRING,\nLatitude DOUBLE,\nLongitude DOUBLE)\nROW FORMAT DELIMITED FIELDS TERMINATED BY '||';"
            ]
        }
    }
}

LoadData = {
    "placement": {
        "cluster_name": "hive"
    },
    "reference": {
        "job_id": "CargarDatos"
    },
    "hive_job": {
        "query_list": {
            "queries": [
              "" # Esta query se declara en ApiUtils.get_path(), un script que se adapta a los datos solicitados.
            ]    # El script solo funciona si primero se ha creado la tabla correspondiente.
        }
    }
}

CalculateDistances = {
    "placement": {
        "cluster_name": "hive"
    },
    "reference": {
        "job_id": "CalcularDistancias"
    },
    "hive_job": {
        "query_list": {
            "queries": [
              "SELECT airbnb.ID, food.ID FROM airbnb, food WHERE\nsqrt(pow(airbnb.Latitude - food.Latitude, 2) + pow(airbnb.Longitude - food.Longitude, 2)) < 0.01"
            ]
        }
    }
}