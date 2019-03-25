

class XSDreg:
    """A simple library to obtain regular expressions for xsd types used in rdf"""
    # source of relevant xsd types https://www.w3.org/TR/rdf11-concepts/

    stringRegex = "[\\s\\S]+"

    # source: https://www.w3.org/TR/xmlschema11-2/#date
    dateRegex = "-?([1-9][0-9]{3,}|0[0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?"

    # source: https://www.w3.org/TR/xmlschema11-2/#time
    timeRegex = "(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\\.[0-9]+)?|(24:00:00(\\.0+)?))(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?"

    # source: https://www.w3.org/TR/xmlschema11-2/#dateTime
    dateTimeRegex = "-?([1-9][0-9]{3,}|0[0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\\.[0-9]+)?|(24:00:00(\\.0+)?))(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?"

    # source: https://www.w3.org/TR/xmlschema11-2/#dateTimeStamp
    dateTimeStampRegex = ".*(Z|(\\+|-)[0-9][0-9]:[0-9][0-9])"

    integerRegex = ""

    decimalRegex = ""

    floatRegex = ""

    doubleRegex = ""

    booleanRegex = ""

    gYearRegex = ""

    gMonthRegex = ""

    gDayRegex = ""

    gYearMonthRegex = ""

    gMonthDayRegex = ""

    durationRegex = ""

    yearMonthDurationRegex = ""

    dayTimeDurationRegex = ""

    byteRegex = ""

    shortRegex = ""

    intRegex = ""

    longRegex = ""

    unsignedByteRegex = ""

    unsignedShortRegex = ""

    unsignedIntRegex = ""

    unsignedLongRegex = ""

    positiveIntegerRegex = ""

    nonNegativeIntegerRegex = ""

    negativeIntegerRegex = ""

    nonPositiveIntegerRegex = ""

    hexBinaryRegex = ""

    base64BinaryRegex = ""