import rdflib


class XSDreg:
    """A simple library to obtain regular expressions for xsd types used in rdf"""
    # source of relevant xsd types https://www.w3.org/TR/rdf11-concepts/
    # source: for most regex is https://www.w3.org/TR/xmlschema11-2/#[name]

    def __init__(self):
        self.stringRegex = "[\\s\\S]+"

        self.dateRegex = "-?([1-9][0-9]{3,}|0[0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?"

        self.timeRegex = "(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\\.[0-9]+)?|(24:00:00(\\.0+)?))(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?"

        self.dateTimeRegex = "-?([1-9][0-9]{3,}|0[0-9]{3})-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])T(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\\.[0-9]+)?|(24:00:00(\\.0+)?))(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?"

        self.dateTimeStampRegex = ".*(Z|(\\+|-)[0-9][0-9]:[0-9][0-9])"

        self.integerRegex = "[\\-+]?[0-9]+"

        self.decimalRegex = "(\\+|-)?([0-9]+(\\.[0-9]*)?|\\.[0-9]+)"

        self.floatRegex = "(\\+|-)?([0-9]+(\\.[0-9]*)?|\\.[0-9]+)([Ee](\\+|-)?[0-9]+)?|(\\+|-)?INF|NaN"

        self.doubleRegex = "(\\+|-)?([0-9]+(\\.[0-9]*)?|\\.[0-9]+)([Ee](\\+|-)?[0-9]+)? |(\\+|-)?INF|NaN"

        self.booleanRegex = "true|false|0|1"

        self.gYearRegex = "-?([1-9][0-9]{3,}|0[0-9]{3})(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?"

        self.gMonthRegex = "--(0[1-9]|1[0-2])(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?"

        self.gDayRegex = "---(0[1-9]|[12][0-9]|3[01])(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?"

        self.gYearMonthRegex = "-?([1-9][0-9]{3,}|0[0-9]{3})-(0[1-9]|1[0-2])(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?"

        self.gMonthDayRegex = "--(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])(Z|(\\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?"

        self.durationRegex = "-?P[0-9]+Y?([0-9]+M)?([0-9]+D)?(T([0-9]+H)?([0-9]+M)?([0-9]+(\.[0-9]+)?S)?)?"

        self.yearMonthDurationRegex = "-?P((([0-9]+Y)([0-9]+M)?)|([0-9]+M))"

        self.dayTimeDurationRegex = "[^YM]*[DT].*"

        self.byteRegex = "-128|[\\-+]?12[0-7]|[\\-+]?1[01][0-9]|[\\-+]?[1-9][0-9]|[\\-+]?[0-9]"

        self.shortRegex = "0|-32768|[\\-+]?3276[0-7]|[\\-+]?327[0-5][0-9]|[\\-+]?32[0-6][0-9]{2}|[\\-+]?3[01][0-9]{3}|[\\-+]?[12][0-9]{4}|[\\-+]?[1-9][0-9]{0,3}"

        self.intRegex = ""

        self.longRegex = ""

        self.unsignedByteRegex = ""

        self.unsignedShortRegex = ""

        self.unsignedIntRegex = ""

        self.unsignedLongRegex = ""

        self.positiveIntegerRegex = ""

        self.nonNegativeIntegerRegex = ""

        self.negativeIntegerRegex = ""

        self.nonPositiveIntegerRegex = ""

        self.hexBinaryRegex = ""

        self.base64BinaryRegex = ""

        self.xsd = rdflib.Namespace('http://www.w3.org/2001/XMLSchema#')

        self.map = {
                str(self.xsd.string) : self.stringRegex, str(self.xsd.boolean) : self.booleanRegex,
                str(self.xsd.decimal) : self. decimalRegex, str(self.xsd.integer) : self.integerRegex,
                str(self.xsd.double) : self.doubleRegex, str(self.xsd.float) : self.floatRegex,
                str(self.xsd.date) : self.dateRegex, str(self.xsd.time) : self.timeRegex,
                str(self.xsd.dateTime) : self.dateTimeRegex,
                str(self.xsd.dateTimeStamp) : self.dateTimeStampRegex, str(self.xsd.gYear) : self.gYearRegex,
                str(self.xsd.gMonth) : self.gMonthRegex, str(self.xsd.gDay) :self.gDayRegex,
                str(self.xsd.gYearMonth) : self.gYearMonthRegex, str(self.xsd.gMonthDay) : self.gMonthDayRegex,
                str(self.xsd.duration) : self.durationRegex,
                str(self.xsd.yearMonthDuration) : self.yearMonthDurationRegex,
                str(self.xsd.dayTimeDuration) : self.dayTimeDurationRegex,
                str(self.xsd.byte) : self.byteRegex
               }

    def getRegex(self, xsdURI):
        return self.map[xsdURI]
