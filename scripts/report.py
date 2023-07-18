#!/usr/bin/env python3
#!/usr/bin/env python3

import reports
import emails
import os 
from datetime import date
 

 
def process_data(data):
    for item in data:
        report.append("name: {}<br/>weight: {}\n".format(item[0], item[1]))
    return report
 
text_data = []
for text_file in list_files:
    with open(desc_path + text_file, 'r') as f:
        text_data.append([line.strip() for line in f.readlines()])
        f.close()
 
if __name__ == "__main__":
    """
    You will need to pass the following arguments to the reports.generate_report method: 
    * the text description processed from the text files as the paragraph argument, 
    * the report title as the title argument, 
    * and the file path of the PDF to be generated as the attachment argument (use ‘/tmp/processed.pdf')
    """
    summary = process_data(text_data)
    paragraph = "<br/><br/>".join(summary)
    title = "Processed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
    attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, paragraph)

