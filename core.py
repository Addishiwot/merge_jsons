# buit in modules
import importlib
import json
import pathlib
from typing import Union, List, Tuple

# third party
from jsonmerge import Merger # type: ignore

Path = Union[str, pathlib.Path]


class Core:
    
    def __init__(self, plugins: List[str] = []) -> None:
        if plugins:
            self._plugins = [
                importlib.import_module(plugin, '.').Plugin() for plugin in plugins
                ] 
        else:
            # import the default plugin
            self._plugins = [
                importlib.import_module('plugins.default', '.').Plugin() 
                ]
            
    @staticmethod
    def _read_json(path: Path):
        with open(path) as f:
            return json.load(f)
    
    @staticmethod
    def _write(
        data: dict, 
        output_file_path: Path
        ):
        """ dumps JSON formatted string to a given file

        Args:
            data (dict): JSON formatted string
            output_file_path (P): path to a file. 
        """
        with open(output_file_path, 'w') as f:
            json.dump(data, f, indent=4)
            
    def _process_json(
        self,
        path_to_json1: Path, 
        path_to_json2: Path) -> Tuple[dict, dict]:
        """
        reads the contents of jsons and then retruns it.
        Args:
            path_to_json2 (P): path to the first json file
            path_to_json2 (P): path to the the second json file
        """

        base = self._read_json(path_to_json1)
        head = self._read_json(path_to_json2)
        
        return base, head
        
        
    def _merge(
        self,
        base: dict,
        head:dict, 
        schema:dict
        ) -> dict:
        """
        merges two dictionaries according to the given schema
        Args:
            base (dict): data dict from the first json file
            head (dict): data dict from the second json file
            schema (dict): schema describing how the jsons should be merged

        Returns:
            rtype: dict
        """
        
        merger = Merger(schema)
        result = merger.merge(base, head)
        
        return result


    def run(self):
        
        for plugin in self._plugins:
            
            base, head = self._process_json(plugin.json1, plugin.json2)
            result = self._merge(base, head, plugin.schema)
            self._write(result, plugin.result)
        

