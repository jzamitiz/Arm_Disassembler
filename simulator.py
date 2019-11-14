import sys
from helpers import SetUp
import masking_constants as MASKs


class State:
    # dataval = []
    PC = 96
    cycle = 1
    R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, opcodes, dataval, addrs, arg1, arg2, arg3, numInstructs, opcodeStr, arg1Str, arg2Str, arg3Str):
        self.opcode = opcodes
        self.dataval = dataval
        self.address = addrs
        self.numInstructions = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.opcodeStr = opcodeStr
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str

    def getIndexOfMemAddress(self, currAddr):
        index = (currAddr - 96)/4
        return int(index)

    def incrementPC(self):
        self.PC += 4
        self.address.append(self.address[len(self.address) - 1] + 4)
        return self.PC

    def printState(self):

        outputFileName = SetUp.get_output_filename()
        with open(outputFileName + "_sim.txt", "a") as outFile:

            i = self.getIndexOfMemAddress(self.PC)
            outFile.write("====================\n")
            outFile.write(
                "cycle:" + str(self.cycle) + "\t" + str(self.PC) + "\t" + self.opcodeStr[i] + "\t" + self.arg1Str[i]
                + self.arg2Str[i] + self.arg3Str[i] + "\n")
            outFile.write("\n")
            outFile.write("registers:\n")

            outStr = "r00:"
            for i in range(0, 8):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr)
            outFile.write("\n")

            outStr = "r08:"
            for i in range(8, 16):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr)
            outFile.write("\n")

            outStr = "r16:"
            for i in range(16, 24):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr)
            outFile.write("\n")

            outStr = "r24:"
            for i in range(24, 32):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr)
            outFile.write("\n")

            outFile.write("\ndata:\n")
            outStr = "\n"
            for i in range(len(self.dataval)):

                if i % 8 == 0 and i != 0 or i == len(self.dataval):
                    outFile.write(outStr + "\n")

                if i % 8 == 0:
                    outStr = str(self.address[i + self.numInstructions]) + ":" + str(self.dataval[i])

                if i % 8 != 0:
                    outStr = outStr + "\t" + str(self.dataval[i])

            outFile.write(outStr + "\n")
        outFile.close()


class Simulator:

    def __init__(self, opcode, dataval, address, arg1, arg2, arg3, numInstructs, opcodeStr, arg1Str, arg2Str, arg3Str):
        self.opcode = opcode
        self.dataval = dataval
        self.address = address
        self.numInstructs = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.opcodeStr = opcodeStr
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str
        self.specialMask = MASKs.specialMask

    def run(self):
        foundBreak = False
        armState = State(self.opcode, self.dataval, self.address, self.arg1, self.arg2, self.arg3, self.numInstructs,
                         self.opcodeStr, self.arg1Str, self.arg2Str, self.arg3Str)

        while not foundBreak:
            jumpAddr = armState.PC
            # get the next instruction
            i = armState.getIndexOfMemAddress(armState.PC)

            # TODO test and delete the need for instructions
            # if self.instructions[i] == '00000000000000000000000000000000':
            # #NOP this might still be wrong need to test more
            if self.opcode[i] == 0:
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1112:  # ADD OPCODE
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] + armState.R[self.arg1[i]]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1624:  # SUB OPCODE
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] - armState.R[self.arg2[i]]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1104:  # AND OPCODE
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] & armState.R[self.arg1[i]]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1360:  # ORR OPCODE
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] | armState.R[self.arg1[i]]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1872:  # EOR OPCODE
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] ^ armState.R[self.arg1[i]]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1691:  # LSL OPCODE mask
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] << armState.R[self.arg2[i]]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1690:  # LSR OPCODE
                armState.R[self.arg3[i]] = (armState.R[self.arg1[i]] % (1 << 32) >> self.arg2[i])
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1692:  # ASR OPCODE
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] >> self.arg2[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif 160 <= self.opcode[i] <= 191:  # B
                armState.printState()
                jumpAddr += ((self.arg1[i] * 4) - 4)  # -4 takes care on incrementing the PC later
                armState.PC = jumpAddr
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif 1160 <= self.opcode[i] <= 1161:  # ADDI OPCODE RANGE
                armState.R[self.arg1[i]] = armState.R[self.arg2[i]] + self.arg3[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif 1672 <= self.opcode[i] <= 1673:  # SUBI OPCODE RANGE
                armState.R[self.arg1[i]] = armState.R[self.arg2[i]] - self.arg3[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1984:  # STUR OPCODE
                calculated_address = armState.R[self.arg2[i]] + (self.arg1[i] * 4)
                initial_mem_address = 96 + (self.numInstructs * 4)
                index_in_mem = (calculated_address - initial_mem_address) // 4
                if index_in_mem < 0:
                    print("Not within range of memory!")
                    exit(-1)
                elif index_in_mem < len(self.dataval):
                    self.dataval[index_in_mem] = armState.R[self.arg3[i]]
                else:
                    while (len(self.dataval)) < index_in_mem:
                        self.dataval.append(0)
                        self.address.append(self.address[len(self.address) - 1] + 4)
                    self.dataval.append(armState.R[self.arg3[i]])
                    if index_in_mem % 8 != 0:
                        add_zero_amt = 7 - (index_in_mem % 8)
                        for i in range(add_zero_amt):
                            self.dataval.append(0)

                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1986:  # LDUR OPCODE
                calculated_address = armState.R[self.arg2[i]] + (self.arg1[i] * 4)
                initial_mem_address = 96 + (self.numInstructs * 4)
                index_in_mem = (calculated_address - initial_mem_address) // 4

                if index_in_mem < 0:
                    print("Not within range of memory!")
                    exit(-1)
                elif index_in_mem < len(self.dataval):
                    armState.R[self.arg3[i]] = self.dataval[index_in_mem]
                else:
                    print("Not within range of memory!")
                    exit(-1)

                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif 1440 <= self.opcode[i] <= 1447:  # CBZ OPCODE RANGE
                if armState.R[self.arg2[i]] == 0:
                    armState.printState()
                    jumpAddr += ((self.arg1[i] * 4) - 4)
                    armState.PC = jumpAddr
                    armState.incrementPC()
                    armState.cycle += 1
                    continue  # go back to top
                else:
                    armState.printState()
                    armState.incrementPC()
                    armState.cycle += 1
                    continue  # go back to top

            elif 1448 <= self.opcode[i] <= 1455:  # CBNZ OPCODE RANGE
                if armState.R[self.arg2[i]] != 0:
                    armState.printState()
                    jumpAddr += ((self.arg1[i] * 4) - 4)
                    armState.PC = jumpAddr
                    armState.incrementPC()
                    armState.cycle += 1
                    continue  # go back to top
                else:
                    armState.printState()
                    armState.incrementPC()
                    armState.cycle += 1
                    continue  # go back to top

            elif 1940 <= self.opcode[i] <= 1943:  # MOVK OPCODE RANGE
                mask = 0xFFFF << self.arg1[i]
                armState.R[self.arg3[i]] = self.arg3[i] & mask  # Rd & w/ mask
                armState.R[self.arg3[i]] = self.arg3[i] ^ mask
                armState.R[self.arg3[i]] = self.arg3[i] | (self.arg2[i] << self.arg1[i])
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif 1684 <= self.opcode[i] <= 1687:  # MOVZ OPCODE RANGE
                armState.R[self.arg3[i]] = 0  # armState.R[self.arg2[i]] << self.arg1[i]
                if self.arg1[i] == 0:
                    armState.R[self.arg3[i]] = self.arg2[i]
                else:
                    armState.R[self.arg3[i]] = self.arg2[i] * self.arg1[i] * 2
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 2038:
                # and (int(self.instructions[i], base=2) & self.specialMask) ==2031591: #break
                foundBreak = True

            else:

                print("IN SIM -- UNKNOWN INSTRUCTION ------------------- !!!!")

            armState.printState()
            armState.PC = jumpAddr
            armState.incrementPC()
            armState.cycle += 1
