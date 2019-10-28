import sys


class SetUp:
    """Contains supporting functions that are mostly class based"""

    def __init__(self):
        pass

    @classmethod
    def get_input_filename(cls):
        """gets input file name from the command line and returns the name"""
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-i' and i < (len(sys.argv) - 1):
                inputFileName = sys.argv[i + 1]

        return inputFileName

    @classmethod
    def get_output_filename(cls):
        """gets output filename from the command line and returns the name"""
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-o' and i < (len(sys.argv) - 1):
                outputFileName = sys.argv[i + 1]

        return outputFileName

    @classmethod
    def import_data_file(cls):
        """gets file name from the command line and then downloads the input file and :returns the list"""
        for i in range(len(sys.argv)):
            if sys.argv[i] == '-i' and i < (len(sys.argv) - 1):
                inputFileName = sys.argv[i + 1]

        try:
            instructions = [line.rstrip() for line in open(inputFileName, 'r')]
        except IOError:
            print("Could not open input file, is path correct?")

        return instructions

    @classmethod
    def imm_bit_to_32_bit_converter(cls, num, bitsize):
        """Converts binaries of various lengths to a standard 32 bit length and :returns the converted number"""
        # TODO make the machine instruction into a 32 bit int.
        if bitsize == 6:  # for CB format

            negBitMask = 0x20  # figure out if 19 bit num is neg
            extendMask = 0xFFFFFFC0

            if (negBitMask & num) > 0:  # is it?
                num = num | extendMask  # if so extend with 1's
                num = num ^ 0xFFFFFFFF  # 2s comp
                num = num + 1
                num = num * -1  # add neg
            else:
                num = num | 0x00000000

        elif bitsize == 19:  # for CB format

            negBitMask = 0x40000  # figure out if 19 bit num is neg
            extendMask = 0xFFF80000

            if (negBitMask & num) > 0:  # is it?
                num = num | extendMask  # if so extend with 1's
                num = num ^ 0xFFFFFFFF  # 2s comp
                num = num + 1
                num = num * -1  # add neg
            else:
                num = num | 0x00000000

        elif bitsize == 12:  # for I format

            negBitMask = 0x800  # figure out if 12 bit num is neg
            extendMask = 0xFFFFF000

            if (negBitMask & num) > 0:  # is it?
                num = num | extendMask  # if so extend with 1's
                num = num ^ 0xFFFFFFFF  # 2s comp
                num = num + 1
                num = num * -1  # add neg
            else:
                num = num | 0x00000000

        elif bitsize == 16:  # for IM format

            negBitMask = 0x8000
            extendMask = 0xFFFF0000

            if (negBitMask & num) > 0:  # is it?
                num = num | extendMask  # if so extend with 1's
                num = num ^ 0xFFFFFFFF  # 2s comp
                num = num + 1
                num = num * -1  # add neg
            else:
                num = num | 0x00000000

        elif bitsize == 26:  # for B format

            negBitMask = 0x2000000
            extendMask = 0xFE000000

            if (negBitMask & num) > 0:  # is it?
                num = num | extendMask  # if so extend with 1's
                num = num ^ 0xFFFFFFFF  # 2s comp
                num = num + 1
                num = num * -1  # add neg
            else:
                num = num | 0x00000000

        else:
            print("You are using an INVALID bit length")

        return num

    @classmethod
    def bin2StringSpaced(cls, s):
        spacedStr = s[0:8] + " " + s[8:11] + " " + s[11:16] + " " + s[16:21] + " " + s[21:26] + " " + s[26:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedD(cls, s):
        spacedStr = s[0:11] + " " + s[11:20] + " " + s[20:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedIM(cls, s):
        spacedStr = s[0:10] + " " + s[10:12] + " " + s[12:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedCB(cls, s):
        spacedStr = s[0:8] + " " + s[8:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedI(cls, s):
        spacedStr = s[0:10] + " " + s[10:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedR(cls, s):
        spacedStr = s[0:11] + " " + s[11:16] + " " + s[16:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedB(cls, s):
        spacedStr = s[0:6] + " " + s[6:32]
        return spacedStr

    @classmethod
    def imm_32_bit_unsigned_to_32_bit_signed_converter(cls, num):
        """converts 32 bit signed, handles negative numbers, returns number"""
        # TODO unsigned is always unsigned, is it supposed to be negative

        negBitMask = 0x80000000

        if (negBitMask & num) > 0:
            num = num ^ 0xFFFFFFFF  # 2s comp
            num = num + 1
            num = num * -1  # add neg

        return num  # eventually convert this to decimal for display

    @classmethod
    def decimalToBinary(cls, num):
        """This function converts decimal number to binary and prints it"""
        if num > 1:
            cls.decimalToBinary(num // 2)
        print(num % 2, end='')

    @classmethod
    def binaryToDecimal(cls, binary):
        print("\n")
        print(int(binary, 2))
