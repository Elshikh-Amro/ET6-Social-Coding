# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 15:30:30 2025

@author: somai
Challenge 2: Digital Access Control
Objective
Use set operations to analyze and improve a company's digital access control system while identifying potential security risks in data access.
Scenario
A secure company vault stores sensitive data, where employees are granted access based on their roles:
Finance Team (F): Needs access to financial records.
Tech Team (T): Needs access to technical documents.
Some employees belong to both teams due to cross-departmental responsibilities.
Access Data (Given)
The security system tracks employee IDs (formatted as "E####").
finance_access = {"E0435", "E1021", "E3098", "E7642", "E8873", "E6590"}
tech_access = {"E7642", "E8873", "E6590", "E9812", "E4520"}
Additionally, two special cases exist:
E0001 (Admin): Has access to all data but is not listed in specific access groups.
E9999 (New Employee): Has no assigned access yet.
Your Task
Analyze the current access structure and identify potential security risks by answering the following:
Who has access to at least one type of data?
Who has access to both financial and technical data?
Who has exclusive access to only one type of data?
Which employees currently lack access (but exist in the system)?
Are there unnecessary overlaps in access that could pose a security risk?
What changes would you recommend to enhance security and minimize excessive access?
# -*- coding: utf-8 -*-

"""
finance_access = set(["E0435", "E1021", "E3098", "E7642", "E8873", "E6590"])

tech_access = set(["E7642", "E8873", "E6590", "E9812", "E4520"])

admin_access = set(["E0001"])

new_employee = 'E9999'

un = finance_access.union(tech_access).union(admin_access)

y = finance_access.intersection(tech_access)

x = finance_access.symmetric_difference(tech_access)

 

 

print("This people have access to at least one type of data",un)

print("This people have access to both financial and tech documents", x)

print("This people have access to exclusively one data type", y)

print("Which employees currently lack access is ", new_employee)

#Are there unnecessary overlaps in access that could pose a security risk? because there is employees have access to both technical and financial.
#What changes would you recommend to enhance security and minimize excessive access? restructure the acces credintials so there is not any intersections between technical and financial data
