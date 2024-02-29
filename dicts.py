print("codeNest sollution members profiles")

devolopers = {"BD":"yameen tareen",
              "full stack":"mr umair",
              "data science":"asad rind",
              "web dev":"haris",
              "interns":"hasnain and tayyab",
              "bussniss manager": "fida boss",
              }

devolopers.pop("BD")

for key , value in devolopers.items():
    print(f"{key} : {value}")