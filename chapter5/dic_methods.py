marks={
    "moiz": 100,
    "ali": 90,
    "sara": 85,
    "john": 95,
    "linda": 88
}
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"moiz": 95, "ali": 92})
print(marks)
print(marks.get("moiz"))#prints none if key not found
