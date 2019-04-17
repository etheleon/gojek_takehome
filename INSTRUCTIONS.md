# GoJek Takehome

# Software Engineer, Machine Learning & Big Data

The goal of this exercise is to provide a realistic example of the kind of work we do and evaluate your ability to do such work. /This exercise should require about *eight hours* of your time./

Please reach out to us if you have any questions! When done, please follow the submission instructions and send your submission via email.

## Problem statement
We would like you to build a Web Service that provides basic analytics over taxi data. The live data can be obtained from  [BigQuery](https://cloud.google.com/bigquery/)  at  [NYC TLC trips](https://console.cloud.google.com/marketplace/details/city-of-new-york/nyc-tlc-trips) . You will use only the following tables:


| Tables |
| — |
| tlc_green_trips_2014 |
| tlc_green_trips_2015 |
| tlc_green_trips_2016 |
| tlc_green_trips_2017 |
| tlc_yellow_trips_2015 |
| tlc_yellow_trips_2016 |
| tlc_yellow_trips_2017 |

The endpoints you need to support are:
* Total trips per day
* Fare heatmap
* Average speed in the past 24 hours

```bash
URL=localhost
PORT= 8080
```

### Total Trips per day (in date range)

```bash
START_DATE=2019-01-01
END_DATE=2019-01-31

curl http://${URL}:${PORT}/total_trips?start=${START_DATE}&end=${END_DATE}
```

Returning

```json
{
   "data":[
      {
         "date":"2019-01-01",
         "total_trips":321
      },
      {
         "date":"2019-01-02",
         "total_trips":432
      },
      {
         "date":"2019-01-03",
         "total_trips":543
      },
      {
         "date":"2019-01-31",
         "total_trips":987
      }
   ]
}
```


### Fare heatmap

The average fare (fare_amount) per pick up location  [S2 ID](http://s2geometry.io/)  at level 16 for the given date.

```bash
DATE=2019-01-01

curl http://${URL}:${PORT}/average_fare_heatmap?date=${DATE}
```

```json
{
   "data":[
      {
         "s2id":"951977d37",
         "fare":13.21
      },
      {
         "s2id":"951977d39",
         "fare":4.32
      },
      {
         "s2id":"951977d40",
         "fare":5.43
      },
      {
         "s2id":"951978321",
         "fare":9.87
      }
   ]
}
```

### Average speed in the past 24 hours

Average speed (trip_distance / (dropoff_datetime - pickup_datetime)) of trips that ended in the past 24 hours from the provided date.

```bash
DATE=2019-01-01

curl http://${URL}:${PORT}/average_speed_24hrs?date=${DATE}
```

```json
{
   "data":[
      {
         "average_speed":24.7
      }
   ]
}
```


## Other considerations
* All dates will be in ISO 8601 YYYY-MM-DD format and date ranges are inclusive on both ends. Timezone is local to the dataset, i.e., New York City’s Eastern Standard Time, and will not be specified.

* You should also handle requests for the current day, even if it is incomplete, i.e., return the average speed for all trips that have occurred up to the current time today.

* Please use the correct HTTP verbs and errors, and also set the response headers appropriately.

# Evaluation
* Please include a short motivation on major design decisions you have made.
> Readable

* Your code will need to run locally on our machines and bind to/respond on localhost. Please provide enough instructions and build scripts for us to do so.
> Docker

* You can use any language and libraries you please, but be prepared to discuss your choices with us.
> Python

* Please provide your git history. You can do this via  [git-bundle](https://git-scm.com/book/en/v2/Git-Tools-Bundling)  or by sending us a link to a *_private_* git repo. We will be taking a look at your git history, so please keep it tidy and descriptive. Do NOT share your code on a *_public_* repo.

* You should consider this as a production system and include relevant documentation and tests in your code.
> Pytest with PyDoc

* You should also consider future maintenance of the code and its architecture. Note that you will be working with us to extend this code at a later stage of the interview process.
> Okay, will try to set up CI | CD with spinnaker and gcr,

* Runtime performance is not critical but should not be neglected. Choose your algorithms and data structures wisely.
