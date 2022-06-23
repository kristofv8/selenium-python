Feature: Making an order
  Verified user is able to log in, choose a shelf,order, pay for it and gets a confirmation

  Scenario: Successful order
    Given User logs in to his account "spacestar@mailinator.com", "123Joetylko456"
    Then  Clicks Products in main menu and choose All Storage Solutions
    Then  Goes to Products Page selects second Bookcase and clicks Add To Cart and Checkout buttons
    Then  User fills in Delivery Form with his credentials, "Joe", "Joey", "112", "76-220", "Bedziechowo", "spacestar@mailinator.com", "+48 69 797 3415" etc. and clicks Continue To Payment button
    Then  Choose payment method, fills in payment details "5555 4444 3333 1111", "joe", "03", "2030", "737" and clicks Continue and after that Payment button
    Then User is able to see discount information close it, and goes to Confirmation Page
