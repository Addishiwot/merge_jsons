import os

class Plugin:
    
    def __init__(self) -> None:
        self._dir_name = os.path.dirname(os.path.abspath(__file__))
        
        self.json1 = os.path.join(self._dir_name, 'json1.json')
        self.json2 = os.path.join(self._dir_name, 'json2.json')
        self.result = os.path.join(self._dir_name, 'retult.json') 
        self.schema = {
            "properties":{
                "widgets":{
                    "mergeStrategy":"arrayMergeById",
                    "mergeOptions":{
                                    "idRef":"/_id"
                                },
                    "items":{
                        "mergeStrategy":"objectMerge",
                        "properties":{
                            "sources":{
                                "mergeStrategy":"arrayMergeById",
                                "mergeOptions":{
                                    "idRef":"/source"
                                        }
                                },
                            "columns":{
                                "mergeStrategy":"arrayMergeById",
                                "mergeOptions":{
                                    "idRef":"/label"
                                    }
                                }
                            }
                        }
                    }
                }
            }