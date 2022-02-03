import xml.etree.ElementTree as etree
"""import xml.etree.Element as e"""
import os
from os.path import isfile, join
import pandas as pd


path =r'C:\Users\цук\Documents\BPS\Datev_Belege14'
list_of_files = []

keys = ['{http://xml.datev.de/bedi/tps/ledger/v050}date', 
'{http://xml.datev.de/bedi/tps/ledger/v050}accountNo', 
'{http://xml.datev.de/bedi/tps/ledger/v050}buCode',
'{http://xml.datev.de/bedi/tps/ledger/v050}tax',
'{http://xml.datev.de/bedi/tps/ledger/v050}information',
'{http://xml.datev.de/bedi/tps/ledger/v050}currencyCode',
'{http://xml.datev.de/bedi/tps/ledger/v050}invoiceId',
'{http://xml.datev.de/bedi/tps/ledger/v050}bookingText',
'{http://xml.datev.de/bedi/tps/ledger/v050}partyId',
'{http://xml.datev.de/bedi/tps/ledger/v050}vatId',
'{http://xml.datev.de/bedi/tps/ledger/v050}accountName',
'{http://xml.datev.de/bedi/tps/ledger/v050}dueDate',
'{http://xml.datev.de/bedi/tps/ledger/v050}bpAccountNo',
'{http://xml.datev.de/bedi/tps/ledger/v050}supplierName',
'{http://xml.datev.de/bedi/tps/ledger/v050}supplierCity'
]
lstKey = []
lstValue = []
lstFile = []
lstAmount = []

for root, dirs, files in os.walk(path):
    for file in files:
        tree=etree.parse(path + "\\" + str(file))
        root = tree.getroot()
        for child in root:
            for accPay in child:
                    amount = accPay.find('{http://xml.datev.de/bedi/tps/ledger/v050}amount').text
                    for i in range(1,16):
                        lstFile.append(str(file))
                        lstAmount.append(str(amount))
                        lstKey.append(str(keys[i-1]))
                        if accPay.find(keys[i-1]) is None:
                            lstValue.append("none")
                        else:
                            lstValue.append(accPay.find(keys[i-1]).text.replace(u'\u000d',' '))
                        
print(len(lstFile), len(lstAmount), len(lstKey), len(lstValue)) # Print all of them out here

df = pd.DataFrame({'file': lstFile, 'amount' : lstAmount,'key' : lstKey, 'value' : lstValue})
df.sort_values('key')
res = df.pivot_table(index=['file', 'amount'], columns='key',
                     values='value', aggfunc= 'min').reset_index()
res.to_csv('dataframe2021_BPSI_012022.txt', index=False, sep='&', header=['file', 'amount', 'accountName','information', 'accountNo','partyId',
 'buCode', 'currencyCode', 'date', 'dueDate',
     'bookingText','invoiceId','bpAccountNo', 'supplierCity', 'supplierName', 'tax','vatId'])


"""data_frame = pandas.DataFrame()"""
"""print(rootnode)
        LedgerImport = root.find('LedgerImport')
        if LedgerImport is not None:
            consolidate = LedgerImport.find('consolidate')
            accountsPayableLedger = consolidate.findAll('accountsPayableLedger')
            print(accountsPayableLedger.find("amount").text)"""
"""for doc in group.findall('document'):
               refid = doc.get('refid')"""
"""for tag in roonode.findall('name'):
            nvalue = tag"""
"""root=XmlD.getroot()"""
""""for target in root.findall("//consolidate"):
            attributes = target.findall(".//accountsPayableLedger")
            for attribute in attributes:
                childs = attribute.getChildren()
                for child in childs:
                    print(child.text)"""
"""for i in root.findall('consolidate/accountsPayableLedger'):
            print(i.descendants.get('date'))"""
"""xmle = e.parse(path+"\\"+str(file))"""

"""for each  child in root:
            print(child.tag, child.attrib)
            for children in child:
                for children in child:
                    print(children.text)
        list_of_files.append(os.path.join(root,file))"""
"""NodeList nodes1 = e.getChildNodes();
        for(int i =0; i < nodes1.getLength(); i++){
            NodeList nodes2 = i.getChildNodes();
            if(child.getNodeType() == e.element_node){
                String tagName = child.getTagName();
                if(!tagName.equals("files")){
                   System.out.println(tagName + " : " + child.getTextContent());
                    }else{
                   NodeList filesChilds = child.getChildNodes();
                   for(int j = 0; j < filesChilds.getLength(); j++){
                      //and like above
                   }
                }
            }
        }"""
for name in list_of_files:
        print(name)