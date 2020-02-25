# Car Number Plate Detector API


## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

**Definition**

`GET /getNumberPlate`

**Response**

```json
{
    "identifier": "NumberPlate",
    "plate no":"TN 0455",
    "Coordinates":[[2,3],[4,5],[7,8],[4,6]],
    "message":"success",
    "time"   :"Sun Sep  8 06:28:28 2019"
}
```

- `200 OK` on success
- `204 No Content` on success