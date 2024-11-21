employees = {
    "name": "saxor", 
    "age": 22, 
    "addresss": "nasugbu"
}
#print(employees)

employees2 = {
    "name": "melvinn",
    "status": "S", 
    "profile": {
        "department": "CICS", 
        "room": "IMT",
        "cofaculty": ["meo", "oli", "pay"]
    }
}
imt_value = employees2["profile"]["room"]
print(imt_value)
