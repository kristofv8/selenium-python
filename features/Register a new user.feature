Feature: Registering a new user
  User opens page, go to create account functionality, fills in form with invalid credentials and sees an error message


  Scenario: User is not able to make a new account using invalid credentials and sees an error message
    Given User clicks Sign in and after that Create An Account Button
    When  User fills in input fields with invalid email value, valid password, accept Terms Of Service and clicks Create An Account button
    Then  User sees a message about invalid email
    When  User fills in input field with valid email value, doesnt fill in password, accept Terms Of Service and clicks Create An Account button
    Then  User sees message that password  value is required
    When  User fills in input fields with valid email value, valid password, doesnt accept Terms Of Service and clicks Create An Account button
    Then  User sees message that accept Terms Of Service is required
    When  User doesnt fill in email, password, doesnt accept Terms Of Service
    Then  User sees that all values are required