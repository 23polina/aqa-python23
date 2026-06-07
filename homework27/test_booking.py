def test_create_booking(api_client):
    body = {
        "firstname": "Test",
        "lastname": "Brown",
        "totalprice": 11204,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-10"
        },
        "additionalneeds": "Breakfast"
    }
    post_response = api_client.post_request("/booking", body=body)
    post_response_json = post_response.json()

    assert post_response.status_code == 200
    assert post_response_json["booking"]["firstname"] == "Test"
    assert post_response_json["booking"]["lastname"] == "Brown"

    booking_id = post_response_json["bookingid"]
    get_response = api_client.get_request(f"/booking/{booking_id}")

    assert get_response.status_code == 200
    assert get_response.json() == post_response_json["booking"]


def test_get_all_bookings(api_client):
    get_response = api_client.get_request("/booking")
    print(get_response.json())
    assert get_response.status_code == 200
    assert get_response.json() is not None


def test_get_booking_with_incorrect_id(api_client):
    get_response = api_client.get_request("/booking/lalalallalalalal12344")
    assert get_response.status_code == 404


def test_update_booking_successfully(api_client, auth):
    body_post = {
        "firstname": "Update",
        "lastname": "Brown",
        "totalprice": 11204,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-10"
        },
        "additionalneeds": "Breakfast"
    }
    post_response = api_client.post_request("/booking", body=body_post)
    booking_id = post_response.json()["bookingid"]

    put_body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 1111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-10"
        },
        "additionalneeds": "No Breakfast"
    }
    put_response = api_client.put_request(f"/booking/{booking_id}", body=put_body, token=auth)
    assert put_response.status_code == 200
    assert put_response.json() == put_body

    get_response = api_client.get_request(f"/booking/{booking_id}")
    assert get_response.json() == put_response.json()


def test_update_booking_without_passing_token(api_client):
    body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 1111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-10"
        },
        "additionalneeds": "No Breakfast"
    }
    put_response = api_client.put_request("/booking/1332", body=body)
    assert put_response.status_code == 403


def test_partial_booking_update(api_client, auth):
    get_response = api_client.get_request("/booking/4097")
    assert get_response.json()["firstname"] != "Mason"
    assert get_response.json()["bookingdates"]["checkin"] != "2026-08-02"
    assert get_response.json()["bookingdates"]["checkout"] != "2026-08-11"
    body = {
        "firstname": "Mason",
        "bookingdates": {
            "checkin": "2026-08-02",
            "checkout": "2026-08-11"
        }
    }
    patch_response = api_client.patch_request("/booking/4097", body=body, token=auth)
    assert patch_response.status_code == 200
    assert patch_response.json()["firstname"] == "Mason"
    assert patch_response.json()["bookingdates"]["checkin"] == "2026-08-02"
    assert patch_response.json()["bookingdates"]["checkout"] == "2026-08-11"

    get_response = api_client.get_request("/booking/4097")
    assert get_response.json()["firstname"] == "Mason"
    assert get_response.json()["bookingdates"]["checkin"] == "2026-08-02"
    assert get_response.json()["bookingdates"]["checkout"] == "2026-08-11"


def test_partial_booking_update_unsuccessful(api_client):
    body = {
        "firstname": "Mason",
        "bookingdates": {
            "checkin": "2026-08-02",
            "checkout": "2026-08-11"
        }
    }
    patch_response = api_client.patch_request("/booking/4097", body=body)
    assert patch_response.status_code == 403


def test_delete_booking(api_client, auth):
    body = {
        "firstname": "Delete",
        "lastname": "Brown",
        "totalprice": 11204,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-10"
        },
        "additionalneeds": "Breakfast"
    }
    post_response = api_client.post_request("/booking", body=body)
    assert post_response.status_code == 200
    assert post_response.json()["booking"]["firstname"] == "Delete"

    booking_id = post_response.json()["bookingid"]

    get_response = api_client.get_request(f"/booking/{booking_id}")
    assert get_response.status_code == 200

    delete_response = api_client.delete_request(f"/booking/{booking_id}", token=auth)
    assert delete_response.status_code == 201

    get_response = api_client.get_request(f"/booking/{booking_id}")
    assert get_response.status_code == 404


def test_delete_booking_without_token(api_client):
    body = {
        "firstname": "Delete",
        "lastname": "Brown",
        "totalprice": 11204,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-08-01",
            "checkout": "2026-08-10"
        },
        "additionalneeds": "Breakfast"
    }
    post_response = api_client.post_request("/booking", body=body)
    booking_id = post_response.json()["bookingid"]

    delete_response = api_client.delete_request(f"/booking/{booking_id}")
    assert delete_response.status_code == 403
