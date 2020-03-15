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

def push(listobj,es):
    for i in range(len(listobj)):
        listobj[0]['issue_date'] = datetime.strptime(listobj[0]['issue_date'],'%m/%d/%Y')
        es.index(index="myindex",ignore=400,doc_type="violations",id=1, body=(listobj[i][0]))

if __name__ == "__main__":
    es = create_and_update_index('parking_violations_index','violations')
    
