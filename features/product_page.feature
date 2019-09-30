Feature: checking price, stars and "customers who bought this item also bought" section of a product

    Scenario Outline: User navigates to product page using search
        Given I navigate to the homepage
        And I search for <search_term>
        When I select <product>
        Then The price of the "Audio CD" is <price>
        And The star rating is <rating>
        And The first item in the "customers who bought this item also bought" section is <first_customers_also_bought>

        Examples: I Learned The Hard Way
            | search_term  | product                | price  | rating | first_customers_also_bought    |
            | Sharon Jones | I Learned The Hard Way | £11.59 | 4.5    | Give The People What They Want |