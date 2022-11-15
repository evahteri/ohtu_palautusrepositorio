*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  markus
    Set Password  markus123
    Set Password Confirmation  markus123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ma
    Set Password  markus123
    Set Password Confirmation  markus123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  eero
    Set Password  dd
    Set Password Confirmation  dd
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  andrew
    Set Password  gregor123www
    Set Password Confirmation  grager445wwwwww
    Submit Credentials
    Register Should Fail With Message  Password confirmation does not match password

Login After Successful Registration
    Set Username  matias
    Set Password  Gohaf222kkal
    Set Password Confirmation  Gohaf222kkal
    Submit Credentials
    Go To Login Page
    Set Username  matias
    Set Password  Gohaf222kkal
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  ma
    Set Password  markus123
    Set Password Confirmation  markus123
    Submit Credentials
    Go To Login Page
    Set Username  ma
    Set Password  markus123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}
