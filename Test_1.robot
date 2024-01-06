*** Settings ***
Library    String

*** Variables ***
${xpath_1}    //div[text()='{key_to_replace}']//div[contains(@class,'dummy_class')]//following-sibling::div[text()='{value_to_replace}']
&{dropdown_item}    Country=India
${v}    India


*** Test Cases ***
Test_Locator
    Create Dynamic Xpath    ${xpath_1}    ${dropdown_item}    replace_single_value=False
    Create Dynamic Xpath    //div[text()='{value_to_replace}']    ${v}    

*** Keywords ***
Create Dynamic Xpath
    [Arguments]    ${xpath}    ${values_to_replace}    ${replace_single_value}=True
    IF    not ${replace_single_value}
        FOR    ${key}    ${value}    IN    &{values_to_replace}
            ${final_xpath}=    Replace String    ${xpath}    {value_to_replace}    ${value} 
            ${final_xpath}=    Replace String    ${final_xpath}    {key_to_replace}    ${key}
        END
    ELSE
        ${final_xpath}=    Replace String    ${xpath}    {value_to_replace}    ${values_to_replace}  
    END
    Log To Console    ${final_xpath}
    RETURN    ${final_xpath}
