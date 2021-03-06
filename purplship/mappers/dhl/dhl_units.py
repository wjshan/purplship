from enum import Enum, Flag
from purplship.domain.Types.units import PackagingUnit


""" DHL Native Types/Units """


class Dimension(Enum):
    CM = "C"
    IN = "I"


class DeliveryType(Enum):
    Door_to_Door = "DD"
    Door_to_Airport = "DA"
    Airport_to_Airport = "AA"
    Door_to_Door_C = "DC"


class DCTPackageType(Enum):
    Flyer_Smalls = "FLY"
    Parcels_Conveyables = "COY"
    Non_conveyables = "NCY"
    Pallets = "PAL"
    Double_Pallets = "DBL"
    Parcels = "BOX"

    """ Unified Packaging type mapping """
    SM = Flyer_Smalls
    BOX = Parcels
    PC = Non_conveyables
    PAL = Pallets


class PackageType(Flag):
    Jumbo_Document = "BD"
    Jumbo_Parcel = "BP"
    Customer_provided = "CP"
    Document = "DC"
    DHL_Flyer = "DF"
    Domestic = "DM"
    Express_Document = "ED"
    DHL_Express_Envelope = "EE"
    Freight = "FR"
    Jumbo_box = "JB"
    Jumbo_Junior_Document = "JD"
    Junior_jumbo_Box = "JJ"
    Jumbo_Junior_Parcel = "JP"
    Other_DHL_Packaging = "OD"
    Parcel = "PA"
    Your_packaging = "YP"

    """ Unified Packaging type mapping """
    SM = Document
    BOX = Parcel
    PC = Your_packaging
    PAL = Freight


class Product(Enum):
    LOGISTICS_SERVICES = "0"
    DOMESTIC_EXPRESS_12_00 = "1"
    # B2C                     =    "2"
    B2C = "3"
    JETLINE = "4"
    SPRINTLINE = "5"
    # EXPRESS_EASY            =    "7"
    EXPRESS_EASY = "8"
    EUROPACK_DOC = "9"
    AUTO_REVERSALS = "A"
    BREAKBULK_EXPRESS = "B"
    MEDICAL_EXPRESS_DOC = "C"
    EXPRESS_WORLDWIDE_DOC = "D"
    EXPRESS_9_00 = "E"
    FREIGHT_WORLDWIDE = "F"
    DOMESTIC_ECONOMY_SELECT = "G"
    ECONOMY_SELECT = "H"
    DOMESTIC_EXPRESS_9_00 = "I"
    JUMBO_BOX = "J"
    EXPRESS_9_00_DOC = "K"
    # EXPRESS_10_30           =    "L"
    EXPRESS_10_30 = "M"
    DOMESTIC_EXPRESS = "N"
    DOMESTIC_EXPRESS_10_30 = "O"
    EXPRESS_WORLDWIDE = "P"
    MEDICAL_EXPRESS = "Q"
    GLOBALMAIL_BUSINESS = "R"
    SAME_DAY = "S"
    EXPRESS_12_00_DOC = "T"
    EXPRESS_WORLDWIDE_U = "U"
    EUROPACK = "V"
    ECONOMY_SELECT_DOC = "W"
    EXPRESS_ENVELOPE = "X"
    EXPRESS_12_00 = "Y"
    Destination_Charges = "Z"


class PayorType(Enum):
    SENDER = "S"
    RECIPIENT = "R"
    THIRD_PARTY = "T"


class Service(Enum):
    Logistics_Services = "0A"
    Mailroom_Management = "0B"
    Pallet_Administration = "0C"
    Warehousing = "0D"
    Express_Logistics_Centre = "0E"
    Strategic_Parts_Centre = "0F"
    Local_Distribution_Centre = "0G"
    Terminal_Handling = "0H"
    Cross_Docking = "0I"
    Inventory_Management = "0J"
    Loading_Unloading = "0K"
    Product_Kitting = "0L"
    Priority_Account_Desk = "0M"
    Document_Archiving = "0N"
    Saturday_Delivery = "AA"
    Saturday_Pickup = "AB"
    Holiday_Delivery = "AC"
    Holiday_Pickup = "AD"
    Domestic_Saturday_Delivery = "AG"
    Standard = "BA"
    Globalmail_Item = "BB"
    Letter = "BC"
    Packet = "BD"
    Letter_Plus = "BE"
    Packet_Plus = "BF"
    Elevated_Risk = "CA"
    Restricted_Destination = "CB"
    Security_Validation = "CC"
    Secure_Protection = "CD"
    Proof_of_Identity = "CE"
    Secure_Storage = "CF"
    Diplomatic_Material = "CG"
    Smart_Sensor = "CH"
    Visa_Program = "CI"
    Onboard_Courier = "CJ"
    Secure_Safebox = "CK"
    Smart_Sentry = "CL"
    Split_Duties_and_Tax = "DC"
    Duties_and_Taxes_Paid = "DD"
    Receiver_Paid = "DE"
    Duties_and_Taxes_Unpaid = "DS"
    Import_Billing = "DT"
    Importer_of_Record = "DU"
    GoGreen_Carbon_Neutral = "EA"
    GoGreen_Carbon_Footprint = "EB"
    GoGreen_Carbon_Estimate = "EC"
    Fuel_Surcharge_B = "FB"
    Fuel_Surcharge_C = "FC"
    Fuel_Surcharge_F = "FF"
    Smartphone_Box = "GA"
    Laptop_Box = "GB"
    Bottle_Box = "GC"
    Repacking = "GD"
    Tablet_Box = "GE"
    Filler_Material = "GF"
    Packaging = "GG"
    Diplomatic_Bag = "GH"
    Pallet_Box = "GI"
    Lock_Box = "GJ"
    Lithium_Ion_PI965_Section_II = "HB"
    Dry_Ice_UN1845 = "HC"
    Lithium_Ion_PI965_966_Section_II = "HD"
    Dangerous_Goods = "HE"
    Perishable_Cargo = "HG"
    Excepted_Quantity = "HH"
    Spill_Cleaning = "HI"
    Consumer_Commodities = "HK"
    Limited_Quantities_ADR = "HL"
    Lithium_Metal_PI969_Section_II = "HM"
    ADR_Load_Exemption = "HN"
    Lithium_Ion_PI967_Section_II = "HV"
    Lithium_Metal_PI970_Section_II = "HW"
    Biological_UN3373 = "HY"
    Extended_Liability = "IB"
    Contract_Insurance = "IC"
    Shipment_Insurance = "II"
    Delivery_Notification = "JA"
    Pickup_Notification = "JC"
    Proactive_Tracking = "JD"
    Performance_Reporting = "JE"
    Prealert_Notification = "JY"
    Change_of_Billing = "KA"
    Cash_On_Delivery = "KB"
    Printed_Invoice = "KD"
    Waybill_Copy = "KE"
    Import_Paperwork = "KF"
    Payment_on_Pickup = "KY"
    Shipment_Intercept = "LA"
    Shipment_Redirect = "LC"
    Storage_at_Facility = "LE"
    Cold_Storage = "LG"
    Specific_Routing = "LH"
    Service_Recovery = "LV"
    Alternative_Address = "LW"
    Hold_for_Collection = "LX"
    Address_Correction_A = "MA"
    Address_Correction_B = "MB"
    Neutral_Delivery = "NN"
    Remote_Area_Pickup = "OB"
    Remote_Area_Delivery_C = "OC"
    Out_of_Service_Area = "OE"
    Remote_Area_Delivery_O = "OO"
    Shipment_Preparation = "PA"
    Shipment_Labeling = "PB"
    Shipment_Consolidation = "PC"
    Relabeling_Data_Entry = "PD"
    Preprinted_Waybill = "PE"
    Piece_Labelling = "PS"
    Data_Staging_03 = "PT"
    Data_Staging_06 = "PU"
    Data_Staging_12 = "PV"
    Data_Staging_24 = "PW"
    Standard_Pickup = "PX"
    Scheduled_Pickup = "PY"
    Dedicated_Pickup = "QA"
    Early_Pickup = "QB"
    Late_Pickup = "QD"
    Residential_Pickup = "QE"
    Loading_Waiting = "QF"
    Bypass_Injection = "QH"
    Direct_Injection = "QI"
    Drop_Off_at_Facility = "QY"
    Delivery_Signature = "SA"
    Content_Signature = "SB"
    Named_Signature = "SC"
    Adult_Signature = "SD"
    Contract_Signature = "SE"
    Alternative_Signature = "SW"
    No_Signature_Required = "SX"
    Dedicated_Delivery = "TA"
    Early_Delivery = "TB"
    Time_Window_Delivery = "TC"
    Evening_Delivery = "TD"
    Delivery_on_Appointment = "TE"
    Return_Undeliverable = "TG"
    Swap_Delivery = "TH"
    Unloading_Waiting = "TJ"
    Residential_Delivery = "TK"
    Repeat_Delivery = "TN"
    Alternative_Date = "TT"
    No_Partial_Delivery = "TU"
    Service_Point_24_7 = "TV"
    Pre_9_00 = "TW"
    Pre_10_30 = "TX"
    Pre_12_00 = "TY"
    Thermo_Packaging = "UA"
    Ambient_Vialsafe = "UB"
    Ambient_Non_Insulated = "UC"
    Ambient_Insulated = "UD"
    Ambient_Extreme = "UE"
    Chilled_Box_S = "UF"
    Chilled_Box_M = "UG"
    Chilled_Box_L = "UH"
    Frozen_No_Ice_S = "UI"
    Frozen_No_Ice_M = "UJ"
    Frozen_No_Ice_L = "UK"
    Frozen_Ice_Sticks_S = "UL"
    Frozen_Ice_Sticks_M = "UM"
    Frozen_Ice_Sticks_L = "UN"
    Frozen_Ice_Plates_S = "UO"
    Frozen_Ice_Plates_M = "UP"
    Frozen_Ice_Plates_L = "UQ"
    Combination_No_Ice = "UR"
    Combination_Dry_Ice = "US"
    Frozen_Ice_Sticks_E = "UT"
    Frozen_Ice_Plates_E = "UV"
    Customer_TCP_1 = "UW"
    Thermo_Accessories = "VA"
    Absorbent_Sleeve = "VB"
    Cooland_Wrap = "VC"
    Dry_Ice_Supplies = "VD"
    Pressure_Bag_S = "VE"
    Pressure_Bag_M = "VF"
    Pressure_Bag_L = "VG"
    Informal_Clearance = "WA"
    Formal_Clearance = "WB"
    Payment_Deferment = "WC"
    Clearance_Authorization = "WD"
    Multiline_Entry = "WE"
    Post_Clearance_Modification = "WF"
    Handover_to_Broker = "WG"
    Physical_Intervention = "WH"
    Bio_Phyto_Veterinary_Controls = "WI"
    Obtaining_Permits_and_Licences = "WJ"
    Bonded_Storage = "WK"
    Bonded_Transit_Documents = "WL"
    Temporary_Import_Export = "WM"
    Under_Bond_Guarantee = "WN"
    Export_Declaration = "WO"
    Exporter_Validation = "WP"
    Certificate_of_Origin = "WQ"
    Document_Translation = "WR"
    Personal_Effects = "WS"
    Paperless_Trade = "WY"
    Import_Export_Taxes = "XB"
    Unrecoverable_Origin_Tax = "XC"
    Quarantine_Inspection = "XD"
    Merchandise_Process = "XE"
    Domestic_Postal_Tax = "XF"
    Tier_Two_Tax = "XG"
    Tier_Three_Tax = "XH"
    Import_Penalty = "XI"
    Cargo_Zone_Process = "XJ"
    Import_Export_Duties = "XX"
    Premium_09_00 = "Y1"
    Premium_10_30 = "Y2"
    Premium_12_00 = "Y3"
    Over_Sized_Piece_B = "YB"
    Over_Handled_Piece_C = "YC"
    Multipiece_Shipment = "YE"
    Over_Weight_Piece_F = "YF"
    Over_Sized_Piece_G = "YG"
    Over_Handled_Piece_H = "YH"
    Premium_9_00_I = "YI"
    Premium_10_30_J = "YJ"
    Premium_12_00_K = "YK"
    Paket_Shipment = "YV"
    Breakbulk_Mother = "YW"
    Breakbulk_Baby = "YX"
    Over_Weight_Piece_Y = "YY"
    Customer_Claim = "ZA"
    Damage_Compensation = "ZB"
    Loss_Compensation = "ZC"
    Customer_Rebate = "ZD"
    eCom_Discount = "ZE"


class WeightUnit(Enum):
    KG = "K"
    LB = "L"
