from helpers import SetUp
import os
import masking_constants as MASKS
import sys


class Disassembler:
    #opcode = []
    opcodeStr = []
    instrSpaced = []
    arg1 = []
    arg2 = []
    arg3 = []
    arg1Str = []
    arg2Str = []
    arg3Str = []
    dataval = []
    rawdata = []
    address = []
    numInstructs = 0

    def run(self):

        instructions = []
        instructions = SetUp.import_data_file()

        outputFilename = SetUp.get_output_filename()

        print("raw output filename is ", outputFilename)

        # creates address list with appropriate length
        for i in range(len(instructions)):
            self.address.append(96 + (i * 4))

        opcode = []

        # creates an opcode list by selecting the 11 left most bits
        for z in instructions:
            opcode.append(int(z, base=2) >> 21)

        for i in range(len(opcode)):
            self.numInstructs = self.numInstructs + 1
            """ # R-type """
            if opcode[i] == 1112:  # ADD OPCODE
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ADD")
                self.arg1.append((int(instructions[i], base=2) & MASKS.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKS.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1624:  # SUB OPCODE
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("SUB")
                self.arg1.append((int(instructions[i], base=2) & MASKS.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKS.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1104:  # AND OPCODE
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("AND")
                self.arg1.append((int(instructions[i], base=2) & MASKS.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKS.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1360:  # ORR OPCODE
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ORR")
                self.arg1.append((int(instructions[i], base=2) & MASKS.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKS.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1690:  # LSR OPCODE
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("LSR")
                self.arg1.append((int(instructions[i], base=2) & MASKS.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKS.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))
            elif opcode[i] == 1691:  # LSL OPCODE
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("LSL")
                self.arg1.append((int(instructions[i], base=2) & MASKS.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKS.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))
            elif opcode[i] == 1692:  # ASR OPCODE
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ASR")
                self.arg1.append((int(instructions[i], base=2) & MASKS.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKS.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
            elif opcode[i] == 1872:  # EOR OPCODE
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("EOR")
                self.arg1.append((int(instructions[i], base=2) & MASKS.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & MASKS.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                """# B-Type"""
            elif 160 <= opcode[i] <= 191:  # B OPCODE
                self.instrSpaced.append(SetUp.bin2StringSpacedB(instructions[i]))
                self.opcodeStr.append("B")
                self.arg1.append(SetUp.imm_bit_to_32_bit_converter((int(instructions[i], base=2) & MASKS.bMask), 26))
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("#" + str(self.arg1[i]))
                self.arg2Str.append("")
                self.arg3Str.append("")
                """# I-Type"""
            elif 1160 <= opcode[i] <= 1161:  # ADDI OPCODE RANGE
                self.instrSpaced.append(SetUp.bin2StringSpacedI(instructions[i]))
                self.opcodeStr.append("ADDI")
                self.arg1.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg2.append((int(instructions[i], base=2) & MASKS.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & MASKS.imMask) >> 10)
                self.arg1Str.append("R" + str(self.arg1[i]))
                self.arg2Str.append(", R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg3[i]))
            elif 1672 <= opcode[i] <= 1673:  # SUBI OPCODE RANGE
                self.instrSpaced.append(SetUp.bin2StringSpacedI(instructions[i]))
                self.opcodeStr.append("SUBI")
                self.arg1.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg2.append((int(instructions[i], base=2) & MASKS.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & MASKS.imMask) >> 10)
                self.arg1Str.append("R" + str(self.arg1[i]))
                self.arg2Str.append(", R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg3[i]))
                """"# D-Type"""
            elif opcode[i] == 1984:  # STUR OPCODE
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("STUR")
                self.arg1.append((int(instructions[i], base=2) & MASKS.addrMask) >> 12)
                self.arg2.append((int(instructions[i], base=2) & MASKS.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", [R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg1[i]) + "]")
            elif opcode[i] == 1986:  # LDUR OPCODE
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("LDUR")
                self.arg1.append((int(instructions[i], base=2) & MASKS.addrMask) >> 12)
                self.arg2.append((int(instructions[i], base=2) & MASKS.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", [R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg1[i]) + "]")
                """"# CB Type"""
            elif 1440 <= opcode[i] <= 1447:  # CBZ OPCODE RANGE
                self.instrSpaced.append(SetUp.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBZ   ")
                self.arg1.append(SetUp.imm_bit_to_32_bit_converter((int(instructions[i], base=2) & MASKS.addr2Mask) >>
                                                                   5, 19))
                self.arg2.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg3.append(0)
                self.arg1Str.append("R" + str(self.arg2[i]))
                self.arg2Str.append(", #" + str(self.arg1[i]))
                self.arg3Str.append("")
            elif 1448 <= opcode[i] <= 1455:  # CBNZ OPCODE RANGE
                self.instrSpaced.append(SetUp.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBNZ")
                self.arg1.append(SetUp.imm_bit_to_32_bit_converter((int(instructions[i], base=2) & MASKS.addr2Mask) >>
                                                                   5, 19))
                self.arg2.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg3.append(0)
                self.arg1Str.append("R" + str(self.arg2[i]))
                self.arg2Str.append(", #" + str(self.arg1[i]))
                self.arg3Str.append("")
                """"# IM Type"""
            elif 1684 <= opcode[i] <= 1687:  # MOVZ OPCODE RANGE
                self.instrSpaced.append(SetUp.bin2StringSpacedIM(instructions[i]))
                self.opcodeStr.append("MOVZ")
                self.arg1.append(((int(instructions[i], base=2) & MASKS.imsftMask) >> 21) * 16)  # need to send to
                self.arg2.append((int(instructions[i], base=2) & MASKS.imdataMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", " + str(self.arg2[i]))
                self.arg3Str.append(", LSL " + str(self.arg1[i]))
            elif 1940 <= opcode[i] <= 1943:  # MOVK OPCODE RANGE
                self.instrSpaced.append(SetUp.bin2StringSpacedIM(instructions[i]))
                self.opcodeStr.append("MOVK")
                self.arg1.append(((int(instructions[i], base=2) & MASKS.imsftMask) >> 21) * 16)  # need to send to
                self.arg2.append((int(instructions[i], base=2) & MASKS.imdataMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & MASKS.rdMask) >> 0)
                self.arg1Str.append("R" + str(self.arg3[i]))
                self.arg2Str.append(", " + str(self.arg2[i]))
                self.arg3Str.append(", LSL " + str(self.arg1[i]))
                """NOP"""
            elif opcode[i] == 0:  # NOP OPCODE
                self.instrSpaced.append(SetUp.bin2StringSpaced(instructions[i]))
                self.opcodeStr.append("NOP")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                """"# Break"""
            elif opcode[i] == 2038 and (int(instructions[i], base=2) & MASKS.specialMask) == 2031591:  # BREAK OPCODE
                self.instrSpaced.append(SetUp.bin2StringSpaced(instructions[i]))
                self.opcodeStr.append("BREAK")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                # print("breaking\n")
                break
            else:
                self.opcodeStr.append("unknown")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                print("i =: " + str(i))
                print("opcode =: " + str(opcode[i]))
                sys.exit("You have found an unknown instruction, investigate NOW")

        counter = 0

        for j in range(self.numInstructs, len(instructions)):
            self.rawdata.append(instructions[j])
            self.dataval.append(SetUp.imm_32_bit_unsigned_to_32_bit_signed_converter(int(self.rawdata[counter], base=2)))
            counter += 1

        return {
            "opcode": opcode,
            "dataval": self.dataval,
            "address": self.address,
            "numInstructs": self.numInstructs,
            "arg1": self.arg1,
            "arg2": self.arg2,
            "arg3": self.arg3,
            "opcodeStr": self.opcodeStr,
            "arg1Str": self.arg1Str,
            "arg2Str": self.arg2Str,
            "arg3Str": self.arg3Str
        }

    def print(self):
        # the following lines write the disassemble out to a file
        outFile = open(SetUp.get_output_filename() + "_dis.txt", 'w')

        for i in range(self.numInstructs):
            outFile.write(str(self.instrSpaced[i]) + '\t' + str(self.address[i]) + '\t'
                          + str(self.opcodeStr[i]) + '\t' + str(self.arg1Str[i]) + str(self.arg2Str[i])
                          + str(self.arg3Str[i]) + '\n')

        for i in range(len(self.dataval)):
            outFile.write(self.rawdata[i] + '\t' + str(self.address[i + self.numInstructs]) + '\t'
                          + str(self.dataval[i]) + '\n')

        outFile.close()
