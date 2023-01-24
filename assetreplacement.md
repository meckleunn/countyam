# Asset Replacement Schema
In order to successfully discuss this issue, a context needs to be established for replacing of assets and historical trends.

Note that this report is writen for use with Python, due to author's understanding of the language. 

## Historical Timeline
Previous to the talks of Asset Management philosophy, assets were replaced on a set schedule. 

Meaning that;
```python
def replacement(Vehicle, Replacement_Years, Purchase_Year):
    Replacement_Year = Purchase_Year + Replacement_Years
    return Replacement_Year

Vehicle = input("Enter the vehicle name: ") # prompt for vehicle
Replacement_Years = int(input("Enter the replacement years in policy: ")) # prompt for policy year
Purchase_Year = int(input("Enter the purchase year: ")) # prompt for year of vehicle purchase

`print("The replacement year for the",Vehicle,"purchased in",Purchase_Year,"is:",replacement(Vehicle, Replacement_Years, Purchase_Year))`
```
#### Managerial / Asset Owner Adjustment
As our asset management philosophy grew, even at the start of understanding. The County was replacing of assets either to quickly, or to late. In the time of discussions around budgeting, managers then provided an input to adjustment of the return year based on a `manager adjustment`.

```python
def replacement(Vehicle, Replacement_Years, Purchase_Year):
    """Calculates the replacement year for a vehicle based on the purchase year and the replacement years in policy"""
    Replacement_Year = Purchase_Year + Replacement_Years
    return Replacement_Year

def manager_adjustment(Replacement_Year, Manager_Adjustment):
    """Calculates the adjusted replacement year for a vehicle based on the replacement year and the manager adjustment"""
    Adjusted_Replacement_Year = Replacement_Year + Manager_Adjustment
    return Adjusted_Replacement_Year

Vehicle = input("Enter the vehicle name: ")
Replacement_Years = int(input("Enter the replacement years in policy: "))
Purchase_Year = int(input("Enter the purchase year: "))

Replacement_Year = replacement(Vehicle, Replacement_Years, Purchase_Year)
print("The replacement year for the",Vehicle,"purchased in",Purchase_Year,"is:",Replacement_Year)

Manager_Adjustment_Necessary = input("Is a manager adjustment necessary? (yes/no): ").lower()
if Manager_Adjustment_Necessary == "yes":
    Manager_Adjustment = int(input("Enter the manager adjustment (enter a positive or negative integer): "))
    Adjusted_Replacement_Year = manager_adjustment(Replacement_Year, Manager_Adjustment)
    print("The adjusted replacement year for the",Vehicle,"purchased in",Purchase_Year,"is:",Adjusted_Replacement_Year)
elif Manager_Adjustment_Necessary == "no":
    print("The replacement year for the",Vehicle,"purchased in",Purchase_Year,"is:",Replacement_Year)
else:
    print("Invalid input, please enter 'yes' or 'no'")
```
#### Moving Forward 

As the County grows, so does the capability of the data that we have available. Not only in the hands of the County, but at the hands of manufacturers, research data and more. 

To innovate our replacement functionality, it should be determined that an asset is no longer fit for service based on inspections done by mechanical staff. 

```
needs to be defined, maybe using NIST
```
