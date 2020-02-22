# Page Crawlers #

food = [
    'YelpFood'
    ]
yelp = [
    food[0]
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
              "DROP TABLE IF EXISTS airbnb;"
              "CREATE TABLE airbnb (ID STRING, ListingUrl STRING, ScrapeID STRING, LastScraped STRING, Name STRING, Summary STRING, Space STRING, Description STRING, ExperiencesOffered STRING, NeighborhoodOverview STRING, Notes STRING, Transit STRING, Access STRING, Interaction STRING, HouseRules STRING, ThumbnailUrl STRING, MediumUrl STRING, PictureUrl STRING, XLPictureUrl STRING, HostID STRING, HostURL STRING, HostName STRING, HostSince STRING, HostLocation STRING, HostAbout STRING, HostResponseTime STRING, HostResponseRate STRING, HostAcceptanceRate STRING, HostThumbnailUrl STRING, HostPictureUrl STRING, HostNeighbourhood STRING, HostListingsCount STRING, HostTotalListingsCount STRING, HostVerifications STRING, Street STRING, Neighbourhood STRING, NeighbourhoodCleansed STRING, NeighbourhoodGroupCleansed STRING, City STRING, State STRING, Zipcode STRING, Market STRING, SmartLocation STRING, CountryCode STRING, Country STRING, Latitude STRING, Longitude STRING, PropertyType STRING, RoomType STRING, Accommodates STRING, Bathrooms STRING, Bedrooms STRING, Beds STRING, BedType STRING, Amenities STRING, SquareFeet STRING, Price STRING, WeeklyPrice STRING, MonthlyPrice STRING, SecurityDeposit STRING, CleaningFee STRING, GuestsIncluded STRING, ExtraPeople STRING, MinimumNights STRING, MaximumNights STRING, CalendarUpdated STRING, HasAvailability STRING, Availability30 STRING, Availability60 STRING, Availability90 STRING, Availability365 STRING, CalendarlastScraped STRING, NumberofReviews STRING, FirstReview STRING, LastReview STRING, ReviewScoresRating STRING, ReviewScoresAccuracy STRING, ReviewScoresCleanliness STRING, ReviewScoresCheckin STRING, ReviewScoresCommunication STRING, ReviewScoresLocation STRING, ReviewScoresValue STRING, License STRING, JurisdictionNames STRING, CancellationPolicy STRING, Calculatedhostlistingscount STRING, ReviewsperMonth STRING, Geolocation STRING, Features STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY ';';"
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
              "DROP TABLE IF EXISTS yelp_food;"
              "CREATE TABLE yelp_food (ID STRING, URL STRING, Name STRING, Score STRING, Reviews STRING, PriceLevel STRING, Category STRING, Phone STRING, Address STRING, District STRING, Latitude STRING, Longitude STRING) ROW FORMAT DELIMITED FIELDS TERMINATED BY '|';"
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
              "" # Esta query se declara en ApiUtils.get_data(), un script que se adapta a los datos solicitados.
            ]    # El script solo funciona si primero se ha creado la tabla correspondiente.
        }
    }
}

ComputeDistances = {
    "placement": {
        "cluster_name": "hive"
    },
    "reference": {
        "job_id": "CalcularDistancias"
    },
    "hive_job": {
        "query_list": {
            "queries": [
              "" # Esta query se declara en ApiUtils.get_querys()
            ]
        }
    }
}