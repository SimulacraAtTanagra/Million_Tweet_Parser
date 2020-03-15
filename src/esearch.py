from elasticsearch import Elasticsearch
import json
from datetime import datetime
def create_and_update_index(index_name, doc_type):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except Exception:
        pass

    es.indices.put_mapping(
        index=index_name,
        doc_type=doc_type,
        body={
            doc_type: {
                "properties": {"issue_date": {"type": "date"},
                "fine_amount":{"type":"integer"},
                "penalty_amount":{"type": "integer"},
                "interest_amount":{"type": "integer"},
                "reduction_amount":{"type":"integer"},
                "payment_amount":{"type":"integer"},
                "amount_due":{"type":"integer"}}
            }
        }
    )

    return es

def push(listobj,es,page_size):
    for i in range(len(listobj)):
        print(i)
        print(listobj[i])
        for j in range(page_size):
            print(j)
            print(listobj[i][j])
            listobj[i][j]['issue_date'] = datetime.strptime(listobj[i][j]['issue_date'],'%m/%d/%Y')
            es.index(index="parking_violations_index",ignore=400,doc_type="violations",id=int(listobj[i][j]['summons_number']), body=(listobj[i][j]))

if __name__ == "__main__":
    es = create_and_update_index('parking_violations_index','violations')
    
