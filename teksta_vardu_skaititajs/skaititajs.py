teksts = ""
with open("teksta_vardu_skaititajs/teksts.txt", "r", encoding="utf-8") as f:
    teksts = f.read()

vardi = teksts.split()
for i in range(len(vardi)):
    vardi[i] = vardi[i].strip(".,!-?*\'\")(")
    vardi[i] = vardi[i].lower()

visi_vardi = {}

for vards in vardi:
    if len(vards) >= 4: 
        if vards in visi_vardi:
            visi_vardi[vards] += 1
        else:
            visi_vardi[vards] = 1

biezakie_vardi = sorted(visi_vardi.items(), key=lambda x: x[1], reverse=True)[:5]
print("5 biežākie vārdi:")
for vards, biežums in biezakie_vardi:
    print(vards, biežums)

pirmie_4_burti = {}

for vards in vardi:
    if len(vards) >= 4:
        pirmie_4_burti_key = vards[:4]
        if pirmie_4_burti_key in pirmie_4_burti:
            pirmie_4_burti[pirmie_4_burti_key] += 1
        else:
            pirmie_4_burti[pirmie_4_burti_key] = 1

print("\nVārdu grupas ar identiskiem pirmajiem 4 burtiem:")
for grupa, skaits in pirmie_4_burti.items():
    print(f"{grupa}: {skaits}")