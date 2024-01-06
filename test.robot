*** Settings ***
Library    Collections
Library    String

*** Variables ***
@{stocks}    Apple    Meta    AT&T    
@{prices}    123    678    222
&{dict1}    a=3    b=4    c=2
&{dict2}    e=10    f=41    g=21

*** Test Cases ***
TC_01_Test
    Create Dictionary From Two Lists

*** Keywords ***
Create Dictionary From Two Lists
    ${new_dict}=    Evaluate    {stock:price for stock, price in zip(${stocks}, ${prices})}
    Log To Console    ${new_dict}
    ${merge}=    Evaluate    {**${dict1},**${dict2}}
    Log To Console   ${merge}
    
