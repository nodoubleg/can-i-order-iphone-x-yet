from mock import patch

from cli import can_i_order_iphone_x


RESP_NO_STORES_HAVE_STOCK = {
	"head": {
		"status": "200",
		"data": {}
	},
	"body": {
		"stores": [{
			"storeEmail": "regentstreet@apple.com",
			"storeName": "Regent Street",
			"reservationUrl": "http://www.apple.com/uk/retail/regentstreet",
			"makeReservationUrl": "http://www.apple.com/uk/retail/regentstreet",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R092.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "London",
			"storeNumber": "R092",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple Regent Street",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "020 7153 9000",
			"address": {
				"address": "Apple Regent Street",
				"address3": None,
				"address2": "235 Regent Street",
				"postalCode": "W1B 2EL"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/regentstreet",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "10:00-21:00",
					"storeDays": "Mon-Fri:"
				}, {
					"storeTimings": "10:00-20:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "12:00-18:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.51424,
			"storelongitude": -0.14214,
			"storedistance": 1.82,
			"storeDistanceWithUnit": "1.82 mi",
			"storeDistanceVoText": "1.82 mi from W1B 2EL",
			"storelistnumber": 1,
			"storeListNumber": 1
		}, {
			"storeEmail": "coventgarden@apple.com",
			"storeName": "Covent Garden",
			"reservationUrl": "http://www.apple.com/uk/retail/coventgarden",
			"makeReservationUrl": "http://www.apple.com/uk/retail/coventgarden",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R245.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "London",
			"storeNumber": "R245",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": False,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "ineligible"
				}
			},
			"phoneNumber": "020 7447 1400",
			"address": {
				"address": "Apple Covent Garden",
				"address3": None,
				"address2": "No. 1-7 The Piazza",
				"postalCode": "WC2E 8HB"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/coventgarden",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "10:00-20:00",
					"storeDays": "Mon-Sat:"
				}, {
					"storeTimings": "12:00-18:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.51217,
			"storelongitude": -0.12352,
			"storedistance": 2.29,
			"storeDistanceWithUnit": "2.29 mi",
			"storeDistanceVoText": "2.29 mi from WC2E 8HB",
			"storelistnumber": 2,
			"storeListNumber": 2
		}, {
			"storeEmail": "whitecity@apple.com",
			"storeName": "White City",
			"reservationUrl": "http://www.apple.com/uk/retail/whitecity",
			"makeReservationUrl": "http://www.apple.com/uk/retail/whitecity",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R226.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "London",
			"storeNumber": "R226",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple White City",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "020 8433 4600",
			"address": {
				"address": "Apple White City",
				"address3": "Ariel Way",
				"address2": "Westfield London",
				"postalCode": "W12 7GF"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/whitecity",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "10:00-22:00",
					"storeDays": "Mon-Sat:"
				}, {
					"storeTimings": "12:00-18:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.50747,
			"storelongitude": -0.22066,
			"storedistance": 2.52,
			"storeDistanceWithUnit": "2.52 mi",
			"storeDistanceVoText": "2.52 mi from W12 7GF",
			"storelistnumber": 3,
			"storeListNumber": 3
		}, {
			"storeEmail": "brentcross@apple.com",
			"storeName": "Brent Cross",
			"reservationUrl": "http://www.apple.com/uk/retail/brentcross",
			"makeReservationUrl": "http://www.apple.com/uk/retail/brentcross",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R163.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "London",
			"storeNumber": "R163",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": False,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "ineligible"
				}
			},
			"phoneNumber": "020 3126 9200",
			"address": {
				"address": "Apple Brent Cross",
				"address3": "Brent Cross Shopping Centre",
				"address2": "Upper West Mall",
				"postalCode": "NW4 3FP"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/brentcross",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "10:00-20:00",
					"storeDays": "Mon-Fri:"
				}, {
					"storeTimings": "09:00-20:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "12:00-18:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.576232751093976,
			"storelongitude": -0.224919319152832,
			"storedistance": 6.27,
			"storeDistanceWithUnit": "6.27 mi",
			"storeDistanceVoText": "6.27 mi from NW4 3FP",
			"storelistnumber": 4,
			"storeListNumber": 4
		}, {
			"storeEmail": "stratfordcity@apple.com",
			"storeName": "Stratford City",
			"reservationUrl": "http://www.apple.com/uk/retail/stratfordcity",
			"makeReservationUrl": "http://www.apple.com/uk/retail/stratfordcity",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R410.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "London",
			"storeNumber": "R410",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple Stratford City",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "020 8277 2200",
			"address": {
				"address": "Apple Stratford City",
				"address3": None,
				"address2": "The Arcade, Westfield Stratford City",
				"postalCode": "E20 1EQ"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/stratfordcity",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "10:00-21:00",
					"storeDays": "Mon-Fri:"
				}, {
					"storeTimings": "09:00-21:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "12:00-18:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.54409,
			"storelongitude": -0.00681,
			"storedistance": 7.74,
			"storeDistanceWithUnit": "7.74 mi",
			"storeDistanceVoText": "7.74 mi from E20 1EQ",
			"storelistnumber": 5,
			"storeListNumber": 5
		}, {
			"storeEmail": "bentallcentre@apple.com",
			"storeName": "Bentall Centre",
			"reservationUrl": "http://www.apple.com/uk/retail/bentallcentre",
			"makeReservationUrl": "http://www.apple.com/uk/retail/bentallcentre",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R227.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "Kingston upon Thames",
			"storeNumber": "R227",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": False,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "ineligible"
				}
			},
			"phoneNumber": "020 8233 3400",
			"address": {
				"address": "Apple Bentall Centre",
				"address3": "Wood Street",
				"address2": "The Bentall Centre",
				"postalCode": "KT1 1TP"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/bentallcentre",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "09:30-18:00",
					"storeDays": "Mon-Wed, Fri:"
				}, {
					"storeTimings": "09:30-21:00",
					"storeDays": "Thu:"
				}, {
					"storeTimings": "09:00-19:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "11:00-17:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.41147,
			"storelongitude": -0.30509,
			"storedistance": 8.19,
			"storeDistanceWithUnit": "8.19 mi",
			"storeDistanceVoText": "8.19 mi from KT1 1TP",
			"storelistnumber": 6,
			"storeListNumber": 6
		}, {
			"storeEmail": "bromley@apple.com",
			"storeName": "Bromley",
			"reservationUrl": "http://www.apple.com/uk/retail/bromley",
			"makeReservationUrl": "http://www.apple.com/uk/retail/bromley",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R496.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "Bromley",
			"storeNumber": "R496",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple Bromley",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "020 8225 5500",
			"address": {
				"address": "Apple Bromley",
				"address3": None,
				"address2": "The Glades Bromley Shopping Centre",
				"postalCode": "BR1 1DN"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/bromley",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "09:00-19:00",
					"storeDays": "Mon-Wed, Fri-Sat:"
				}, {
					"storeTimings": "09:00-21:00",
					"storeDays": "Thu:"
				}, {
					"storeTimings": "11:00-17:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.40263,
			"storelongitude": 0.01568,
			"storedistance": 10.04,
			"storeDistanceWithUnit": "10.04 mi",
			"storeDistanceVoText": "10.04 mi from BR1 1DN",
			"storelistnumber": 7,
			"storeListNumber": 7
		}, {
			"storeEmail": "watford@apple.com",
			"storeName": "Watford",
			"reservationUrl": "http://www.apple.com/uk/retail/watford",
			"makeReservationUrl": "http://www.apple.com/uk/retail/watford",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R527.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "Watford",
			"storeNumber": "R527",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple Watford",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "019 2342 1700",
			"address": {
				"address": "Apple Watford",
				"address3": None,
				"address2": "Intu Watford Shopping Centre",
				"postalCode": "WD17 2TN"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/watford",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "09:00-18:00",
					"storeDays": "Mon-Wed, Fri:"
				}, {
					"storeTimings": "09:00-21:00",
					"storeDays": "Thu:"
				}, {
					"storeTimings": "09:00-19:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "11:00-17:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.655216,
			"storelongitude": -0.39291,
			"storedistance": 14.83,
			"storeDistanceWithUnit": "14.83 mi",
			"storeDistanceVoText": "14.83 mi from WD17 2TN",
			"storelistnumber": 8,
			"storeListNumber": 8
		}, {
			"storeEmail": "lakeside@apple.com",
			"storeName": "Lakeside",
			"reservationUrl": "http://www.apple.com/uk/retail/lakeside",
			"makeReservationUrl": "http://www.apple.com/uk/retail/lakeside",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R242.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "Grays",
			"storeNumber": "R242",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple Lakeside",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "017 0871 7500",
			"address": {
				"address": "Apple Lakeside",
				"address3": "Lakeside Shopping Centre",
				"address2": "West Thurrock Way",
				"postalCode": "RM20 2ZP"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/lakeside",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "10:00-22:00",
					"storeDays": "Mon-Fri:"
				}, {
					"storeTimings": "09:00-21:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "11:00-17:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.48856,
			"storelongitude": 0.28326,
			"storedistance": 19.37,
			"storeDistanceWithUnit": "19.37 mi",
			"storeDistanceVoText": "19.37 mi from RM20 2ZP",
			"storelistnumber": 9,
			"storeListNumber": 9
		}, {
			"storeEmail": "theoracle@apple.com",
			"storeName": "The Oracle",
			"reservationUrl": "http://www.apple.com/uk/retail/theoracle",
			"makeReservationUrl": "http://www.apple.com/uk/retail/theoracle",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R176.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "Reading",
			"storeNumber": "R176",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple The Oracle",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "0118 925 4500",
			"address": {
				"address": "Apple The Oracle",
				"address3": None,
				"address2": "Upper Level, The Oracle Shopping Centre",
				"postalCode": "RG1 2AG"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/theoracle",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "09:30-20:00",
					"storeDays": "Mon-Fri:"
				}, {
					"storeTimings": "09:00-19:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "11:00-17:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.453639,
			"storelongitude": -0.971324,
			"storedistance": 34.72,
			"storeDistanceWithUnit": "34.72 mi",
			"storeDistanceVoText": "34.72 mi from RG1 2AG",
			"storelistnumber": 10,
			"storeListNumber": 10
		}, {
			"storeEmail": "festivalplace@apple.com",
			"storeName": "Festival Place",
			"reservationUrl": "http://www.apple.com/uk/retail/festivalplace",
			"makeReservationUrl": "http://www.apple.com/uk/retail/festivalplace",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R482.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "Basingstoke",
			"storeNumber": "R482",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple Festival Place",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "0125 669 6000",
			"address": {
				"address": "Apple Festival Place",
				"address3": None,
				"address2": "Upper Level, Queen Anne’s Walk",
				"postalCode": "RG21 7BE"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/festivalplace",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "09:00-19:00",
					"storeDays": "Mon-Wed, Sat:"
				}, {
					"storeTimings": "09:00-20:00",
					"storeDays": "Thu-Fri:"
				}, {
					"storeTimings": "11:00-17:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.26526,
			"storelongitude": -1.08538,
			"storedistance": 42.62,
			"storeDistanceWithUnit": "42.62 mi",
			"storeDistanceVoText": "42.62 mi from RG21 7BE",
			"storelistnumber": 11,
			"storeListNumber": 11
		}],
		"overlayInitiatedFromWarmStart": False,
		"viewMoreHoursLinkText": "View more hours",
		"storesCount": "11 stores found near SW33xb",
		"little": False,
		"location": "SW33xb",
		"notAvailableNearby": "Not available today at [X] nearest stores.",
		"notAvailableNearOneStore": "Not available today at the nearest store.",
		"productLocatorSpecialHours": "Special opening hours:",
		"productLocatorSpecialHoursView": "View special store hours"
	}
}

RESP_ONE_STORES_HAVE_STOCK = {
	"head": {
		"status": "200",
		"data": {}
	},
	"body": {
		"stores": [{
			"storeEmail": "regentstreet@apple.com",
			"storeName": "Regent Street",
			"reservationUrl": "http://www.apple.com/uk/retail/regentstreet",
			"makeReservationUrl": "http://www.apple.com/uk/retail/regentstreet",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R092.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "London",
			"storeNumber": "R092",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": True,
					"storePickupQuote": "Currently unavailable at Apple Regent Street",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "020 7153 9000",
			"address": {
				"address": "Apple Regent Street",
				"address3": None,
				"address2": "235 Regent Street",
				"postalCode": "W1B 2EL"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/regentstreet",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "10:00-21:00",
					"storeDays": "Mon-Fri:"
				}, {
					"storeTimings": "10:00-20:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "12:00-18:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.51424,
			"storelongitude": -0.14214,
			"storedistance": 1.82,
			"storeDistanceWithUnit": "1.82 mi",
			"storeDistanceVoText": "1.82 mi from W1B 2EL",
			"storelistnumber": 1,
			"storeListNumber": 1
		}, {
			"storeEmail": "coventgarden@apple.com",
			"storeName": "Covent Garden",
			"reservationUrl": "http://www.apple.com/uk/retail/coventgarden",
			"makeReservationUrl": "http://www.apple.com/uk/retail/coventgarden",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R245.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "London",
			"storeNumber": "R245",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": False,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "ineligible"
				}
			},
			"phoneNumber": "020 7447 1400",
			"address": {
				"address": "Apple Covent Garden",
				"address3": None,
				"address2": "No. 1-7 The Piazza",
				"postalCode": "WC2E 8HB"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/coventgarden",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "10:00-20:00",
					"storeDays": "Mon-Sat:"
				}, {
					"storeTimings": "12:00-18:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.51217,
			"storelongitude": -0.12352,
			"storedistance": 2.29,
			"storeDistanceWithUnit": "2.29 mi",
			"storeDistanceVoText": "2.29 mi from WC2E 8HB",
			"storelistnumber": 2,
			"storeListNumber": 2
		}, {
			"storeEmail": "whitecity@apple.com",
			"storeName": "White City",
			"reservationUrl": "http://www.apple.com/uk/retail/whitecity",
			"makeReservationUrl": "http://www.apple.com/uk/retail/whitecity",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R226.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "London",
			"storeNumber": "R226",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple White City",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "020 8433 4600",
			"address": {
				"address": "Apple White City",
				"address3": "Ariel Way",
				"address2": "Westfield London",
				"postalCode": "W12 7GF"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/whitecity",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "10:00-22:00",
					"storeDays": "Mon-Sat:"
				}, {
					"storeTimings": "12:00-18:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.50747,
			"storelongitude": -0.22066,
			"storedistance": 2.52,
			"storeDistanceWithUnit": "2.52 mi",
			"storeDistanceVoText": "2.52 mi from W12 7GF",
			"storelistnumber": 3,
			"storeListNumber": 3
		}, {
			"storeEmail": "brentcross@apple.com",
			"storeName": "Brent Cross",
			"reservationUrl": "http://www.apple.com/uk/retail/brentcross",
			"makeReservationUrl": "http://www.apple.com/uk/retail/brentcross",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R163.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "London",
			"storeNumber": "R163",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": False,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "ineligible"
				}
			},
			"phoneNumber": "020 3126 9200",
			"address": {
				"address": "Apple Brent Cross",
				"address3": "Brent Cross Shopping Centre",
				"address2": "Upper West Mall",
				"postalCode": "NW4 3FP"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/brentcross",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "10:00-20:00",
					"storeDays": "Mon-Fri:"
				}, {
					"storeTimings": "09:00-20:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "12:00-18:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.576232751093976,
			"storelongitude": -0.224919319152832,
			"storedistance": 6.27,
			"storeDistanceWithUnit": "6.27 mi",
			"storeDistanceVoText": "6.27 mi from NW4 3FP",
			"storelistnumber": 4,
			"storeListNumber": 4
		}, {
			"storeEmail": "stratfordcity@apple.com",
			"storeName": "Stratford City",
			"reservationUrl": "http://www.apple.com/uk/retail/stratfordcity",
			"makeReservationUrl": "http://www.apple.com/uk/retail/stratfordcity",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R410.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "London",
			"storeNumber": "R410",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple Stratford City",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "020 8277 2200",
			"address": {
				"address": "Apple Stratford City",
				"address3": None,
				"address2": "The Arcade, Westfield Stratford City",
				"postalCode": "E20 1EQ"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/stratfordcity",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "10:00-21:00",
					"storeDays": "Mon-Fri:"
				}, {
					"storeTimings": "09:00-21:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "12:00-18:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.54409,
			"storelongitude": -0.00681,
			"storedistance": 7.74,
			"storeDistanceWithUnit": "7.74 mi",
			"storeDistanceVoText": "7.74 mi from E20 1EQ",
			"storelistnumber": 5,
			"storeListNumber": 5
		}, {
			"storeEmail": "bentallcentre@apple.com",
			"storeName": "Bentall Centre",
			"reservationUrl": "http://www.apple.com/uk/retail/bentallcentre",
			"makeReservationUrl": "http://www.apple.com/uk/retail/bentallcentre",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R227.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "Kingston upon Thames",
			"storeNumber": "R227",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": False,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "ineligible"
				}
			},
			"phoneNumber": "020 8233 3400",
			"address": {
				"address": "Apple Bentall Centre",
				"address3": "Wood Street",
				"address2": "The Bentall Centre",
				"postalCode": "KT1 1TP"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/bentallcentre",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "09:30-18:00",
					"storeDays": "Mon-Wed, Fri:"
				}, {
					"storeTimings": "09:30-21:00",
					"storeDays": "Thu:"
				}, {
					"storeTimings": "09:00-19:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "11:00-17:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.41147,
			"storelongitude": -0.30509,
			"storedistance": 8.19,
			"storeDistanceWithUnit": "8.19 mi",
			"storeDistanceVoText": "8.19 mi from KT1 1TP",
			"storelistnumber": 6,
			"storeListNumber": 6
		}, {
			"storeEmail": "bromley@apple.com",
			"storeName": "Bromley",
			"reservationUrl": "http://www.apple.com/uk/retail/bromley",
			"makeReservationUrl": "http://www.apple.com/uk/retail/bromley",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R496.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "Bromley",
			"storeNumber": "R496",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple Bromley",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "020 8225 5500",
			"address": {
				"address": "Apple Bromley",
				"address3": None,
				"address2": "The Glades Bromley Shopping Centre",
				"postalCode": "BR1 1DN"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/bromley",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "09:00-19:00",
					"storeDays": "Mon-Wed, Fri-Sat:"
				}, {
					"storeTimings": "09:00-21:00",
					"storeDays": "Thu:"
				}, {
					"storeTimings": "11:00-17:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.40263,
			"storelongitude": 0.01568,
			"storedistance": 10.04,
			"storeDistanceWithUnit": "10.04 mi",
			"storeDistanceVoText": "10.04 mi from BR1 1DN",
			"storelistnumber": 7,
			"storeListNumber": 7
		}, {
			"storeEmail": "watford@apple.com",
			"storeName": "Watford",
			"reservationUrl": "http://www.apple.com/uk/retail/watford",
			"makeReservationUrl": "http://www.apple.com/uk/retail/watford",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R527.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "Watford",
			"storeNumber": "R527",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple Watford",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "019 2342 1700",
			"address": {
				"address": "Apple Watford",
				"address3": None,
				"address2": "Intu Watford Shopping Centre",
				"postalCode": "WD17 2TN"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/watford",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "09:00-18:00",
					"storeDays": "Mon-Wed, Fri:"
				}, {
					"storeTimings": "09:00-21:00",
					"storeDays": "Thu:"
				}, {
					"storeTimings": "09:00-19:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "11:00-17:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.655216,
			"storelongitude": -0.39291,
			"storedistance": 14.83,
			"storeDistanceWithUnit": "14.83 mi",
			"storeDistanceVoText": "14.83 mi from WD17 2TN",
			"storelistnumber": 8,
			"storeListNumber": 8
		}, {
			"storeEmail": "lakeside@apple.com",
			"storeName": "Lakeside",
			"reservationUrl": "http://www.apple.com/uk/retail/lakeside",
			"makeReservationUrl": "http://www.apple.com/uk/retail/lakeside",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R242.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "Grays",
			"storeNumber": "R242",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple Lakeside",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "017 0871 7500",
			"address": {
				"address": "Apple Lakeside",
				"address3": "Lakeside Shopping Centre",
				"address2": "West Thurrock Way",
				"postalCode": "RM20 2ZP"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/lakeside",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "10:00-22:00",
					"storeDays": "Mon-Fri:"
				}, {
					"storeTimings": "09:00-21:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "11:00-17:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.48856,
			"storelongitude": 0.28326,
			"storedistance": 19.37,
			"storeDistanceWithUnit": "19.37 mi",
			"storeDistanceVoText": "19.37 mi from RM20 2ZP",
			"storelistnumber": 9,
			"storeListNumber": 9
		}, {
			"storeEmail": "theoracle@apple.com",
			"storeName": "The Oracle",
			"reservationUrl": "http://www.apple.com/uk/retail/theoracle",
			"makeReservationUrl": "http://www.apple.com/uk/retail/theoracle",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R176.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "Reading",
			"storeNumber": "R176",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple The Oracle",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "0118 925 4500",
			"address": {
				"address": "Apple The Oracle",
				"address3": None,
				"address2": "Upper Level, The Oracle Shopping Centre",
				"postalCode": "RG1 2AG"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/theoracle",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "09:30-20:00",
					"storeDays": "Mon-Fri:"
				}, {
					"storeTimings": "09:00-19:00",
					"storeDays": "Sat:"
				}, {
					"storeTimings": "11:00-17:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.453639,
			"storelongitude": -0.971324,
			"storedistance": 34.72,
			"storeDistanceWithUnit": "34.72 mi",
			"storeDistanceVoText": "34.72 mi from RG1 2AG",
			"storelistnumber": 10,
			"storeListNumber": 10
		}, {
			"storeEmail": "festivalplace@apple.com",
			"storeName": "Festival Place",
			"reservationUrl": "http://www.apple.com/uk/retail/festivalplace",
			"makeReservationUrl": "http://www.apple.com/uk/retail/festivalplace",
			"storeImageUrl": "https://rtlimages.apple.com/cmc/dieter/store/4_3/R482.png?resize=828:*&output-format=jpg",
			"country": "GB",
			"city": "Basingstoke",
			"storeNumber": "R482",
			"partsAvailability": {
				"MQAC2B/A": {
					"storePickEligible": True,
					"storeSearchEnabled": True,
					"storeSelectionEnabled": False,
					"storePickupQuote": "Currently unavailable at Apple Festival Place",
					"pickupSearchQuote": "Currently unavailable",
					"storePickupLabel": "Pickup:",
					"partNumber": "MQAC2B/A",
					"purchaseOption": "",
					"ctoOptions": "",
					"storePickupLinkText": "Check availability",
					"storePickupProductTitle": "iPhone X 64GB Space Grey",
					"pickupDisplay": "unavailable"
				}
			},
			"phoneNumber": "0125 669 6000",
			"address": {
				"address": "Apple Festival Place",
				"address3": None,
				"address2": "Upper Level, Queen Anne’s Walk",
				"postalCode": "RG21 7BE"
			},
			"hoursUrl": "http://www.apple.com/uk/retail/festivalplace",
			"storeHours": {
				"storeHoursText": "Store Hours",
				"bopisPickupDays": "Days",
				"bopisPickupHours": "Hours",
				"hours": [{
					"storeTimings": "09:00-19:00",
					"storeDays": "Mon-Wed, Sat:"
				}, {
					"storeTimings": "09:00-20:00",
					"storeDays": "Thu-Fri:"
				}, {
					"storeTimings": "11:00-17:00",
					"storeDays": "Sun:"
				}]
			},
			"storelatitude": 51.26526,
			"storelongitude": -1.08538,
			"storedistance": 42.62,
			"storeDistanceWithUnit": "42.62 mi",
			"storeDistanceVoText": "42.62 mi from RG21 7BE",
			"storelistnumber": 11,
			"storeListNumber": 11
		}],
		"overlayInitiatedFromWarmStart": False,
		"viewMoreHoursLinkText": "View more hours",
		"storesCount": "11 stores found near SW33xb",
		"little": False,
		"location": "SW33xb",
		"notAvailableNearby": "Not available today at [X] nearest stores.",
		"notAvailableNearOneStore": "Not available today at the nearest store.",
		"productLocatorSpecialHours": "Special opening hours:",
		"productLocatorSpecialHoursView": "View special store hours"
	}
}


@patch('cli.requests')
def test_can_i_order_iphone_x_says_no_when_not_yet_available(mock_requests):
    mock_requests.get().json.return_value = RESP_NO_STORES_HAVE_STOCK

    can_i, detail = can_i_order_iphone_x(post_code='se14yu')
    assert can_i is False
    assert detail == 'Checked 11 stores. Not available yet'


@patch('cli.requests')
def test_can_i_order_iphone_x_says_yes_when_available(mock_requests):
    mock_requests.get().json.return_value = RESP_ONE_STORES_HAVE_STOCK

    can_i, detail = can_i_order_iphone_x(post_code='se14yu')
    assert can_i is True
    assert detail == 'IPhone X now available at:\nApple Regent Street'