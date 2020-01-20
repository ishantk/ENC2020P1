# single value container
num = 10

# multi value container
numbers = 10, 20, 30, 40, 50

"""
    
    state      partyA      partyB
    ------------------------------
    punjab     34567       12345
    haryana    23111       67655
    himachal   76551       23982
    up         11123       33121
    goa        54134       12332

"""
punjabPartyA = 34567
haryanaPartyA = 23111
himachalPartyA = 76551
upPartyA = 11123
goaPartyA = 54134

punjabPartyB = 12345
haryanaPartyB = 67655
himachalPartyB = 23982
upPartyB = 33121
goaPartyB = 12332

partyAVoteCount = punjabPartyA + haryanaPartyA + himachalPartyA + upPartyA + goaPartyA
partyBVoteCount = punjabPartyB + haryanaPartyB + himachalPartyB + upPartyB + goaPartyB

print(">> partyAVoteCount:", partyAVoteCount)
print(">> partyBVoteCount:", partyBVoteCount)

if partyAVoteCount > partyBVoteCount:
    print(">> PartyA won elections by",(partyAVoteCount - partyBVoteCount), "votes")
else:
    print(">> PartyB won elections by", (partyBVoteCount - partyAVoteCount), "votes")

# Challenge : Whenever data increases Single Value Containers are not a good choice
#             Developer's Time will be wasted


#              0        1       2      3     4
partyAVotes = 34567, 23111, 76551, 11123, 54134
partyBVotes = 12345, 67655, 23982, 33121, 12332

partyAVoteCount = 0
partyBVoteCount = 0

# partyAVoteCount = partyAVotes[0] + partyAVotes[1] + partyAVotes[2] + partyAVotes[3] + partyAVotes[4]
for i in range(0, len(partyAVotes)):
    # print(partyAVotes[i], " | ", partyBVotes[i])
    partyAVoteCount = partyAVoteCount + partyAVotes[i]
    partyBVoteCount = partyBVoteCount + partyBVotes[i]

if partyAVoteCount > partyBVoteCount:
    print(">> PartyA won elections by",(partyAVoteCount - partyBVoteCount), "votes")
else:
    print(">> PartyB won elections by", (partyBVoteCount - partyAVoteCount), "votes")

