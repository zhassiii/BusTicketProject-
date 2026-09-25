import csv
class ticketCategory:
    def __init__(this,code, title, desc):
        this.title = title
        this.code = code
        this.description = desc
        this.topupTypes = []
    def getTitle(this):
        return this.title
    def getDescription(this):
        return this.description
    def getTopupTypes(this):
        return this.topupTypes
    def addTopup(this, topUpCategory):
        this.topupTypes.append(topUpCategory)
    def findTopupTypesByName(this, topupName):
        #Checks the needed top-up and returns it
        for topupType in this.topupTypes:
            if topupName in topupType.title:
                return topupType


class TopUpCategory:
    def __init__(this, title, price, passengerClassName, desc, quantity, entitlementType, entitlementUnit, entitlementvalue):
        this.title = title
        this.price = float(price)
        this.passengerClassName = passengerClassName
        this.description = desc
        this.quantity = quantity
        this.entitlementtype = entitlementType
        this.entitlementunit = entitlementUnit
        this.entitlementvalue = entitlementvalue
    def getPriceinPoundAndPence(this):
        priceinPounds = this.price / 100
        return priceinPounds
    def getTitle(this):
        return this.title
    def chosenTopup(this):
        priceInPounds = this.getPriceinPoundAndPence()
        return(this.title + "\n" + this.description + "\n" + "Price in pounds: " + f'{priceInPounds}')
    def getTicketsPurchased(this):
        return this.quantity

#Opening the csv file
def csvRead():
    filename = "mobile_products.csv"
    categoryList = []
    categoryObjectList = []
    topUpObjectList = []
    with open(filename, mode='r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for lines in csv_reader:
            thisTopUp = TopUpCategory(lines["topup_title"],
                                                 lines["topup_price_in_pence"],
                                                 lines["topup_passenger_class_name"],
                                                 lines["topup_description"],
                                                 lines["topup_passenger_class_quantity"],
                                                 lines["topup_entitlement_type"],
                                                 lines["topup_entitlement_unit"],
                                                 lines["topup_entitlement_value"])
            categoryList.append(thisTopUp)
            topUpObjectList.append(thisTopUp)
            #Stores unique names of category titles into a list
            if lines["category_title"] not in categoryList:
                categoryList.append(lines["category_title"])
                thisCategory = ticketCategory(lines["category_id"],
                                                            lines["category_title"],
                                                            lines["category_description"])
                categoryObjectList.append(thisCategory)
                thisCategory.topupTypes.append(thisTopUp)
            else:
                for category in categoryObjectList:
                    if category.getTitle() == lines["category_title"]:
                        category.topupTypes.append(thisTopUp)
                        break
    return categoryObjectList, topUpObjectList
#Function that specifies which exactly ticket the customer wants when picked grouprider and network grouprider
def specTicket(topUpResp, eligibility):
    filename = "mobile_products.csv"
    with open(filename, mode='r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for line in csv_reader:
            if line["topup_title"] == topUpResp and line["topup_passenger_class_name"] == eligibility:
                return line
        return None
