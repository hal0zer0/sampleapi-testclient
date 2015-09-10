Feature: get all the widgets
  Scenario: run GET command to /widgets
    Given we have the widget URL
    when we send the request
    then we will get a collection back
    and they will have the right properties
    and they will return an array in the items field
