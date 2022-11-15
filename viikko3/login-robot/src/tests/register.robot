*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  test  testpassword123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  test  12dddregfrgsgds
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  ev  password12312
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  eerotesti  pass
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  eerotesti  passasssasssa
    Output Should Contain  Password cannot contain only letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  test  testpassword123
    Input New Command
