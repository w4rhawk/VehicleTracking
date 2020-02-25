# Car Parking Space Detector API

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

**Definition**

`GET /getFreeSpaceToPark`

**Response**

```json
	json_data= {
		        "identifier"          	  : "FreeSpace",
                "no of free spots"        : 5,
                "message"                 :"success",
                "time"                    :"Fri Oct 18 23:55:59 2019",
                "Entry Authentication"    :"OK"
               }
```

- `200 OK` on success
- `204 No Content` on success