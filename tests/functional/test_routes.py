import os
import pytest


@pytest.mark.parametrize("routes", [
    "/",
    "/portfolio",
    "/contact"
])
def test_all_routes_return_200_response(test_client, routes):
    """
    GIVEN a Flask application running in test mode
    WHEN each available route is requested (via GET)
    THEN check for a 200 response code.
    """
    res = test_client.get(routes)
    assert res.status_code == 200


@pytest.mark.parametrize("name, email, subject, message", [
    ("", "", "", ""),
    ("test", "", "", ""),
    ("", os.environ["DUMMY_MAIL_USERNAME"], "", ""),
    ("", "", "testing", ""),
    ("", "", "", "test")
])
def test_redirect_route_when_form_is_incorrectly_submitted(test_client, name, email, subject, message):
    """
    GIVEN a Flask application running in test mode
    WHEN /contact route is requested (via POST) 
    AND the form is incorrectly submitted
    THEN check for a 302 response code
    """

    res = test_client.post("/contact",
    data=dict(name=name, email=email, subject=subject, message=message)
    )

    assert res.status_code == 302


@pytest.mark.parametrize("name, email, subject, message", [
    ("test", os.environ["DUMMY_MAIL_USERNAME"], "testing", "test")
])
def test_200_response_when_form_is_correctly_submitted(test_client, name, email, subject, message):
    """
    GIVEN a Flask application running in test mode
    WHEN /contact route is requested (via POST)
    AND the form is correctly submitted
    THEN check for a 200 response code
    """

    res = test_client.post("/contact",
    data=dict(name=name, email=email, subject=subject, message=message)
    )

    assert res.status_code == 200


@pytest.mark.parametrize("name, email, subject, message", [
    ("test", os.environ["DUMMY_MAIL_USERNAME"], "testing", "test")
])
def test_200_response_when_new_template_created_after_form_is_submitted(test_client, name, email, subject, message):
    """
    GIVEN a Flask application running in test mode
    WHEN /submit route is requested (via POST)
    THEN check for a 200 response code
    """
    res = test_client.post("/contact",
    data=dict(name=name, email=email, subject=subject, message=message)
    )
    res.location = "/submit"
    assert res.status_code == 200