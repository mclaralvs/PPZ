import querido_diario

# Returns all gazettes between 01/01/2020 and 31/01/2021 that contains the words
# 'covid' and 'cloroquina' from territory '2927408 ' (Salvador)
gazettes = querido_diario.gazettes(
   since="2020-01-01",
   until="2021-01-31",
   keywords=["Bruno", "Reis"],
   territory_id="2927408",
   offset=0,
   size=10
)

for g in gazettes['gazettes']: print (g)
