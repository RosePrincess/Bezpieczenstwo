import json
import os
from heapq import heappush, nlargest, nsmallest
from math import ceil

all_parties = ["PO", "PIS", "SLD", "RP", "PSL", "WMN", "PPP", "PJN", "NPJKM", "NDPSAL", "P"]
parties = ["PO", "PIS", "SLD", "RP", "PSL", "WMN"]
#parties
results = [0,0,0,0,0,0,0,0,0,0,0]

with open(os.path.dirname(os.path.realpath(__file__))+'/results2011.json', "r") as f:
    data = json.load(f)

with open(os.path.dirname(os.path.realpath(__file__))+'/r2011.txt', "w+") as file:
    file.write("Rozdane mandaty w poszczególnych okręgach:\n")
    file.write("Nr okręgu & Nazwa okręgu")
    for party in parties:
        file.write(" & " + party)
    file.write("\\" + "\\\n \hline \n")

    for row in data:
        mandates = row["mandaty"]

        div = 0
        dhondt = []
        temp_results = []
        # if row['nr'] == 31:
        #         print("\nn & PO & PIS & SLD & RP & PSL & MN \\" + "\\")
        for i in range(mandates):
            div += 1   
            s = str(div)    

            for partyNumber, party in enumerate(parties):
                item = (row[party]/div, parties[partyNumber], partyNumber, div)
                heappush(dhondt,item)
                # if row['nr'] == 31:
                #     print(item)
            #     if row['nr'] == 31:
            #         s = s + " & " + str(row[party]/div)
            # if row['nr'] == 31:
            #     print(s + " \\" + "\\")
    

        for i in range(len(parties)):
            temp_results.append(0)
        
        seatNumber = 1

        for (val, partyName, partyNumber, div) in nlargest(mandates,dhondt):
            temp_results[partyNumber] = temp_results[partyNumber] + 1
            seatNumber = seatNumber + 1
            lastSeatVal = val
            lastSeatPartyNumber = partyNumber
            lastSeatPartyName = partyName
            lastSeatDiv = div
            # if row['nr'] == 31:
            #     print(str(div) + " & " + partyName +  " & " + str(val))
    

        file.write(str(row["nr"]) + " & " + row["nazwa"])
        # for r in temp_results:
        #     file.write(" & " + str(r))
        
        file.write("\\" + "\\\n")
        for i in range(len(temp_results)):
            results[i] += temp_results[i]

    file.write("\n\nWyniki wyborów\n")
    file.write("Partia & Liczba mandatów \\" + "\\\n \hline \\n")

    for i in range(len(parties)):
        file.write(parties[i] + ' & ' + str(results[i]) + "\\" + "\\\n")
