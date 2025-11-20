from pathlib import Path
from xml.dom.minidom import parse

xml_path = Path(__file__).resolve().parent / "employees.xml"
DOMTree = parse(str(xml_path))
root = DOMTree.documentElement
employees = root.getElementsByTagName("employee")

for employee in employees:
    tag_id = employee.getElementsByTagName("id")[0]
    tag_name = employee.getElementsByTagName("name")[0]
    emp_id = tag_id.childNodes[0].data.strip()
    name = tag_name.childNodes[0].data.strip()
    print(emp_id, "\t", name)
