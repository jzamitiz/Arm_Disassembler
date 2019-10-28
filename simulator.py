import sys
from helpers import SetUp
import masking_constants as MASKs


class State:
    dataval = []
    PC = 96
    cycle = 1
    R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, opcode, dataval, address, arg1, arg2, arg3, numInstructs, opcodeStr, arg1Str, arg2Str, arg3Str):
        self.opcode = opcode
        self.dataval = dataval
        self.address = address
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
        PC = self.PC + 4
        return PC

    def printState(self):

        outputFileName = SetUp.get_output_filename()

        with open(outputFileName + "_sim.txt", "a") as outFile:

            j = self.getIndexOfMemAddress(self.PC)
            outFile.write("====================\n")
            outFile.write(
                "cycle:" + str(self.cycle) + "\t" + str(self.PC) + "\t" + self.opcodeStr[j] + "\t" + self.arg1Str[j]
                + self.arg2Str[j] + self.arg3Str[j] + "\n")
            outFile.write("\n")
            outFile.write("registers:\n")
            outStr = "r00:\t"
            for i in range(0, 8):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr)
            outFile.write("\n")

            outStr = "r08:\t"
            for i in range(8, 16):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr)
            outFile.write("\n")

            outStr = "r16:\t"
            for i in range(16, 24):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr)
            outFile.write("\n")

            outStr = "r24:\t"
            for i in range(24, 32):
                outStr = outStr + "\t" + str(self.R[i])
            outFile.write(outStr)

            outFile.write("\n\n")
            outFile.write("data:\n")
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
                self.arg3[i] = self.arg2[i] + self.arg1[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1624:  # SUB OPCODE
                self.arg3[i] = self.arg1[i] - self.arg2[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1104:  # AND OPCODE
                self.arg3[i] = self.arg2[i] & self.arg1[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1360:  # ORR OPCODE
                self.arg3[i] = self.arg2[i] | self.arg1[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1872:  # EOR OPCODE
                self.arg3[i] = self.arg2[i] ^ self.arg1[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1691:  # LSL OPCODE
                self.arg3[i] = self.arg1[i] << self.arg2[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1690:  # LSR OPCODE
                self.arg3[i] = self.arg1[i] >> self.arg2[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif self.opcode[i] == 1692:  # ASR OPCODE
                self.arg3[i] = self.arg1[i] / (2*self.arg2[i])
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif 160 <= self.opcode[i] <= 191:  # B
                jumpAddr += ((self.arg1[i] * 4) - 4)  # -4 takes care on incrementing the PC later
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif 1160 <= self.opcode[i] <= 1161:  # ADDI OPCODE RANGE
                self.arg1[i] = self.arg2[i] + self.arg3[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif 1672 <= self.opcode[i] <= 1673:  # SUBI OPCODE RANGE
                self.arg1[i] = self.arg2[i] - self.arg3[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif 1440 <= self.opcode[i] <= 1447:  # CBZ OPCODE RANGE
                if self.arg2[i] == 0:
                    jumpAddr += ((self.arg1[i] * 4) - 4)
                    armState.printState()
                    armState.incrementPC()
                    armState.cycle += 1
                    continue  # go back to top
                else:
                    armState.printState()
                    armState.incrementPC()
                    armState.cycle += 1
                    continue  # go back to top

            elif 1448 <= self.opcode[i] <= 1455:  # CBNZ OPCODE RANGE
                if self.arg2[i] != 0:
                    jumpAddr += ((self.arg1[i] * 4) - 4)
                    armState.printState()
                    armState.incrementPC()
                    armState.cycle += 1
                    continue  # go back to top
                else:
                    armState.printState()
                    armState.incrementPC()
                    armState.cycle += 1
                    continue  # go back to top

            elif 1940 <= self.opcode[i] <= 1943:  # MOVK OPCODE RANGE
                self.arg3[i] = self.arg2[i] << self.arg1[i]
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue  # go back to top

            elif 1684 <= self.opcode[i] <= 1687:  # MOVZ OPCODE RANGE
                self.arg3[i] = self.arg2[i] << self.arg1[i]
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