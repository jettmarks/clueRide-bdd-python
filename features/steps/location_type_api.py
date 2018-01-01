from behave import *
import requests

use_step_matcher("re")

api_url = 'https://player-test.clueride.com/rest/location/types'
response = None
auth_headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsImJhZGdlcyI6W10sImVtYWlsIjoidGVzdC5lbWFpbEBjbHVlcmlkZS5jb20iLCJndWVzdCI6ZmFsc2UsInR5cCI6IkpXVCJ9.eyJpc3MiOiJjbHVlcmlkZS5jb20iLCJqdGkiOiJpdmVucGhvZHI4MzBkdWNwOG9pNjhmajBxYyJ9.i-7t4on7g-KrJrxDgjwItnhRyp1N2PcXyk51DR1Ig9A'}


@when("I request Location Types")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    global response
    response = requests.get(api_url, headers=auth_headers)
    code = response.status_code
    assert code == 200, "Got unexpected status code: " + str(code)


def valid_property(object_to_validate, field):
    assert object_to_validate[field] is not None, "Missing " + field


def retrieve_location_types_from_response():
    location_types = response.json()
    assert len(location_types) > 10, "Expected more location types"
    return location_types


@then("I can list out Location Types")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    location_types = retrieve_location_types_from_response()
    for location_type in location_types:
        print(location_type)
        valid_property(location_type, 'id')
        valid_property(location_type, 'name')
        # valid_property(location_type, 'icon')


@then("the two lists match")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    location_types_from_api = retrieve_location_types_from_response()
    location_types_from_select = context.select_list

    expected_size = len(location_types_from_api)
    actual_size = len(location_types_from_select)
    assert actual_size == expected_size, "Expected " + str(expected_size) + " but got " + str(actual_size)

