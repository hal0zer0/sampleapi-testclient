from behave import *
import requests
import json
import logging

@given('we have the widget url')
def step_impl(context):
    context.url = "http://localhost:3000/widgets"


@when('we send the request')
def step_impl(context):
    assert context.url is not None
    context.data = requests.get(context.url)


@then('we will get a collection back')
def step_impl(context):
    assert context.failed is False
    context.parsed = context.data.json()


@then('they will have the right properties')
def step_impl(context):
    attrs = context.parsed.keys()
    assert "href" in attrs
    assert "timestamp" in attrs


@then('they will return an array in the items field')
def step_impl(context):
    assert type(context.parsed['items']) is list
