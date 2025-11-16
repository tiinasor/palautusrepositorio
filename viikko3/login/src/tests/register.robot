*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  newuser
    Set Password  password123
    Set Password Confirmation  password123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ab
    Set Password  password123
    Set Password Confirmation  password123
    Submit Credentials
    Registration Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  validuser
    Set Password  pass12
    Set Password Confirmation  pass12
    Submit Credentials
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  validuser
    Set Password  onlyletters
    Set Password Confirmation  onlyletters
    Submit Credentials
    Registration Should Fail With Message  Password must contain non-alphabetic characters

Register With Nonmatching Password And Password Confirmation
    Set Username  validuser
    Set Password  password123
    Set Password Confirmation  password456
    Submit Credentials
    Registration Should Fail With Message  Password and password confirmation do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  password123
    Set Password Confirmation  password123
    Submit Credentials
    Registration Should Fail With Message  Username is already taken

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Credentials
    Click Button  Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Welcome Page Should Be Open
    Title Should Be  Welcome to Ohtu Application!

Register Page Should Be Open
    Title Should Be  Register

Go To Register Page
    Go To  ${REGISTER_URL}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
